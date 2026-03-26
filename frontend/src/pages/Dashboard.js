import { useEffect, useState } from "react";
import API from "../services/api";

function Dashboard() {
    const [tasks, setTasks] = useState([]);
    const [title, setTitle] = useState("");
    const [desc, setDesc] = useState("");

    const fetchTasks = async () => {
        const res = await API.get("/tasks");
        setTasks(res.data);
    };

    const createTask = async () => {
        await API.post("/tasks", { title, description: desc });
        fetchTasks();
    };

    const deleteTask = async (id) => {
        await API.delete(`/tasks/${id}`);
        fetchTasks();
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    return (
        <div>
            <h2>Dashboard</h2>

            <input placeholder="Title" onChange={(e) => setTitle(e.target.value)} />
            <input placeholder="Description" onChange={(e) => setDesc(e.target.value)} />
            <button onClick={createTask}>Add Task</button>

            {tasks.map((task) => (
                <div key={task.id}>
                    <p>{task.title}</p>
                    <button onClick={() => deleteTask(task.id)}>Delete</button>
                </div>
            ))}
        </div>
    );
}

export default Dashboard;