import React, { useState } from 'react';
import NavBar from './components/NavBar';
import Map from './components/Map';
import CityStatistics from './components/CityStatistics';
import { ChakraProvider, CSSReset } from '@chakra-ui/react';

function App() {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = (query) => {
    console.log('Search Query:', query);
    setSearchQuery(query);
  };

  return (
    <ChakraProvider>
      <CSSReset />
      <NavBar onSearch={handleSearch} />
      <Map searchQuery={searchQuery} />
      <CityStatistics />
    </ChakraProvider>
  );
}

export default App;
