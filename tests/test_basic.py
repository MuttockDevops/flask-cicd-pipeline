from app.main import app

def test_home_route():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"Hello" in response.data

def test_secret_route():
    with app.test_client() as client:
        response = client.get("/secret")
        assert response.status_code == 200
        assert b"Secret is" in response.data
