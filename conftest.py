import pytest
from fixture.application import Application
import json
import os.path

fixture_create = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture_create
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture_create is None or not fixture_create.is_valid():
        fixture_create = Application(browser=browser, BUrl=web_config['BUrl'])
#    fixture_create.ses_h.is_login(loginname=web_config['username'], password=web_config['password'])
    return fixture_create


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture_create.ses_h.is_logout()
        fixture_create.district()
    # yield fixture_create
    request.addfinalizer(fin)
    return fixture_create


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
