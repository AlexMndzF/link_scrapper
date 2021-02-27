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
                        type=int,
                        default=1
                        )
    args = parser.parse_args()
    return args


def main():
    args = get_config()
    url = Node(args.url)
    deep = args.deep
    GetUrls(HtmlParser()).get_urls(url=url, deep=deep, indentation=0)


if __name__ == "__main__":
    main()
