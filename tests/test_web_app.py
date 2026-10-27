import pytest

from web_app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)

    return app.test_client()


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Electricity Bill Calculator" in response.data


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_calculate_bill(client):
    response = client.post(
        "/calculate",
        data={"units": "150", "price": "0.30"},
    )

    assert response.status_code == 200
    assert "45.00" in response.get_data(as_text=True)


@pytest.mark.parametrize(
    "data",
    [
        {"units": "-150", "price": "0.30"},
        {"units": "150", "price": "-0.30"},
        {"units": "hello", "price": "0.30"},
        {"units": "", "price": "0.30"},
        {},
    ],
)
def test_invalid_input(client, data):
    response = client.post("/calculate", data=data)

    assert response.status_code == 400