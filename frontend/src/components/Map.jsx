// Map.jsx
import React, { useEffect, useState } from "react";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet.heat";
import { getCoordinates } from "../services/api";

export default function Map({ searchQuery }) {
  const [addressPoints, setAddressPoints] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Call the API to get coordinates
    getCoordinates()
      .then((data) => {
        setAddressPoints(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Failed to fetch coordinates:", error);
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    if (loading) {
      return;
    }

    var map = L.map("map").setView([0, 0], 2);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    const points = addressPoints
      .filter((p) => {
        if (searchQuery) {
          if (!p[2]) {
            // Exclude points that don't have metadata when there is a search query
            return false;
          }

          // Split the search query into key and value
          const [key, value] = searchQuery
            .replace(/["{}]/g, "")
            .split(":")
            .map((s) => s.trim());

          // Check if the metadata contains the key and if the value matches
          const matches = Object.entries(p[2]).some(([k, v]) => {
            return (
              k.toLowerCase() === key.toLowerCase() &&
              v.toString().toLowerCase() === value.toLowerCase()
            );
          });

          return matches;
        }
        // Include all points when there is no search query
        return true;
      })
      .map((p) => {
        return [parseFloat(p[0]), parseFloat(p[1])];
      });

    const intensity = points.length > 0 ? 50000 / points.length : 1;
    const heatPoints = points.map((p) => [...p, intensity]);

    L.heatLayer(heatPoints).addTo(map);


    // Cleanup function to remove the map when the component is unmounted
    return () => {
      map.remove();
    };
  }, [searchQuery, addressPoints, loading]);

  return (
    <div>
      {loading ? (
        <div>Loading...</div>
      ) : (
        <div id="map" style={{ height: "60vh" }}></div>
      )}
    </div>
  );
}
