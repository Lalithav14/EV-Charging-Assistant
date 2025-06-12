import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [health, setHealth] = useState("Loading...");
  const [statusColor, setStatusColor] = useState("gray");

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://localhost:5000/api/health")
        .then(res => res.json())
        .then(data => {
          setHealth(data.status);
          setStatusColor(data.status === "GOOD" ? "green" : "red");
        });
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="dashboard">
      <h1>⚡ EV Charging Assistant</h1>
      <div className="health-card" style={{ backgroundColor: statusColor }}>
        <h2>Vehicle Health</h2>
        <p>{health}</p>
      </div>
    </div>
  );
}

export default App;
