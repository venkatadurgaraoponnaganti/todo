const API_URL = "/api/todos";

async function loadTodos() {
    const response = await fetch(API_URL);
    const todos = await response.json();

    const list = document.getElementById("todo-list");
    list.innerHTML = "";

    todos.forEach(todo => {
        const li = document.createElement("li");
        li.textContent = todo.task;
        list.appendChild(li);
    });
}

async function addTodo() {
    const task = document.getElementById("task-input").value;

    if (!task) return;

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task })
    });

    document.getElementById("task-input").value = "";
    loadTodos();
}

loadTodos();

