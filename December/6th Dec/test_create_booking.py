# Testing frame works --> Unit Test, PyTest, Nose
# Every test will start with test_name.py
# pytest -k -Match sustring - pytest -k "name" -> test_name.py


# How to do create booking by pytest

import requests
import pytest


@pytest.mark.positive
def test_create_booking_positive():
    print("Create booking TC")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}

    json_body = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }

    response = requests.post(url=URL, headers=headers, json=json_body)
    print(type(URL))
    print(type(headers))
    print(type(json_body))

    assert response.status_code == 200



@pytest.mark.negative
def test_create_booking_negative():
    print("Create booking TC")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}

    json_body = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }

    response = requests.post(url=URL, json=json_body)
    print(type(URL))
    print(type(headers))
    print(type(json_body))

    assert response.status_code == 500