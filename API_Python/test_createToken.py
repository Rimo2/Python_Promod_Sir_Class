import requests


def create_auth():
    print("creating auth token")
    URL = "https://restful-booker.herokuapp.com/auth"
    json_body = {
        "username": "admin",
        "password": "password123"
    }
    Headers = {"Content-Type": "application/json"}

    response = requests.post(url=URL, json=json_body, headers=Headers)
    print(response.status_code)
    print(response.json())
    data = response.json()
    print(data["token"])
    token = data["token"]
    return token


def create_booking_id():
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
    booking_id = data["bookingid"]
    return booking_id


def test_update_booking():
    booking_id = create_booking_id()
    url = "https://restful-booker.herokuapp.com/booking/"
    booking_update_url = url + str(booking_id)
    json_body = {
        "firstname": "Rimo",
        "lastname": "Sen",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    cookie_token = "token=" + create_auth()
    header = {"Content-Type": "application/json",
              "Cookie": cookie_token}
    response = requests.put(url=booking_update_url, headers=header, json=json_body)
    print(response.json())


def test_crud():
    booking_id = create_booking_id()
    url = "https://restful-booker.herokuapp.com/booking/"
    booking_update_url = url + str(booking_id)
    json_body = {
        "firstname": "Rimo",
        "lastname": "Sen",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    cookie_token = "token=" + create_auth()
    header = {"Content-Type": "application/json",
              "Cookie": cookie_token}
    response = requests.put(url=booking_update_url, headers=header, json=json_body)
    print(response.json())

    delete_url= booking_update_url
    delete_response = requests.delete(url=delete_url,headers=header)
    print(delete_response.status_code)
    print(delete_response)


