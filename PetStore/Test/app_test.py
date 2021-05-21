"""The tests to run in this project.
To run the tests type,
$ nosetests --verbose
"""

from nose.tools import assert_true
import requests

BASE_URL = "http://localhost:5000"


def test_get_all_requests():
    "Test getting all requests"
    response = requests.get('%s/Bids/All' % (BASE_URL))
    assert_true(response.ok)


def test_post_request():
    "Test adding posting request"
    payload = {'pet_id': 1, 'user_id': 4, 'money': 55}
    response = requests.post('%s/Bids/Insert' % (BASE_URL), json=payload)
    assert_true(response.status_code == 200)


def test_bad_post_request():
    "Test adding bad post request"
    payload = {'petID': 'doggie'}
    response = requests.post('%s/request' % (BASE_URL), json=payload)
    print(response.status_code)
    assert_true(response.status_code == 404)
