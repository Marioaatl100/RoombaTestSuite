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

#Test verifying [0,0] roomsize, 400 response code, I was expecting some kind of error message too
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
    if resp.status_code != 400:
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
    
#Test verifying duplicate patches only count as 1
def test_duplicate_patch():
    data = { "roomSize" : [5, 5], 
    "coords" : [0, 0], 
    "patches" : [ [1, 0], [2, 2], [1, 0] ], 
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

#Test verifying error message when coords are out the limits of the roomsize
def test_offlimitis_coords():
    data = { "roomSize" : [5, 5], 
    "coords" : [6, 6], 
    "patches" : [ [1, 0], [2, 2], [1, 0] ], 
    "instructions" : "EEEWWW"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    data = resp.json()

    #Validations from payload
    if resp.status_code != 400:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False

#Test verifying it still works without patches
def test_no_patches():
    data = { "roomSize" : [5, 5], 
    "coords" : [0, 0], 
    "instructions" : "EEEWWW"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)   

    #Validations from payload
    if resp.status_code != 200:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False

#Test verifying error when no coordinates
def test_no_coords():
    data = { "roomSize" : [5, 5], 
    "coords" : [0, 0], 
    "instructions" : "EEEWWW"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)
    #Validations from payload
    if resp.status_code != 200:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False

#Test validating error response on invalid instructions
def test_invalid_instrucctions():
    data = { "roomSize" : [5, 5], 
    "coords" : [0, 0], 
    "instructions" : "AAAAAA"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)

    #Validations from payload
    if resp.status_code != 400:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False

#Test validating error response on invalid instructions 2
def test_invalid_instrucctions():
    data = { "roomSize" : [5, 5], 
    "coords" : [0, 0], 
    "instructions" : "nnnnn"}
    #Flag for the asserts
    flag = True
    resp = requests.post(url="http://localhost:8080/v1/cleaning-sessions", json=data)

    #Validations from payload
    if resp.status_code != 400:
        flag = False

    #Assert
    if flag:
        assert True
    else:
        assert False