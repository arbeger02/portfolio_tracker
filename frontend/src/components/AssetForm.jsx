import React, { useState } from 'react';
import { addAsset } from '../services/api';

function AssetForm({ portfolioId }) {
    const [symbol, setSymbol] = useState('');
    const [quantity, setQuantity] = useState('');
    const [purchasePrice, setPurchasePrice] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        await addAsset(portfolioId, symbol, quantity, purchasePrice);
        alert('Asset added successfully!');
        setSymbol('');
        setQuantity('');
        setPurchasePrice('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Symbol"
                value={symbol}
                onChange={(e) => setSymbol(e.target.value)}
                required
            />
            <input
                type="number"
                placeholder="Quantity"
                value={quantity}
                onChange={(e) => setQuantity(e.target.value)}
                required
            />
            <input
                type="number"
                placeholder="Purchase Price"
                value={purchasePrice}
                onChange={(e) => setPurchasePrice(e.target.value)}
                required
            />
            <button type="submit">Add Asset</button>
        </form>
    );
}

export default AssetForm;