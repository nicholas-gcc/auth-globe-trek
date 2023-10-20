import React, { useEffect, useState } from 'react';
import { Box, Text, VStack, Heading, List, ListItem } from '@chakra-ui/react';
import { getCityStatistics } from '../services/api';

const CityStatistics = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      const result = await getCityStatistics();
      setData(result);
      setLoading(false);
    };

    fetchData();
  }, []);

  if (loading) {
    return <Text>Statistics are loading...</Text>;
  }

  if (!data || !data.geolocations) {
    return <Text>Failed to load statistics</Text>;
  }

  const geolocations = data.geolocations;
  const totalLogins = Object.values(geolocations).reduce((a, b) => a + b, 0);

  const sortedCities = Object.entries(geolocations)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10);

  const top10TotalLogins = sortedCities.reduce((acc, city) => acc + city[1], 0);

  return (
    <Box p={5} bg="white" boxShadow="0 4px 8px rgba(0,0,0,0.1)" borderRadius="md">
      <VStack spacing={3}>
        <Heading size="md">Top 10 Cities by User Logins</Heading>
        <List spacing={2}>
          {sortedCities.map(([city, count], index) => (
            <ListItem key={city}>
              <Text fontSize="lg">
                {index + 1}. {city} - {((count / totalLogins) * 100).toFixed(2)}% of all logins
              </Text>
            </ListItem>
          ))}
        </List>
      </VStack>
    </Box>
  );
};

export default CityStatistics;
