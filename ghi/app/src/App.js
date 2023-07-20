import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatList from './hats_list'


function App(props) {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="hats" element={<HatList hats={props.hats} />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
