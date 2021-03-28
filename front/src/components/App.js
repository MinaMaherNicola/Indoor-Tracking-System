import React, { useEffect, useState } from 'react';
import Navbar from './Navbar';
import Indicator from './Indicator';
import Map from './Map';
import axios from 'axios';

const url = 'http://127.0.0.1:5000/prototype';
const data = [-30, -17, -42, -40, -58, -56, -36, -52];

const App = () => {
  const [square, setSquare] = useState(null);

  useEffect(() => {
    const getSquare = async () => {
      const sq = await axios({
        method: 'POST',
        url: url,
        data: data
      });
      setSquare(sq.data.res);
    };
    getSquare();
    console.log(square);
  }, []);
  console.log(square);
  return (
    <div>
      <Navbar />
      {/* <Indicator /> */}
      <Map />
    </div>
  );
};

export default App;
