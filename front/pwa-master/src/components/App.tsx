import React from 'react';
import Controller from './Controller';
import api from './../api/api';

const App: React.FC = () => {
  const postToMobile = async (name: string) => {
    const response = await api.post('/mobile', { square: name });
    console.log(response.data);
  };

  const postToWatch = async (name: string) => {
    const response = await api.post('/watch', { square: name });
    console.log(response.data);
  };

  return (
    <div>
      <Controller apiFunction={postToMobile} header="Mobile" />
      <Controller apiFunction={postToWatch} header="Watch" />
    </div>
  );
};

export default App;
