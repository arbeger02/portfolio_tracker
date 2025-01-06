import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/api';

export const fetchPortfolio = async (userId) => {
    const response = await axios.get(`${API_BASE_URL}/portfolio?user_id=${userId}`);
    return response.data[0]; // Assuming the first portfolio is returned
};

export const addAsset = async (portfolioId, symbol, quantity, purchasePrice) => {
    await axios.post(`${API_BASE_URL}/portfolio/add`, {
        portfolio_id: portfolioId,
        symbol,
        quantity,
        purchase_price: purchasePrice,
    });
};

export const fetchRealTimePrices = async (symbols) => {
    // Use Alpha Vantage or CoinGecko API to fetch real-time prices
    const prices = {};
    for (const symbol of symbols) {
        const response = await axios.get(`https://api.coingecko.com/api/v3/simple/price?ids=${symbol}&vs_currencies=usd`);
        prices[symbol] = response.data[symbol].usd;
    }
    return prices;
};