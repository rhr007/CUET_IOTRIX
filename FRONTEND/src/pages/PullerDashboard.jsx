import { useEffect, useState } from "react";
import api from "../api/axiosClient";
import Swal from "sweetalert2";

export default function PullerDashboard() {
  const pullerId = localStorage.getItem("user_id");
  const pullerName = localStorage.getItem("user_name");
  const [points, setPoints] = useState(0);

  const [pending, setPending] = useState([]);
  const [accepted, setAccepted] = useState([]);
  const [completed, setCompleted] = useState([]);

  const fetchAll = async () => {
    const p = await api.get("/puller/requests");
    setPending(p.data);

    const a = await api.get("/puller/accepted", {
      params: { puller_id: pullerId },
    });
    setAccepted(a.data);

    const c = await api.get("/puller/completed", {
      params: { puller_id: pullerId },
    });
    setCompleted(c.data);

    const p_res = await api.get("/puller/points", {
      params: { puller_id: pullerId },
    });
    setPoints(p_res.data);
  };

  const accept = async (reqId) => {
    const res = await api.post("/puller/accept", null, {
      params: { puller_id: pullerId, request_id: reqId },
    });

    Swal.fire(res.data.message, "", "success");
    fetchAll();
  };
  const reject = async (reqId) => {
    const res = await api.post("/puller/reject", null, {
      params: { request_id: reqId },
    });

    Swal.fire(res.data.message, "", "error");
    fetchAll();
  };

  const completeRide = async (reqId) => {
    const res = await api.post("/puller/complete", null, {
      params: { puller_id: pullerId, request_id: reqId },
    });

    Swal.fire(
      `Ride Completed! Earned ${res.data.earned_points} points`,
      "",
      "success"
    );

    setPoints(res.data.total_points);
    fetchAll();
  };

  const logout = () => {
    localStorage.clear();
    window.location.href = "/";
  };

  useEffect(() => {
    fetchAll();
    const interval = setInterval(fetchAll, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-100 to-blue-100 p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-green-700">
          Welcome, {pullerName}
        </h1>

        <button
          onClick={logout}
          className="bg-red-500 text-white px-4 py-2 rounded shadow hover:bg-red-600"
        >
          Logout
        </button>
      </div>

      <div className="mb-6 p-4 bg-white rounded-lg shadow border">
        <h2 className="text-xl font-bold text-green-600">
          Your Points: {points}
        </h2>
      </div>

      {/* Pending */}
      <section className="mb-8">
        <h2 className="text-2xl font-bold text-gray-700 mb-3">
          Pending Requests
        </h2>

        {pending.length === 0 ? (
          <div className="p-4 bg-white rounded-lg shadow border text-center text-gray-500">
            No pending requests at the moment
          </div>
        ) : (
          pending.map((r) => (
            <div
              key={r.id}
              className="p-4 bg-white rounded-lg shadow mb-3 border flex justify-between items-center"
            >
              <div>
                <p>
                  <b>From:</b> CUET Campus
                </p>
                <p>
                  <b>Destination:</b> {r.destination}
                </p>
                <p>
                  <b>Time:</b> {new Date(r.request_time).toLocaleString()}
                </p>
              </div>

              <div className="flex gap-3">
                <button
                  onClick={() => accept(r.id)}
                  className="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600 cursor-pointer"
                >
                  Accept
                </button>

                <button
                  onClick={() => reject(r.id)}
                  className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 cursor-pointer"
                >
                  Reject
                </button>
              </div>
            </div>
          ))
        )}
      </section>

      {/* Accepted */}
      <section className="mb-8">
        <h2 className="text-2xl font-bold text-blue-700 mb-3">
          Accepted Requests
        </h2>

        {accepted.map((r) => (
          <div
            key={r.id}
            className="p-4 bg-white rounded-lg shadow mb-3 border flex justify-between items-center"
          >
            <div>
              <p>
                <b>Destination:</b> {r.destination}
              </p>
              <p>
                <b>Status:</b> {r.status}
              </p>
            </div>

            <button
              onClick={() => completeRide(r.id)}
              className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
            >
              Completed?
            </button>
          </div>
        ))}
      </section>

      {/* Completed */}
      <section>
        <h2 className="text-2xl font-bold text-purple-700 mb-3">
          Completed Rides
        </h2>

        {completed.map((r) => (
          <div
            key={r.id}
            className="p-4 bg-white rounded-lg shadow mb-3 border"
          >
            <p>
              <b>Destination:</b> {r.destination}
            </p>
            <p>
              <b>Status:</b> Completed
            </p>
          </div>
        ))}
      </section>
    </div>
  );
}
