import React, { useEffect, useState } from 'react';
import Navbar from './Navbar';
import Indicator from './Indicator';
import Map from './Map';
import axios from 'axios';

// const url = 'http://127.0.0.1:5000/prototype';
const url = 'https://ips-grad-project.herokuapp.com/prototype';
const data = [
  [-30, -17, -42, -40, -58, -56, -36, -52],
  [-44, -20, -36, -28, -48, -58, -42, -54],
  [-40, -20, -32, -28, -48, -58, -44, -52]
];

const App = () => {
  const [square, setSquare] = useState({ name: 's-01' });
  const [currentSquare, setCurrentSquare] = useState(0);
  console.log(data[currentSquare]);

  useEffect(() => {
    const getSquare = async () => {
      const sq = await axios({
        method: 'POST',
        url: url,
        data: data[currentSquare]
      });
      setSquare(sq.data.res);
    };
    setInterval(() => {
      setCurrentSquare((currentSquare) => (currentSquare + 1) % 3);
      console.log('Current Square:');
      console.log(currentSquare);
      getSquare();
      console.log('inside interval');
    }, 5000);
    console.log('inside useEffect');
  }, [square]);

  return (
    <div className="holder">
      <Navbar />
      <Indicator name={square.name} />
      <Map />
    </div>
  );
};

export default App;
