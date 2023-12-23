# Assertion - assert
# PyTest
import pytest
import requests


def test_sample():
    assert 4 == 4


def test_sample2():
    assert 5 == 5


def test_generate_get_request():
    id = '1'
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    print(full_url)
    response_body = requests.get(full_url)
    print(response_body.status_code)
    assert response_body.status_code == 200
