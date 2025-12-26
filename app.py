from flask import Flask, request, jsonify, render_template, redirect, url_for
from db import get_connection, init_db
from logger import logger
from config import DEBUG

app = Flask(__name__)

init_db()




@app.route("/api/tasks", methods=["POST"])
def create_task():
    try:
        data = request.get_json(force=True)

        if "title" not in data:
            return jsonify({"error": "Title is required"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tasks (title, description, due_date, status)
            VALUES (?, ?, ?, ?)
        """, (
            data["title"],
            data.get("description"),
            data.get("due_date"),
            data.get("status", "PENDING")
        ))

        conn.commit()
        conn.close()

        logger.info("Task created")
        return jsonify({"message": "Task created successfully"}), 201

    except Exception as e:
        logger.error(f"Create task failed: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        conn.close()

        tasks = [dict(row) for row in rows]
        return jsonify(tasks), 200

    except Exception as e:
        logger.error(f"Fetch tasks failed: {e}")
        return jsonify({"error": "Internal server error"}), 500



@app.route("/")
def task_list():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    return render_template("tasks.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add_task_ui():
    if request.method == "POST":
        data = {
            "title": request.form["title"],
            "description": request.form.get("description"),
            "due_date": request.form.get("due_date")
        }

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO tasks (title, description, due_date)
                VALUES (?, ?, ?)
            """, (
                data["title"],
                data["description"],
                data["due_date"]
            ))

            conn.commit()
            conn.close()

            logger.info("Task created via UI")

        except Exception as e:
            logger.error(f"UI task creation failed: {e}")

        return redirect(url_for("task_list"))

    return render_template("add_task.html")

@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task_api(task_id):
    try:
        data = request.get_json(force=True)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tasks
            SET title = ?, description = ?, due_date = ?, status = ?
            WHERE id = ?
        """, (
            data.get("title"),
            data.get("description"),
            data.get("due_date"),
            data.get("status"),
            task_id
        ))

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error": "Task not found"}), 404

        conn.commit()
        conn.close()

        return jsonify({"message": "Task updated successfully"}), 200

    except Exception as e:
        logger.error(f"API update failed: {e}")
        return jsonify({"error": "Internal server error"}), 500




@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task_api(task_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error": "Task not found"}), 404

        conn.commit()
        conn.close()

        return jsonify({"message": "Task deleted successfully"}), 200

    except Exception as e:
        logger.error(f"API delete failed: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task_ui(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        cursor.execute("""
            UPDATE tasks
            SET title = ?, description = ?, due_date = ?, status = ?
            WHERE id = ?
        """, (
            request.form["title"],
            request.form.get("description"),
            request.form.get("due_date"),
            request.form.get("status"),
            task_id
        ))

        conn.commit()
        conn.close()
        return redirect(url_for("task_list"))

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()

    if not task:
        return "Task not found", 404

    return render_template("edit_task.html", task=task)


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task_ui(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("task_list"))


if __name__ == "__main__":
    app.run(debug=DEBUG)
