import requests
import pytest
import allure

def test_happy_path():
    data = { "roomSize" : [5, 5], 
    "coords" : [1, 2], 
    "patches" : [ [1, 0], [2, 2], [2, 3] ], 
    "instructions" : "NNESEESWNWW"}

    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    data = resp.json()
    if resp.status_code == 200:
        assert True
    else:
        assert False


    
#test_happy_path()