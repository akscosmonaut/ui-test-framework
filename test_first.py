import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fixtures import string_for_search


def test_first_pass():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


def test_with_error():
    try:
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("запуск тестов")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    except Exception as err:
        driver.get_screenshot_as_file("test_with_error.png")
        pytest.fail()
    finally:
        driver.close()


def test_with_fixture(string_for_search):
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys(string_for_search)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


"""https://docs.pytest.org/en/6.2.x/parametrize.html - 
    Parametrizing fixtures and test functions"""


@pytest.mark.parametrize("search_string", ["functions", "asserts"])
def test_with_params(search_string):
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys(search_string)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


@pytest.mark.skip(reason="we test pytest")
def test_skipped():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
