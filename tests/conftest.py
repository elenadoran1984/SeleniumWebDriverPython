"""
This module contains shared fixtures.
"""

import json
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def config():

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):

    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        driver = webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()

# @pytest.fixture
# def browser():
#     # Selenium Manager automatically manages ChromeDriver
#     driver = webdriver.Chrome()
#
#     # Wait up to 10 seconds for elements
#     driver.implicitly_wait(10)
#
#     yield driver
#
#     # Close the browser
#     driver.quit()
