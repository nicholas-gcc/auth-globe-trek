import axios from 'axios';

const baseURL = "http://127.0.0.1:8000/api/v1";

const api = axios.create({
  baseURL,
});

export const getCityStatistics = async () => {
  try {
    const response = await api.get("/geolocation/user-ips/?format=city");
    return response.data;
  } catch (error) {
    console.error('There was an error fetching the city statistics', error);
  }
};

export const getCoordinates = async () => {
  try {
    const response = await api.get("/geolocation/user-ips/?format=coords");
    return response.data.coordinates;
  } catch (error) {
    console.error("Failed to fetch coordinates:", error);
    throw error;
  }
};
