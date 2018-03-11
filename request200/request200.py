import requests
import urllib
from urllib import parse

def getAndPrintInfo(url: str):
    req = requests.get(url)
    reqAttributes = {'encoding': req.encoding, 'status code': req.status_code, 'elapsed': req.elapsed,
                     'history': req.history, 'content-type': req.headers['Content-Type']}
    print("\n\n" + "~*+Your URL information+*~".center(40))
    for (k, v) in reqAttributes.items():
        print((str(k) + ':').rjust(20), str(v).ljust(4))

def validateUrl(url: str):
    urlToken = urllib.parse.urlparse(url)

    min_attributes = ('scheme', 'netloc')
    if not all([getattr(urlToken, attr) for attr in min_attributes]):
        return False
    else:
        return True


if __name__ == "__main__":
    url = input("\nHey kitty girl. Please enter a url to get: ")

    if validateUrl(url):
        getAndPrintInfo(url)
        if url.__contains__('trixiemattel'):
            print("\nUmmmmm....")
            print("...I see you like Trixie Mattel. Back off. She's mine...")

    else:
        print("{} is not a valid url.".format(url))


