from app import app
import json

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert json.loads(response.data) == {'message': 'Welcome to my API'}

def test_add():
    tester = app.test_client()
    response = tester.post('/add', json={'a': 10, 'b': 15})
    assert response.status_code == 200
    assert json.loads(response.data) == {'result': 25}

def test_subtract():
    tester = app.test_client()
    response = tester.post('/subtract', json={'a': 20, 'b': 5})
    assert response.status_code == 200
    assert json.loads(response.data) == {'result': 15}
