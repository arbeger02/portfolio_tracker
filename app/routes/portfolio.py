from flask import Blueprint, request, jsonify
from ..models import Portfolio, Asset, db

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400

    portfolios = Portfolio.query.filter_by(user_id=user_id).all()
    portfolio_data = []

    for portfolio in portfolios:
        assets = Asset.query.filter_by(portfolio_id=portfolio.id).all()
        asset_data = [{'symbol': asset.symbol, 'quantity': asset.quantity, 'purchase_price': asset.purchase_price} for asset in assets]
        portfolio_data.append({'id': portfolio.id, 'name': portfolio.name, 'assets': asset_data})

    return jsonify(portfolio_data), 200

@portfolio_bp.route('/api/portfolio/add', methods=['POST'])
def add_asset():
    data = request.get_json()
    portfolio_id = data.get('portfolio_id')
    symbol = data.get('symbol')
    quantity = data.get('quantity')
    purchase_price = data.get('purchase_price')

    if not portfolio_id or not symbol or not quantity or not purchase_price:
        return jsonify({'message': 'Missing fields'}), 400

    new_asset = Asset(symbol=symbol, quantity=quantity, purchase_price=purchase_price, portfolio_id=portfolio_id)
    db.session.add(new_asset)
    db.session.commit()

    return jsonify({'message': 'Asset added successfully'}), 201

@portfolio_bp.route('/api/portfolio/remove', methods=['DELETE'])
def remove_asset():
    asset_id = request.args.get('asset_id')
    if not asset_id:
        return jsonify({'message': 'Asset ID is required'}), 400

    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({'message': 'Asset not found'}), 404

    db.session.delete(asset)
    db.session.commit()

    return jsonify({'message': 'Asset removed successfully'}), 200