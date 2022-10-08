import requests

print("Hola")


def test_api_post():
    data = { "roomSize" : [5, 5], "coords" : [1, 2], "patches" : [ [1, 0], [2, 2], [2, 3] ], "instructions" : "NNESEESWNWW"}
    resp = requests.post(url=" http://localhost:8080/v1/cleaning-sessions", data=data)
    data = resp.json()
    assert (resp.status_code == 200), "Status code is not 201. Rather found : "\
        + str(resp.status_code)
    assert data['name'] == "John", "User created with wrong name. \
        Expected : John, but found : " + str(data['name'])
    assert data['job'] == "QA", "User created with wrong job. \
        Expected : QA, but found : " + str(data['name'])

    print(resp.json())


test_api_post()