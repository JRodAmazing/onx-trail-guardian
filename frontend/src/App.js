import React, { useState, useEffect } from "react";
import TrailMap from "./components/TrailMap";
import "./App.css";

function App() {
  const [trails, setTrails] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTrails();
  }, []);

  const fetchTrails = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/v1/trails/");
      const data = await response.json();
      setTrails(data);
      setLoading(false);
    } catch (error) {
      console.error("Error fetching trails:", error);
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🔥 Trail Guardian Pro</h1>
        <p>Real-time Wildfire Threat Scoring</p>
      </header>
      
      <div className="container">
        {loading ? (
          <p>Loading trails...</p>
        ) : (
          <>
            <div className="map-section">
              <TrailMap trails={trails} />
            </div>
            
            <h2 style={{ textAlign: "left", marginTop: "2rem" }}>Available Trails</h2>
            <div className="trails-grid">
              {trails.map((trail) => (
                <div key={trail.id} className="trail-card">
                  <h3>{trail.name}</h3>
                  <p>
                    <strong>Threat Level:</strong>{" "}
                    <span className="threat-score">{trail.threat_score}/100</span>
                  </p>
                  <p>{trail.description}</p>
                  <p><strong>Difficulty:</strong> {trail.difficulty}</p>
                  <p><strong>Distance:</strong> {trail.length_miles} miles</p>
                  <p><strong>Active Fires:</strong> {trail.active_fires_nearby}</p>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
