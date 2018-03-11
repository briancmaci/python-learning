import requests
import sys

def getAndPrintInfo(url: str):
    req = requests.get(url)
    reqAttributes = {'encoding': req.encoding, 'status code': req.status_code, 'elapsed': req.elapsed,
                     'history': req.history, 'content-type': req.headers['Content-Type']}
    for (k, v) in reqAttributes.items():
        print("{}: {}".format(k, v))


if __name__ == "__main__":
    getAndPrintInfo(sys.argv[1])
