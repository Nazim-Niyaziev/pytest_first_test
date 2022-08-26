import pytest


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = '/applications/Google Chrome'
    chrome_options.add_extension(
        '/Users/admin/Library/Application Support/Google/Chrome/Default/extensions/extension.crx')
    chrome_options.add_argument('--kiosk')
    return chrome_options
