import { useState } from "react";
import API from "../services/api";

function Register({ setPage }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleRegister = async () => {
        try {
            await API.post("/auth/register", { email, password });
            alert("Registered successfully");
            setPage("login");
        } catch {
            alert("Registration failed");
        }
    };

    return (
        <div>
            <h2>Register</h2>
            <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
            <input placeholder="Password" type="password" onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleRegister}>Register</button>
        </div>
    );
}

export default Register;