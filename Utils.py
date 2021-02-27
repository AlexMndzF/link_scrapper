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

    def get_links(self, url):
        self.url = url
        self._get_html()
        links = set(re.findall(self.regex, self.soups))
        return links

    def _get_html(self):
        res = requests.get(self.url)
        html = res.text
        self.soups = str(BeautifulSoup(html, 'html.parser'))



class GetUrls:
    def __init__(self, htmlparser=HtmlParser()):
        self.htmlparser = htmlparser

    def get_urls(self, url, deep, indentation):
        print("- " * indentation, url.value)
        if deep == 0:
            return
        links = self.htmlparser.get_links(url.value)
        for e in links:
            node = Node(e)
            self.get_urls(node, deep - 1, indentation + 1)
            url.add_children(node)
