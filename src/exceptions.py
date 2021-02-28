class InvalidUrlException(Exception):
    def __init__(self, status_code):
        self.status_code = status_code


class NoUrlsFoundException(Exception):
    def __init__(self, url):
        self.url = url
