import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import ShoeList from './ShoeList';
import ShoeForm from './ShoeForm';

import HatList from './hats_list';
import HatForm from './hats_form';


function App(props) {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/shoes" element={<ShoeList shoes={props.shoes} />} />
          <Route path="/shoes/new" element={<ShoeForm/>} />
          <Route path="hats" element={<HatList hats={props.hats} />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
