import React from 'react';
import Button from './Button';

interface Props {
  header: string;
  apiFunction: Function;
}

const Controller: React.FC<Props> = props => {
  return (
    <div>
      <h2>{props.header}</h2>
      <div>
        <Button functionality={props.apiFunction} name="S-01" />
        <Button functionality={props.apiFunction} name="S-02" />
      </div>
    </div>
  );
};

export default Controller;
