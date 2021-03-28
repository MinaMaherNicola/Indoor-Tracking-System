import React from 'react';

const squares = [
  { square: 's-01', top: '365px', left: '415px' },
  { square: 's-02', top: '275px', left: '415px' },
  { square: 's-03', top: '365px', left: '565px' },
  { square: 's-04', top: '365px', left: '565px' }
];

const Indicator = ({ name }) => {
  const position = squares[parseInt(name[-1]) - 1] || squares[0];
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
