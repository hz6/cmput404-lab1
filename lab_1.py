import requests as req


def main():
    print(req.get("http://google.com"))
    print(req.__version__)


main()
