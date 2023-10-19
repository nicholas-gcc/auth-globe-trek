// Map.jsx
import React, { useEffect } from "react";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet.heat";
import { addressPoints } from "../utils/addressPoints";

export default function Map({ searchQuery }) {
  useEffect(() => {
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
          const [key, value] = searchQuery.replace(/["{}]/g, '').split(':').map(s => s.trim());

          // Check if the metadata contains the key and if the value matches
          const matches = Object.entries(p[2]).some(([k, v]) => {
            return k.toLowerCase() === key.toLowerCase() && v.toString().toLowerCase() === value.toLowerCase();
          });

          return matches;
        }
        // Include all points when there is no search query
        return true;
      })
      .map((p) => {
        return [parseFloat(p[0]), parseFloat(p[1]), 500];
      });

    L.heatLayer(points).addTo(map);

    // Cleanup function to remove the map when the component is unmounted
    return () => {
      map.remove();
    };
  }, [searchQuery]);

  return <div id="map" style={{ height: "70vh" }}></div>;
}

