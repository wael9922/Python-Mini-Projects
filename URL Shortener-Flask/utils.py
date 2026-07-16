import pyshorteners
from urllib.parse import urlparse


def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])


def shorten_url(url, service):
    """
    Shorten
    :param url: url: str
    :param service: service: str
    :return: url: str
    """
    if not url:
        return None, "Please enter a URL"

    if not is_valid_url(url):
        return None, "Invalid URL format"

    short = pyshorteners.Shortener()

    shortener_methods = {
        "TinyURL": short.tinyurl.short,
        "Clck.ru": short.clckru.short,
        "OSDB": short.osdb.short,
        "Ow.ly": short.owly.short,
    }

    try:
        shortened_url = shortener_methods[service](url)
        return shortened_url, None
    except Exception:
        return None, "Error shortening URL. Try another service."