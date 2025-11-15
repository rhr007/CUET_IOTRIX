import { useState } from "react";
import api from "../api/axiosClient";
import Swal from "sweetalert2";
import { Link } from "react-router-dom";

export default function Signup() {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async () => {
    if (!name || !phone || !password) {
      Swal.fire("Oops!", "All fields are required!", "warning");
      return;
    }

    if (phone.length < 4) {
      Swal.fire("Invalid Phone", "Phone number is too short!", "error");
      return;
    }

    if (password.length < 6) {
      Swal.fire(
        "Weak Password",
        "Password must be at least 6 characters long!",
        "error"
      );
      return;
    }

    try {
      const res = await api.post("/auth/signup", {
        name,
        phone,
        password,
        is_admin: false,
      });

      Swal.fire("Success!", res.data.message, "success");
      window.location.href = "/";
    } catch (err) {
      Swal.fire(
        "Error",
        err.response?.data?.detail || "Signup failed",
        "error"
      );
    }
  };

  return (
    <div className="h-screen flex items-center justify-center bg-gradient-to-br from-blue-100 to-purple-200">
      <div className="w-96 p-8 bg-white rounded-2xl shadow-xl border border-indigo-100">
        <h2 className="text-2xl font-bold mb-4 text-center text-indigo-700">
          Create Your Account
        </h2>

        <label className="text-gray-700 font-medium">Full Name</label>
        <input
          className="border w-full p-2 mb-4 rounded focus:ring-2 focus:ring-indigo-400 outline-none"
          placeholder="Enter your name"
          onChange={(e) => setName(e.target.value)}
          required
        />

        <label className="text-gray-700 font-medium">Phone Number</label>
        <input
          className="border w-full p-2 mb-4 rounded focus:ring-2 focus:ring-indigo-400 outline-none"
          placeholder="Enter phone number"
          onChange={(e) => setPhone(e.target.value)}
          required
        />

        <label className="text-gray-700 font-medium">Password</label>
        <input
          type="password"
          className="border w-full p-2 mb-6 rounded focus:ring-2 focus:ring-indigo-400 outline-none"
          placeholder="Create a password"
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button
          onClick={handleSignup}
          className="w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700 transition-all shadow-md hover:shadow-lg"
        >
          Sign Up
        </button>

        <p className="text-center text-sm text-gray-600 mt-4">
          Already have an account?{" "}
          <Link
            to="/"
            className="text-indigo-600 font-semibold hover:underline"
          >
            Login
          </Link>
        </p>
      </div>
    </div>
  );
}
