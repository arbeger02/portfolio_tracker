import React from 'react';
import AssetTable from './AssetTable';
import AssetForm from './AssetForm';

function Dashboard({ portfolio }) {
    return (
        <div>
            <h2>Portfolio: {portfolio.name}</h2>
            <AssetTable assets={portfolio.assets} />
            <AssetForm portfolioId={portfolio.id} />
        </div>
    );
}

export default Dashboard;