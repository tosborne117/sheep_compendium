from fastapi.testclient import TestClient
from main import app
from models.models import Sheep

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    new_sheep = {
        "id": 7,
        "name": "Summer",
        "breed": "Babydoll",
        "sex": "ewe"
    }

    response = client.post("/sheep", json=new_sheep)

    assert response.status_code == 201

    assert response.json() == {
        "id": 7,
        "name": "Summer",
        "breed": "Babydoll",
        "sex": "ewe"
    }

    assert client.get("/sheep/7").json() == new_sheep

def test_update_sheep():
    change_sheep = {
        "id": 2,
        "name": "Summer",
        "breed": "Babydoll",
        "sex": "ewe"
    }

    response = client.post("/sheep/2", json=change_sheep)

    assert response.status_code == 201

    assert response.json() == {
        "id": 2,
        "name": "Summer",
        "breed": "Babydoll",
        "sex": "ewe"
    }



