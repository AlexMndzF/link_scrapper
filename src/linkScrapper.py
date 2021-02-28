from Utils import Node
from src.exceptions import NoUrlsFoundException


class LinkScrapper:
    def __init__(self, htmlparser):
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