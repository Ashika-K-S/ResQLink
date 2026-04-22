import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import API from "../../api/axios";
import { AuthContext } from "../../context/AuthContext";
import "./SelectRole.css";

const SelectRole = () => {
  const [role, setRole] = useState("citizen");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const { login } = useContext(AuthContext);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      await API.post("users/set-role/", { role });
      localStorage.setItem("role", role);

    
      login(role);

      navigate("/dashboard");
    } catch (err) {
      setError("Failed to set role. Please try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="select-role-container">
      <div className="select-role-card">
        <div className="select-role-header">
          <h2>Complete Your Profile</h2>
          <p>Welcome! Please select your role to help us customize your experience.</p>
        </div>

        {error && <div className="error-message">{error}</div>}

        <form onSubmit={handleSubmit} className="select-role-form">
          <div className="role-options">
            <label className={`role-option-card ${role === "citizen" ? "active" : ""}`}>
              <input
                type="radio"
                name="role"
                value="citizen"
                checked={role === "citizen"}
                onChange={(e) => setRole(e.target.value)}
              />
              <div className="role-icon">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12 12C14.2091 12 16 10.2091 16 8C16 5.79086 14.2091 4 12 4C9.79086 4 8 5.79086 8 8C8 10.2091 9.79086 12 12 12Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                  <path d="M6 20V18C6 15.7909 7.79086 14 10 14H14C16.2091 14 18 15.7909 18 18V20" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </div>
              <div className="role-text">
                <h3>Citizen</h3>
                <p>Report emergencies and stay informed about local incidents.</p>
              </div>
            </label>

            <label className={`role-option-card ${role === "volunteer" ? "active" : ""}`}>
              <input
                type="radio"
                name="role"
                value="volunteer"
                checked={role === "volunteer"}
                onChange={(e) => setRole(e.target.value)}
              />
              <div className="role-icon">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M16 21V19C16 17.9391 15.5786 16.9217 14.8284 16.1716C14.0783 15.4214 13.0609 15 12 15H5C3.93913 15 2.92172 15.4214 2.17157 16.1716C1.42143 16.9217 1 17.9391 1 19V21" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                  <path d="M8.5 11C10.7091 11 12.5 9.20914 12.5 7C12.5 4.79086 10.7091 3 8.5 3C6.29086 3 4.5 4.79086 4.5 7C4.5 9.20914 6.29086 11 8.5 11Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                  <path d="M17 11L19 13L23 9" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </div>
              <div className="role-text">
                <h3>Volunteer</h3>
                <p>Provide assistance and support during emergency situations.</p>
              </div>
            </label>
          </div>

          <button type="submit" className="complete-btn" disabled={loading}>
            {loading ? (
              <span className="loader-text">Updating...</span>
            ) : (
              "Complete Account Setup"
            )}
          </button>
        </form>
      </div>
    </div>
  );
};

export default SelectRole;