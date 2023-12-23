import requests


def main():
    id = '3433'
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url+id
    print(full_url)
    response_body= requests.get(full_url)
    print(response_body.status_code)


if __name__ == "__main__":
        main()
