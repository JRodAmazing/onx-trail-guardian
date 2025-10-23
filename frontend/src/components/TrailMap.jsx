import React, { useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import L from "leaflet";
import "./TrailMap.css";

delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});

function TrailMap({ trails }) {
  const getThreatColor = (threatScore) => {
    if (threatScore >= 70) return "red";
    if (threatScore >= 40) return "orange";
    return "green";
  };

  const createIcon = (threatScore) => {
    return L.divIcon({
      className: "custom-marker",
      html: `<div style="background-color: ${getThreatColor(threatScore)}; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; border: 2px solid white;">${threatScore}</div>`,
    });
  };

  return (
    <MapContainer center={[37.0902, -95.7129]} zoom={4} style={{ width: "100%", height: "600px" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {trails.map((trail) => (
        <Marker key={trail.id} position={[trail.latitude, trail.longitude]} icon={createIcon(trail.threat_score)}>
          <Popup>
            <div className="popup-content">
              <h3>{trail.name}</h3>
              <p>{trail.description}</p>
              <p><strong>Difficulty:</strong> {trail.difficulty}</p>
              <p><strong>Distance:</strong> {trail.length_miles} miles</p>
              <p><strong>Threat Score:</strong> <span className="threat-badge">{trail.threat_score}/100</span></p>
              <p><strong>Active Fires:</strong> {trail.active_fires_nearby}</p>
            </div>
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}

export default TrailMap;
