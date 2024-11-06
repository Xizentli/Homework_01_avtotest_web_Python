import pytest
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def authorization():
    res = requests.post(data["url"] + "gateway/login",
                        data={"username": data["user"], "password": data["passwd"]})
    print(res.content)  # отладочный
    return res.json()["token"]


@pytest.fixture()
def test_text1():
    return "testtitle"
