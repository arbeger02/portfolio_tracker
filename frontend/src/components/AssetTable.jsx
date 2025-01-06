import React from 'react';

function AssetTable({ assets }) {
    return (
        <table>
            <thead>
                <tr>
                    <th>Symbol</th>
                    <th>Quantity</th>
                    <th>Current Price</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
                {assets.map((asset, index) => (
                    <tr key={index}>
                        <td>{asset.symbol}</td>
                        <td>{asset.quantity}</td>
                        <td>{asset.current_price}</td>
                        <td>${(asset.quantity * asset.current_price).toFixed(2)}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
}

export default AssetTable;