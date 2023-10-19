import React from 'react';
import { Box, Text, VStack, Heading, List, ListItem } from '@chakra-ui/react';

const data = {
	"geolocations": {
		"Washington, Washington, D.C.": 1,
		"Al Aḩmadī, Al Aḩmadī": 4,
		"Chengdu, Sichuan": 1,
		"Bayamón, Bayamón": 5,
		"Sierra Vista, Arizona": 7,
		"Ashburn, Virginia": 8,
		"Palo Alto, California": 3,
		"Englewood, Colorado": 9,
		"Quebrada, Camuy": 4,
		"Mezzouna, Sidi Bouzid Governorate": 1,
		"Columbus, Ohio": 2,
		"Tehran, Tehran": 1,
		"Jakarta, Jakarta": 8,
		"Miami, Florida": 1,
		"Montgomery, Alabama": 1,
		"Warrensburg, Missouri": 1,
		"Indianapolis, Indiana": 1,
		"Turin, Piedmont": 1,
		"Chicago, Illinois": 2,
		"Melbourne, Victoria": 2,
		"Mount Laurel, New Jersey": 6,
		"Seoul, Seoul": 1,
		"Towson, Maryland": 1,
		"As Sulaymānīyah, Sulaymaniyah": 1,
		"Cheongju-si, North Chungcheong": 1,
		"London, England": 1,
		"Munich, Bavaria": 1,
		"Seattle, Washington": 1,
		"Dearborn, Michigan": 1,
		"Kolkata, West Bengal": 1,
		"Rivas-Vaciamadrid, Madrid": 1,
		"Beijing, Beijing": 2,
		"Grenoble, Auvergne-Rhône-Alpes": 1,
		"Svinninge, Zealand": 1,
		"Buenos Aires, Buenos Aires F.D.": 1,
		"Fengshan, Takao": 1,
		"Lutherville, Maryland": 1,
		"Rodeio, Santa Catarina": 1,
		"Sydney, New South Wales": 1,
		"Shanghai, Shanghai": 1,
		"Stuttgart, Baden-Wurttemberg": 1,
		"Leova, Leova": 1,
		"Dayton, Ohio": 1,
		"Cockeysville, Maryland": 1,
		"Mays Chapel, Maryland": 1,
		"Omaha, Nebraska": 1,
		"Stockholm, Stockholm": 1,
		"Edmonton, Alberta": 1,
		"Georgetown, Maryland": 1,
		"Reinach, Aargau": 1
	}
};

const CityStatistics = () => {
  const sortedCities = Object.entries(data.geolocations)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10);

  return (
    <Box p={5} bg="white" boxShadow="0 4px 8px rgba(0,0,0,0.1)" borderRadius="md">
      <VStack spacing={3}>
        <Heading size="md">Top 10 Cities by User Logins</Heading>
        <List spacing={2}>
          {sortedCities.map(([city, count], index) => (
            <ListItem key={city}>
              <Text fontSize="lg">{index + 1}. {city} - {count} logins</Text>
            </ListItem>
          ))}
        </List>
      </VStack>
    </Box>
  );
};

export default CityStatistics;
