import requests
import pytest
import allure

#Test verifying expected results from bitbucket instructions
def test_happy_path():
    data = { "roomSize" : [5, 5], 
    "coords" : [1, 2], 
    "patches" : [ [1, 0], [2, 2], [2, 3] ], 
    "instructions" : "NNESEESWNWW"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    data = resp.json()

    #Validations from happy path response
    if resp.status_code != 200:
        flag = False

    if data['coords'] != [1,3]:
        flag = False
       
    if data['patches'] != 1:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False

#Test verifying the coords output functionality
def test_coords_output():
    data = { "roomSize" : [5, 5], 
    "coords" : [0, 0], 
    "patches" : [ [1, 0], [2, 2], [2, 3] ], 
    "instructions" : "NNEE"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    data = resp.json()

    #Validations from payload
    if resp.status_code != 200:
        flag = False

    if data['coords'] != [2,2]:
        flag = False
       
    if data['patches'] != 1:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False

#Test verifying it remains inside the roomsize
def test_limit_size_movement():
    data = { "roomSize" : [5, 5], 
    "coords" : [0, 0], 
    "patches" : [ [1, 0], [2, 2], [2, 3] ], 
    "instructions" : "NNNNNNNN"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    data = resp.json()

    #Validations from payload
    if resp.status_code != 200:
        flag = False

    if data['coords'] != [0,4]:
        flag = False
       
    if data['patches'] != 0:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False

#Test verifying [0,0] roomsize, I expected some kind of error response
def test_invalid_roomsize():
    data = { "roomSize" : [0, 0], 
    "coords" : [0, 0], 
    "patches" : [ [1, 0], [2, 2], [2, 3] ], 
    "instructions" : "NNNNNNNN"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    print(resp)
    #Validations from payload
    if resp.status_code != 200:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False
 
#Test veryfing patches are cleaned correctly
def test_cleaning_feature():
    data = { "roomSize" : [5, 5], 
    "coords" : [0, 0], 
    "patches" : [ [1, 0], [2, 2], [2, 3] ], 
    "instructions" : "EEEWWW"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    data = resp.json()

    #Validations from payload
    if resp.status_code != 200:
        flag = False

    if data['coords'] != [0,0]:
        flag = False
       
    if data['patches'] != 1:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False
    
#test_happy_path()