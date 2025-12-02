from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []

# Serve frontend
@app.route("/")
def home():
    return render_template("index.html")

# API – Get todos
@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# API – Add todo
@app.route("/api/todos", methods=["POST"])
def add_todo():
    data = request.json
    todo = {"id": len(todos) + 1, "task": data["task"]}
    todos.append(todo)
    return jsonify({"message": "Todo added", "todo": todo})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

