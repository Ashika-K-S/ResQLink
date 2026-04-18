import React from 'react';

const Dashboard = () => {
    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', backgroundColor: '#f3f4f6' }}>
            <div style={{ background: 'white', padding: '3rem', borderRadius: '1rem', boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)', textAlign: 'center' }}>
                <h1 style={{ color: '#4f46e5', marginBottom: '1rem' }}>Welcome to Dashboard!</h1>
                <p style={{ color: '#6b7280', fontSize: '1.2rem' }}>You have successfully logged in.</p>
            </div>
        </div>
    );
};

export default Dashboard;
