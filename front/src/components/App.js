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
  [-56, -32, -19, -24, -47, -60, -72, -48]
];

let currentSquare = 0;

const App = () => {
  const [square, setSquare] = useState('s-01');

  const getSquare = async () => {
    const squareDate = await axios({
      method: 'POST',
      url: url,
      data: data[currentSquare]
    });

    if (square !== squareDate.data.res.name) {
      setSquare(squareDate.data.res.name);
    }
  };

  useEffect(() => {
    const intervalID = setInterval(() => {
      currentSquare = (currentSquare + 1) % 3;
      getSquare();
    }, 6000);

    console.log(`Inside useEffect: Square:${square}`);

    return () => {
      clearInterval(intervalID);
    };
  });

  return (
    <div className="holder">
      <Navbar />
      <Indicator name={square} />
      <Map />
    </div>
  );
};

export default App;
