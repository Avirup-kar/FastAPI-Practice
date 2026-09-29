from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#Test home api
def test_home():
    response = client.get("/")
    #Status code check
    assert response.status_code == 200
    #Response data check
    assert response.json() == {"message": "Hello Mohit"}
    

#Test ADD API
def test_add():
    response = client.get("/add?a=5&b=3")    
    #Status code check
    assert response.status_code == 200
    #Response data check
    assert response.json() == {"result": 8}
    