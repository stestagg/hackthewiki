import sys
import requests


def main():
    print(requests.get("https://en.wikipedia.org/wiki/Special:Random").text)


if __name__ == '__main__':
    sys.exit(main())
