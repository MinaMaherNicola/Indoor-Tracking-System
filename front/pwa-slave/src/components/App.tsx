import React, { useEffect, useState } from 'react';
import Map from './Map';
import api from './../api/api';
import imgPath from './../img/map.jpeg';

const App: React.FC = () => {
  const [locations, setLocations] = useState({});

  useEffect(() => {
    const getData = async () => {
      const { data } = await api.get('/mobile');
      console.log(data);
      setLocations(() => data);
    };
    const id = setInterval(() => {
      getData();
    }, 5000);

    return () => {
      clearInterval(id);
    };
  }, [locations]);

  return (
    <div className="app-container">{imgPath && <Map locations={locations} mapImg={imgPath} />}</div>
  );
};

export default App;
