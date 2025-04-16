// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import TutorPage from './pages/TutorPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<TutorPage />} />
      </Routes>
    </Router>
  );
};

export default App;
