import React, { useState, useEffect } from 'react';
import Dashboard from './components/Dashboard';
import { fetchPortfolio } from './services/api';

function App() {
    const [portfolio, setPortfolio] = useState([]);

    useEffect(() => {
        const loadPortfolio = async () => {
            const data = await fetchPortfolio(1); // Replace with dynamic user ID
            setPortfolio(data);
        };
        loadPortfolio();
    }, []);

    return (
        <div className="App">
            <h1>My Portfolio</h1>
            <Dashboard portfolio={portfolio} />
        </div>
    );
}

export default App;