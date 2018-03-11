from app import app
from app.managers.request import request_endpoint, validate_url


if __name__ == "__main__":
    url = input("\nHey kitty girl. Please enter a url to get: ")

    if validate_url(url):
        request_endpoint('get', url, debug=True)
        if url.__contains__('trixiemattel'):
            print("\nUmmmmm....")
            print("...I see you like Trixie Mattel. Back off. She's mine...")

    else:
        print("{} is not a valid url.".format(url))
