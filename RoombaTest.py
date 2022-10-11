import requests
import pytest
import allure

def test_happy_path():
    data = { "roomSize" : [5, 5], 
    "coords" : [1, 2], 
    "patches" : [ [1, 0], [2, 2], [2, 3] ], 
    "instructions" : "NNESEESWNWW"}
    flag = True

    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    data = resp.json()

    print(data.coords)
    print(data.patches)
    if resp.status_code != 200:
        flag = False

    if data.coords != [1,3]:
        flag = False
       
    if data.patches != 1:
        flag = False


    if flag:
        assert True
    else:
        assert False
    
#test_happy_path()