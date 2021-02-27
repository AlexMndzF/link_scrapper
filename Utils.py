import re
import requests
from bs4 import BeautifulSoup


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_children(self, node):
        self.children.append(node)


class HtmlParser:
    def __init__(self):
        self.regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        self._get_html()
        self._get_links()

    def get_links(self, url):
        self.url = url
        self._get_html()
        self._get_links()

    def _get_html(self):
        res = requests.get(self.url)
        html = res.text
        self.soups = str(BeautifulSoup(html, 'html.parser'))

    def _get_links(self):
        self.links = set(re.findall(self.regex, self.soups))


class GetUrls:
    def __init__(self, HtmlParser, url):
        self.htmlparser = HtmlParser
        self.url = url

    def get_urls(self, url, deep, indentation):
        print("- " * indentation, url.value)
        if deep == 0:
            return
        links = HtmlParser(self.url).links
        for e in links:
            node = Node(e)
            self.get_urls(node, deep - 1, indentation + 1)
            url.add_children(node)
