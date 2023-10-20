import React, { useState } from 'react';
import {
  Box,
  Flex,
  Avatar,
  HStack,
  IconButton,
  Button,
  Menu,
  MenuButton,
  MenuList,
  useDisclosure,
  useColorModeValue,
  Stack,
  Input,
  InputGroup,
  InputRightElement,
  Icon,
} from '@chakra-ui/react';
import { HamburgerIcon, CloseIcon, SearchIcon } from '@chakra-ui/icons';

const NavLink = ({ children }) => {
  return (
    <Box
      as="a"
      px={2}
      py={1}
      rounded={'md'}
      _hover={{
        textDecoration: 'none',
        bg: useColorModeValue('gray.200', 'gray.700'),
      }}
      href={'#'}>
      {children}
    </Box>
  );
};

export default function NavBar({ onSearch }) {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = () => {
    onSearch(searchQuery);

  };

  return (
    <>
      <Box bg={useColorModeValue('gray.100', 'gray.900')} px={4}>
        <Flex h={16} alignItems={'center'} justifyContent={'space-between'}>
          <IconButton
            size={'md'}
            icon={isOpen ? <CloseIcon /> : <HamburgerIcon />}
            aria-label={'Open Menu'}
            display={{ md: 'none' }}
            onClick={isOpen ? onClose : onOpen}
          />
          <HStack spacing={8} alignItems={'center'}>
            <Box>Filters:</Box>
            <InputGroup>
              <Input
                placeholder='e.g. subscription: free'
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
              <InputRightElement
                children={<Icon as={SearchIcon} />}
                onClick={handleSearch}
                cursor="pointer"
              />
            </InputGroup>
            <HStack as={'nav'} spacing={4} display={{ base: 'none', md: 'flex' }}>
              
            </HStack>
          </HStack>
          <Flex alignItems={'center'}>
            <Menu>
              <MenuButton
                as={Button}
                rounded={'full'}
                variant={'link'}
                cursor={'pointer'}
                minW={0}>
                <Avatar
                  size={'sm'}
                  src={
                    'https://d112y698adiu2z.cloudfront.net/photos/production/challenge_thumbnails/001/119/326/datas/original.png'
                  }
                />
              </MenuButton>
              <MenuList>
              </MenuList>
            </Menu>
          </Flex>
        </Flex>

        {isOpen ? (
          <Box pb={4} display={{ md: 'none' }}>
            <Stack as={'nav'} spacing={4}>
              
            </Stack>
          </Box>
        ) : null}
      </Box>

      <Box bg={useColorModeValue('gray.400', 'gray.800')} p={4}>Tenant: auth-globe-trek.us.auth0.com</Box>
    </>
  );
}
