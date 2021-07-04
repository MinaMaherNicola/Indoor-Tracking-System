import React from 'react';
import Indicator from './Indicator';

interface Props {
  mapImg: string;
  locations: object;
}

const Map: React.FC<Props> = props => {
  const { mobile = 's-01', watch = 's-01' } = { ...props.locations };
  return (
    <div className="map-container">
      <img src={props.mapImg} alt="map" />
      <Indicator location={{ mobile, name: 'mobile' }} color="blue" />
      <Indicator location={{ watch, name: 'watch' }} color="red" />
    </div>
  );
};

export default Map;
