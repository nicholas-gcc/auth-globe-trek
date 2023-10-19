import React from 'react';
import NavBar from './components/NavBar';
import Map from './components/Map';
import CityStatistics from './components/CityStatistics';
import { ChakraProvider, CSSReset } from '@chakra-ui/react';

function App() {
  return (
    <ChakraProvider>
      <CSSReset />
      <NavBar />
      <Map />
      <CityStatistics />
    </ChakraProvider>
  );
}

export default App;
