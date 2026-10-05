from flask import Flask, jsonify, request

app = Flask(__name__)

TASKS = []
_next_id = 1

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "luyava-ai-task-api"})

@app.get("/api/tasks")
def list_tasks():
    return jsonify({"tasks": TASKS, "count": len(TASKS)})

@app.post("/api/tasks")
def create_task():
    global _next_id
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    if not title:
        return jsonify({"error": "title is required"}), 400
    task = {"id": _next_id, "title": title, "description": str(data.get("description", "")).strip(), "status": "pending"}
    _next_id += 1
    TASKS.append(task)
    return jsonify(task), 201

@app.patch("/api/tasks/<int:task_id>")
def update_task(task_id):
    task = next((t for t in TASKS if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "task not found"}), 404
    data = request.get_json(silent=True) or {}
    if "title" in data:
        title = str(data["title"]).strip()
        if not title:
            return jsonify({"error": "title cannot be empty"}), 400
        task["title"] = title
    if "description" in data:
        task["description"] = str(data["description"]).strip()
    if "status" in data:
        if data["status"] not in {"pending", "in_progress", "done"}:
            return jsonify({"error": "invalid status"}), 400
        task["status"] = data["status"]
    return jsonify(task)

@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    global TASKS
    before = len(TASKS)
    TASKS = [t for t in TASKS if t["id"] != task_id]
    if len(TASKS) == before:
        return jsonify({"error": "task not found"}), 404
    return "", 204

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
