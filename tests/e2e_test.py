import json
from ..app.wsgi import app

def test_list():
    response = app.test_client().get('/')
    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is dict

# TODO: Add more tests