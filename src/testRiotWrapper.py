import pytest
from .riotWrapper import riotWrapper  # Replace 'your_module' with the actual module name

@pytest.fixture
def riot_wrapper_instance():
    # Create an instance of the riotWrapper class for testing
    return riotWrapper("your_api_key", "https://oc1.api.riotgames.com")

def test_api_url_with_region(riot_wrapper_instance):
    # Test the api_url method with a specified region
    url = riot_wrapper_instance.api_url("/some/api/endpoint", "https://oc1.api.riotgames.com")
    assert url == "https://oc1.api.riotgames.com/some/api/endpoint?api_key=your_api_key"

def test_api_url_without_region(riot_wrapper_instance):
    # Test the api_url method without a specified region
    url = riot_wrapper_instance.api_url("/some/api/endpoint")
    assert url == "https://oc1.api.riotgames.com/some/api/endpoint?api_key=your_api_key"

def test_match_count(riot_wrapper_instance):
    # Test the match_count method
    url = riot_wrapper_instance.match_count("/match/v4/matchlists/by-account", "https://oc1.api.riotgames.com", match_count=10)
    expected_url = "https://oc1.api.riotgames.com/match/v4/matchlists/by-account?start=0&count=10&api_key=your_api_key"
    assert url == expected_url

def test_match_count_with_default_count(riot_wrapper_instance):
    # Test the match_count method with default match_count
    url = riot_wrapper_instance.match_count("/match/v4/matchlists/by-account", "https://oc1.api.riotgames.com")
    expected_url = "https://oc1.api.riotgames.com/match/v4/matchlists/by-account?start=0&count=20&api_key=your_api_key"
    assert url == expected_url
