"""Given a wikipedia article as our single argument, print out the links."""
import argparse
import sys

import requests

from bs4 import BeautifulSoup


def is_article_link(href):
    if href is None:
        return False
    return href.startswith("/wiki/") and ":" not in href


def generate_links(url):
    text = requests.get(url).text
    soup = BeautifulSoup(text, "html.parser")
    for link in soup.find_all("a"):
        if is_article_link(link.get("href")):
            yield link["href"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    child_articles = set(generate_links(args.url))
    for child_article in child_articles:
        print(child_article)
    sys.stderr.write("%d\n" % len(child_articles))


if __name__ == "__main__":
    sys.exit(main())
