import React from 'react';
import mapImage from './../img/map.jpeg';

const Map = () => {
  return (
    <div className="map">
      <img className="map__img" alt="map of home" src={mapImage} />
    </div>
  );
};

export default Map;
