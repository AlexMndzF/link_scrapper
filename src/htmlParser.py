import re
import requests
from bs4 import BeautifulSoup

from src.exceptions import InvalidUrlException


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