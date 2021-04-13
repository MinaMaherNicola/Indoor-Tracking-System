import React from 'react';

const squares = [
  { square: 's-01', top: '365px', left: '415px' },
  { square: 's-02', top: '275px', left: '415px' },
  { square: 's-03', top: '365px', left: '565px' },
  { square: 's-04', top: '365px', left: '565px' }
];

const squaresLaptop = [
  { square: 's-01', top: '365px', left: '325px' },
  { square: 's-02', top: '275px', left: '325px' },
  { square: 's-03', top: '365px', left: '470px' },
  { square: 's-04', top: '365px', left: '565px' }
];

const Indicator = ({ name }) => {
  console.log(squaresLaptop[parseInt(name[name.length - 1]) - 1]);
  const position = squaresLaptop[parseInt(name[name.length - 1]) - 1];
  return (
    <div
      style={{ position: 'absolute', top: position.top, left: position.left }}
      className="indicator"
    >
      &nbsp;
    </div>
  );
};

export default Indicator;
