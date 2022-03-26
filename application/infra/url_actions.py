from html2image import Html2Image
import re


def get_screenshot(url_address: str, path: str, save_as="screenshot.png"):
    """
    Get screenshot from a giving url
    :return: screenshot.png
    """
    hti = Html2Image(output_path=path, custom_flags=['--no-sandbox'])
    # hti.browser.flags.append('--no-sandbox')
    hti.screenshot(url=url_address, save_as=save_as)


def validate_url(url_address: str) -> str:
    """
    Gets url address, verifies it and ask until it's valid
    :return: the valid url address
    """
    _check = is_url(url_address)
    while not _check:
        url_address = input("Please send a valid url address: ")
        _check = is_url(url_address)

    print("URL is valid!")
    return url_address


def is_url(url) -> bool:
    """
    Verifies the url address to be valid
    :return: True if valid, False if not
    """
    regex = re.compile(
        r'^(?:http|ftp)s?://'                                                                 # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
        r'localhost|'                                                                         # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'                                                # or ip
        r'(?::\d+)?'                                                                          # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None
