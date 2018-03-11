import requests
import urllib
from urllib import parse


def request_endpoint(type: str, url: str, debug: bool=False):
    if type == 'get':
        req = requests.get(url)
        if debug : print_url_info(req)

    elif type == 'post':
        req = requests.post(url)
        if debug : print_url_info(req)

    else:
        print("Invalid request type from client")


def print_url_info(req: requests):
    req_attributes = {'encoding': req.encoding, 'status code': req.status_code, 'elapsed': req.elapsed,
                      'history': req.history, 'content-type': req.headers['Content-Type'], 'response': req.content}
    print("\n\n" + "~*+ {} information+*~".center(40).format(req.url))
    for (k, v) in req_attributes.items():
        print((str(k) + ':').rjust(20), str(v).ljust(4))


def validate_url(url: str):
    url_token = urllib.parse.urlparse(url)

    min_attributes = ('scheme', 'netloc')
    if not all([getattr(url_token, attr) for attr in min_attributes]):
        return False
    else:
        return True