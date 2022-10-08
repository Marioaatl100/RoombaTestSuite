import requests

def test_happy_path():
    data = { "roomSize" : [5, 5], 
    "coords" : [1, 2], 
    "patches" : [ [1, 0], [2, 2], [2, 3] ], 
    "instructions" : "NNESEESWNWW"}

    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    data = resp.json()
    assert (resp.status_code == 200), "Status code is not 200. Rather found : "\
        + str(resp.status_code)

    
#test_happy_path()