'''
File for unit testing 
'''

from app import app

def test_home():
    response = app.test_client().get("/")

    assert response.status_code == 200 ## success
    assert response.data ==b"Hello world"