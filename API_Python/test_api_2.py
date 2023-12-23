# Assertion - assert
# pytest

import requests


def test_sample():
    id = 1344
    base_url = "https://restful-booker.herokuapp.com/booking/"
    get_booking_details_url = base_url + str(id)
    response = requests.get(get_booking_details_url)
    print(response.status_code)
    #
    # if response.status_code == 200:
    #     print("The Get request is passed")
    # else:
    #     print("The Get request is failed")

    assert response.status_code == 200
    data = response.json()
    print(type(data))

    # Assertions
    assert 'firstname' in data, "Firstname key is present"
    assert 'lastname' in data, "Lastname key is present"
    assert 'totalprice' in data, "Total price key is present"
    # assert 'checkout' in data,"checkout key is present"

    assert data["firstname"] == "Jim", "Firstname  is Eric"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "The check in date is 2018-01-01"
    assert data["bookingdates"]["checkout"] == "2019-01-01", "The check out date is 2019-01-01"

    assert 'firstname'
def test_sample2():
    assert  5==4