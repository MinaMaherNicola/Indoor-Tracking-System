import React from 'react';

interface Props {
  name: string;
  functionality: Function;
}

const Button: React.FC<Props> = props => {
  return (
    <button style={{ marginRight: '15px' }} onClick={() => props.functionality(props.name)}>
      {props.name}
    </button>
  );
};

export default Button;
