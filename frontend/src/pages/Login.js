import { useState } from "react";
import API from "../services/api";

function Login({ setPage }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        try {
            const res = await API.post("/auth/login", new URLSearchParams({
                username: email,
                password: password,
            }));

            localStorage.setItem("token", res.data.access_token);
            alert("Login successful");
            setPage("dashboard");
        } catch (err) {
            alert("Login failed");
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
            <input placeholder="Password" type="password" onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleLogin}>Login</button>
            <button onClick={() => setPage("register")}>Go to Register</button>
        </div>
    );
}

export default Login;