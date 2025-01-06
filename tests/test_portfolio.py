# tests/test_portfolio.py
import pytest
from app import create_app
from app.models import User, Portfolio, Asset, db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_user(app):
    with app.app_context():
        user = User(username='testuser', email='test@example.com', password_hash='hashedpassword')
        db.session.add(user)
        db.session.commit()
        return user

@pytest.fixture
def test_portfolio(app, test_user):
    with app.app_context():
        portfolio = Portfolio(name='My Portfolio', user_id=test_user.id)
        db.session.add(portfolio)
        db.session.commit()
        return portfolio

def test_get_portfolio(client, test_user, test_portfolio):
    # Test fetching a portfolio
    response = client.get(f'/api/portfolio?user_id={test_user.id}')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'My Portfolio'

def test_add_asset(client, test_portfolio):
    # Test adding an asset to the portfolio
    response = client.post('/api/portfolio/add', json={
        'portfolio_id': test_portfolio.id,
        'symbol': 'AAPL',
        'quantity': 10,
        'purchase_price': 150
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Asset added successfully'

    # Verify the asset was added
    response = client.get(f'/api/portfolio?user_id={test_portfolio.user_id}')
    assert len(response.json[0]['assets']) == 1
    assert response.json[0]['assets'][0]['symbol'] == 'AAPL'

def test_remove_asset(client, test_portfolio):
    # Add an asset first
    client.post('/api/portfolio/add', json={
        'portfolio_id': test_portfolio.id,
        'symbol': 'AAPL',
        'quantity': 10,
        'purchase_price': 150
    })

    # Get the asset ID
    response = client.get(f'/api/portfolio?user_id={test_portfolio.user_id}')
    asset_id = response.json[0]['assets'][0]['id']

    # Test removing the asset
    response = client.delete(f'/api/portfolio/remove?asset_id={asset_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Asset removed successfully'

    # Verify the asset was removed
    response = client.get(f'/api/portfolio?user_id={test_portfolio.user_id}')
    assert len(response.json[0]['assets']) == 0