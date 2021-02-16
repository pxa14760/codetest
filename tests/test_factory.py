from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_smv(client):
    response = client.get('/smv')
    assert response.status_code == 200

def test_smovingAverage(client):
    response = client.get('/movingAverage')
    assert response.status_code == 200