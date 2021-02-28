from requests.exceptions import ConnectionError, MissingSchema

URlS_MOCK = {
    'google.es': ['facebook.es/1', 'whatsapp.es/1', 'instagram.es/1'],
    'facebook.es/1': ['facebook.es/2'],
    'facebook.es/2': ['facebook.es/3'],
    'whatsapp.es/1': ['whatsapp.es/2'],
    'whatsapp.es/2': ['whatsapp.es/3'],
    'instagram.es/1': ['instagram.es/2'],
    'instagram.es/2': ['instagram.es/3']
}


def url_mock(url):
    urls = URlS_MOCK.get(url)
    return urls
