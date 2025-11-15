import { useState } from "react";
import api from "../api/axiosClient";
import Swal from "sweetalert2";

export default function Login() {
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault(); // prevent page reload

    // Frontend required check
    if (!phone || !password) {
      Swal.fire("Error", "Phone and Password are required", "error");
      return;
    }

    try {
      const res = await api.post("/auth/login", { phone, password });
      const { is_admin, user_id, name, points } = res.data;

      localStorage.setItem("user_id", user_id);
      localStorage.setItem("is_admin", is_admin);
      localStorage.setItem("user_name", name);
      localStorage.setItem("points", points);

      Swal.fire("Success!", "Logged in successfully.", "success");

      // Redirect based on role
      if (is_admin) window.location.href = "/admin";
      else window.location.href = "/puller";
    } catch (err) {
      console.log(err);
      Swal.fire("Error", err.response?.data?.detail || "Login failed", "error");
    }
  };

  return (
    <div className="h-screen flex items-center justify-center bg-gray-100">
      <div className="w-80 p-6 bg-white rounded shadow">
        <h2 className="text-xl font-bold mb-4">Login</h2>
        <form onSubmit={handleLogin}>
          <input
            className="border w-full p-2 mb-3"
            placeholder="Phone"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
          <input
            type="password"
            className="border w-full p-2 mb-3"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded hover:bg-green-600 cursor-pointer"
          >
            Login
          </button>
        </form>
        <button
          className="w-full text-blue-600 mt-3 cursor-pointer"
          onClick={() => (window.location.href = "/signup")}
        >
          Create Account
        </button>
      </div>
    </div>
  );
}
