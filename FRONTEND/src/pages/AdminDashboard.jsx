import { useEffect, useState } from "react";
import api from "../api/axiosClient";
import Swal from "sweetalert2";

export default function AdminDashboard() {
  const [pending, setPending] = useState([]);

  const fetchPending = async () => {
    try {
      const res = await api.get("/admin/pending");
      setPending(res.data.filter((u) => !u.is_active));
    } catch (err) {
      console.error("Failed to fetch pending users:", err);
      Swal.fire("Error", "Failed to fetch pending accounts", "error");
    }
  };

  const approve = async (id) => {
    try {
      await api.post(`/admin/approve/${id}`);
      Swal.fire("Approved!", "", "success");
      fetchPending();
    } catch (err) {
      console.error(err);
      Swal.fire("Error", "Failed to approve user", "error");
    }
  };

  const reject = async (id) => {
    try {
      await api.post(`/admin/reject/${id}`);
      Swal.fire("Rejected!", "", "error");
      fetchPending();
    } catch (err) {
      console.error(err);
      Swal.fire("Error", "Failed to reject user", "error");
    }
  };

  const logout = () => {
    localStorage.removeItem("user_id");
    localStorage.removeItem("is_admin");
    Swal.fire("Logged out!", "", "info");
    window.location.href = "/";
  };

  useEffect(() => {
    fetchPending();
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 via-purple-100 to-pink-100 p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-purple-700">Admin Dashboard</h1>
        <button
          onClick={logout}
          className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 transition-colors"
        >
          Logout
        </button>
      </div>

      <h2 className="text-2xl mb-4 text-purple-600">Pending Puller Accounts</h2>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
        {pending.length === 0 && (
          <p className="text-gray-600 col-span-full">No pending accounts</p>
        )}

        {pending.map((u) => (
          <div
            key={u.id}
            className="p-4 bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300"
          >
            <h3 className="font-semibold text-lg text-blue-700 mb-1">
              {u.name || "No Name"}
            </h3>
            <p className="text-gray-700 mb-3">{u.phone}</p>
            <div className="flex gap-2">
              <button
                onClick={() => approve(u.id)}
                className="flex-1 bg-green-500 text-white py-2 rounded hover:bg-green-600 transition-colors"
              >
                Approve
              </button>
              <button
                onClick={() => reject(u.id)}
                className="flex-1 bg-red-500 text-white py-2 rounded hover:bg-red-600 transition-colors"
              >
                Reject
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
