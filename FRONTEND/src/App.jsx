import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import AdminDashboard from "./pages/AdminDashboard";
import PullerDashboard from "./pages/PullerDashboard";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />

        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/puller" element={<PullerDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
