#!/usr/bin/python

import argparse
from Utils import Node, HtmlParser, GetUrls


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',
                        help='Url to examine',
                        default="20",
                        type=str
                        ),
    parser.add_argument('-d', '--deep',
                        type=int
                        )
    args = parser.parse_args()
    return args


def main():
    args = 1  # get_config()
    url = Node("https://www.google.com")  # Nodo(args.url)
    deep = 2  # args.deep
    GetUrls().get_urls(url=url, deep=deep, indentation=0)


if __name__ == "__main__":
    main()
