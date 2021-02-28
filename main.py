#!/usr/bin/python

import argparse
from Utils import Node
from src.exceptions import InvalidUrlException
from src.htmlParser import HtmlParser
from src.linkScrapper import LinkScrapper
from requests.exceptions import ConnectionError, MissingSchema


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',
                        help='Url to extract urls',
                        type=str
                        ),
    parser.add_argument('-d', '--deep',
                        help='Deep of extraction, by default 1 for make the first iteration.',
                        type=int,
                        default=1
                        )
    args = parser.parse_args()
    return args


def main():
    args = get_config()
    url = Node(args.url)
    deep = args.deep
    try:
        LinkScrapper(HtmlParser()).get_urls(url=url, deep=deep, indentation=0)
    except (ConnectionError, MissingSchema) as e:
        print(f'Invalid host: {e}')


if __name__ == "__main__":
    main()
