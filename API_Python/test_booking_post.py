# 1. Python frame works --> Unit Test, Nose, Pytest
# 2. Every test will start from test_name.py
# 3. pytest -h will list down all the helps regarding pytest
import pytest
# Create booking using pytest

import requests


@pytest.mark.positive
def test_create_booking_positive():
    print("Create booking test case")

    booking_url = "https://restful-booker.herokuapp.com/booking"
    Headers = {"Content-Type": "application/json"}
    body = {
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

    response = requests.post(url=booking_url, headers=Headers, json=body)
    print(response.status_code)
    print(response.json())
    data = response.json()

    assert data["booking"]['firstname'] == "Jim"
    assert data["booking"]["bookingdates"]["checkin"] == "2018-01-01"
    assert data["booking"]["bookingdates"]["checkout"] == "2019-01-01"
    assert response.status_code == 200

    booking_id = response.json()["bookingid"]
    assert response.status_code == 200, "Expected status code 200"
    print(f"The booking id is {booking_id}")
    return booking_id


def test_get_bookingDetails():
    id = test_create_booking_positive()
    base_url = "https://restful-booker.herokuapp.com/booking/"
    get_booking_details_url = base_url + str(id)
    response = requests.get(get_booking_details_url)
    print(response.status_code)

    assert response.status_code == 200
    data = response.json()

    assert data["firstname"] == "Jim", "Firstname  is Eric"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "The check in date is 2018-01-01"
    assert data["bookingdates"]["checkout"] == "2019-01-01", "The check out date is 2019-01-01"


def test_create_booking_negative():
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    Headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=Headers, json=json_payload)
    print(type(URL))

    assert response.status_code == 500


