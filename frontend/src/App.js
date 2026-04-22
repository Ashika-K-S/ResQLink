import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

import Login from './pages/Auth/Login';
import Signup from './pages/Auth/Signup';
import Dashboard from './pages/Dashboard/Dashboard';

import ProtectedRoute from './components/ProtectedRoute';
import SelectRole from "./pages/Auth/SelectRole";
import './App.css';

import SocialLoginSuccess from './pages/Auth/SocialLoginSuccess';
import ForgotPassword from './pages/Auth/ForgotPassword';
import ResetPassword from './pages/Auth/ResetPassword';


function App() {
  return (
    <Router>
      <div className="App">
        <Routes>

         
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />

  
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute allowedRoles={["citizen", "volunteer", "authority"]}>
                <Dashboard />
              </ProtectedRoute>
            }
          />

          
          <Route path="/" element={<Navigate to="/login" replace />} />
          <Route path="/social-login-success" element={<SocialLoginSuccess />} />

          <Route path="/select-role" element={<SelectRole />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/reset-password/:uid/:token" element={<ResetPassword />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;