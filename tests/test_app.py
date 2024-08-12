import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Add Todo' in response.data

def test_add_todo(client):
    response = client.post('/add', data={'todo': 'Test Todo'})
    assert response.status_code == 302  # Redirects after POST
    response = client.get('/')
    assert b'Test Todo' in response.data

def test_delete_todo(client):
    # Add a todo first
    client.post('/add', data={'todo': 'Todo to Delete'})
    # Now delete the todo
    response = client.post('/delete/0')
    assert response.status_code == 302  # Redirects after POST
    response = client.get('/')
    assert b'Todo to Delete' not in response.data
