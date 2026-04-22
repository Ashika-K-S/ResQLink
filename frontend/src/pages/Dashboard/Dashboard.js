import React, { useContext } from 'react';
import { AuthContext } from "../../context/AuthContext";
import "./Dashboard.css";

const Dashboard = () => {
  const { logout, user } = useContext(AuthContext);

  const getRoleBadge = (role) => {
    const roles = {
      citizen: { label: 'Citizen', class: 'badge-citizen' },
      volunteer: { label: 'Volunteer', class: 'badge-volunteer' },
      authority: { label: 'Authority', class: 'badge-authority' }
    };
    const r = roles[role] || { label: role, class: 'badge-default' };
    return <span className={`role-badge ${r.class}`}>{r.label}</span>;
  };

  return (
    <div className="dashboard-wrapper">
      <header className="dashboard-navbar">
        <div className="navbar-logo">
          <span className="logo-text">ResQLink</span>
        </div>
        <div className="navbar-actions">
          <div className="user-info">
            {getRoleBadge(user?.role)}
            <span className="user-email">Logged in as {user?.email || 'User'}</span>
          </div>
          <button className="logout-btn" onClick={logout}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg>
            Sign Out
          </button>
        </div>
      </header>

      <main className="dashboard-content">
        <div className="hero-section">
          <h1>Welcome back, {user?.role}!</h1>
          <p>Your centralized emergency response and coordination dashboard.</p>
        </div>

        <div className="dashboard-grid">
          <div className="dashboard-card">
            <h3>Recent Alerts</h3>
            <p>No active emergencies in your immediate area.</p>
          </div>

            {user?.role === "citizen" && (
            <div className="dashboard-card primary">
              <h3>Report Emergency</h3>
              <p>Quickly alert authorities and volunteers about an incident.</p>
              <button className="action-link">Start Report</button>
            </div>
          )}

          {user?.role === "volunteer" && (
            <div className="dashboard-card secondary">
              <h3>Active Missions</h3>
              <p>Check for open assistance requests near you.</p>
              <button className="action-link">View Requests</button>
            </div>
          )}

          {user?.role === "authority" && (
            <div className="dashboard-card authority">
              <h3>System Oversight</h3>
              <p>Monitor responder deployments and infrastructure status.</p>
              <button className="action-link">Open Control Panel</button>
            </div>
          )}
        </div>
      </main>
    </div>
  );
};

export default Dashboard;