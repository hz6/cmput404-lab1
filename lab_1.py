import requests as req

print("The version of requests library:\n", req.__version__)
pg = req.get("http://google.com")


def main():
    print("Page Content:\n", pg.content)
    print("Status Code:\n", pg.status_code)


main()
