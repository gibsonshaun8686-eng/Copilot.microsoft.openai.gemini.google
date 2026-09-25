from flask import Flask, render_template_string, jsonify, request
import json
from pathlib import Path

app = Flask(__name__)

TASKS_PATH = Path("tasks.json")

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Automation Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2rem; background: #f4f7fb; color: #1f2937; }
    .card { background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 1rem; }
    h1 { margin-top: 0; }
    pre { background: #111827; color: #e5e7eb; padding: 1rem; border-radius: 8px; overflow-x: auto; }
    button { background: #2563eb; color: white; border: none; padding: 0.75rem 1rem; border-radius: 8px; cursor: pointer; }
    button:hover { background: #1d4ed8; }
    input, textarea { width: 100%; box-sizing: border-box; padding: 0.75rem; margin-top: 0.5rem; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Automation Dashboard</h1>
    <p>Run tasks from a simple dashboard and view the latest task output.</p>
    <button id="run-btn">Run tasks</button>
  </div>

  <div class="card">
    <h2>Task list</h2>
    <pre id="task-list">Loading...</pre>
  </div>

  <div class="card">
    <h2>Create a custom task</h2>
    <form id="task-form">
      <label>Task name
        <input type="text" name="name" value="dashboard-task" required>
      </label>
      <label>Action
        <input type="text" name="action" value="echo" required>
      </label>
      <label>Message
        <textarea name="message" rows="4">Hello from the dashboard</textarea>
      </label>
      <button type="submit">Add task</button>
    </form>
  </div>

  <div class="card">
    <h2>Latest output</h2>
    <pre id="output">No output yet.</pre>
  </div>

  <script>
    async function loadTasks() {
      const res = await fetch('/tasks');
      const tasks = await res.json();
      document.getElementById('task-list').textContent = JSON.stringify(tasks, null, 2);
    }

    document.getElementById('run-btn').addEventListener('click', async () => {
      const res = await fetch('/run', { method: 'POST' });
      const data = await res.json();
      document.getElementById('output').textContent = JSON.stringify(data, null, 2);
      loadTasks();
    });

    document.getElementById('task-form').addEventListener('submit', async (event) => {
      event.preventDefault();
      const form = new FormData(event.target);
      const task = {
        name: form.get('name'),
        action: form.get('action'),
        payload: { message: form.get('message') }
      };

      const res = await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(task)
      });

      const data = await res.json();
      document.getElementById('output').textContent = JSON.stringify(data, null, 2);
      loadTasks();
    });

    loadTasks();
  </script>
</body>
</html>
"""


def load_tasks():
    if not TASKS_PATH.exists():
        return []
    with TASKS_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with TASKS_PATH.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
        f.write("\n")


@app.route("/")
def index():
    return render_template_string(HTML)


@app.route("/tasks", methods=["GET", "POST"])
def tasks_api():
    if request.method == "GET":
        return jsonify(load_tasks())

    task = request.get_json(force=True)
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return jsonify({"status": "ok", "task": task})


@app.route("/run", methods=["POST"])
def run_tasks():
    tasks = load_tasks()
    results = []
    for task in tasks:
        name = task.get("name", "unnamed")
        action = task.get("action", "noop")
        payload = task.get("payload", {})

        if action == "echo":
            results.append({"name": name, "status": "ok", "message": payload.get("message", "Hello")})
        elif action == "noop":
            results.append({"name": name, "status": "ok", "message": "no-op"})
        else:
            results.append({"name": name, "status": "error", "message": f"Unsupported action: {action}"})

    return jsonify({"status": "ok", "results": results})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
