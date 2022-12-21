import random
import pytest


# @pytest.fixture(scope="session")
# @pytest.fixture(scope="module")
# @pytest.fixture(scope="class")
@pytest.fixture
def string_for_search():
    test_string = ['vdhzWxXpFw', 'xdxyrDImyF', 'KfseEZfQnj', 'mZvwdzUXyD',
                   'LYYbgMLKMD']
    return random.choice(test_string)