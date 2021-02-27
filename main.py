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


def get_urls(url, deep, indentation):
    """
    Funcion que devuelve una lista de urls contenidas en la url principal.
    """

    print("- "*indentation, url.value)

    if deep == 0:
        return
    links = HtmlParser().links
    for e in links:
        node = Node(e)
        get_urls(node, deep - 1, indentation + 1)
        url.add_children(node)


def main():
    args = 1  # get_config()
    url = Node("https://www.google.com")  # Nodo(args.url)
    deep = 2  # args.deep
    get_urls(url, deep, 0)


if __name__ == "__main__":
    main()
