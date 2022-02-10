import Welcome from './pages/Welcome';
import Result from './pages/Result';
import Header from './components/Header';
import Display from './pages/Display';
import { Routes, Route} from 'react-router-dom';

import './App.scss';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Welcome />}/>
      <Route path="/busca/:term/:court/:field" element={<Result />}/>
      <Route path="/exibir/:number" element={<Display />}/>
      <Route path="*" element={<Header />}/>
    </Routes>
   );
}

export default App;