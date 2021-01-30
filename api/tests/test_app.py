import json
#Added multiple tests but not sure how to run multiple tests
# Will learn more to add multiple running test with pytest

def test_client(app, client):
    del app
    res = client.get('/api/stores?offset=3')
    print('get the resonse', res)
    assert res.status_code == 200
    expected = {'offset': 3,
          'stores': [{'name': 'St_Albans', 'postcode': 'AL1 2RJ'},
                    {'name': 'Hatfield', 'postcode': 'AL9 5JP'},
                     {'name': 'Worthing', 'postcode': 'BN14 9GB'}]}
    assert expected == json.loads(res.get_data(as_text=True))

def test_client(app, client):
    del app
    res = client.get('/api/stores?offset=1')
    assert res.status_code == 200
    expected = {'offset': 1,
          'stores': [{'name': 'St_Albans', 'postcode': 'AL1 2RJ'}]}
    assert expected == json.loads(res.get_data(as_text=True))

def test_client(app, client):
    del app
    res = client.get('/api/stores?s=rm&offset=1')
    assert res.status_code == 200
    expected = {'offset': 1,
          'stores': [{'name': 'Dagenham', 'postcode': 'RM9 6SJ'}]}
    assert expected == json.loads(res.get_data(as_text=True))