import React from 'react';

interface Props {
  color: string;
  location: object;
}

const squares = {
  mobile: {
    1: { top: '35%' },
    2: { top: '20%' }
  },
  watch: {
    1: { top: '30%' },
    2: { top: '13%' }
  }
};

const Indicator: React.FC<Props> = props => {
  const color = props.color || 'red';
  const { name = 'mobile' } = { ...props.location };
  if (name === 'mobile') {
    if (props.location['mobile']) {
      const index = props.location['mobile'][3] * 1;
      const { top = '38%' } = squares['mobile'][index];
      return (
        <div
          style={{ backgroundColor: color, boxShadow: `0 0 1rem ${color}`, top: top }}
          className="indicator"
        ></div>
      );
    }
  } else if (name === 'watch') {
    if (props.location['watch']) {
      const index = props.location['watch'][3] * 1;
      const { top = '38%' } = squares['watch'][index];
      return (
        <div
          style={{ backgroundColor: color, boxShadow: `0 0 1rem ${color}`, top: top }}
          className="indicator"
        ></div>
      );
    }
  }
  return null;
};

export default Indicator;
