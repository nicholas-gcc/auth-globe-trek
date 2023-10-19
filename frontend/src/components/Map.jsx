import React, { useEffect } from "react";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet.heat";
import { addressPoints } from "../utils/addressPoints";

export default function Map() {
  useEffect(() => {
    var map = L.map("map").setView([0, 0], 2);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    const points = addressPoints
      ? addressPoints.map((p) => {
          return [parseFloat(p[0]), parseFloat(p[1]), 500];
        })
      : [];

    L.heatLayer(points).addTo(map);

    // Cleanup function to remove the map when the component is unmounted
    return () => {
      map.remove();
    };
  }, []);

  return <div id="map" style={{ height: "70vh" }}></div>;
}

