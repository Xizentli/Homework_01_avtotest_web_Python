import requests
import yaml


with open("config.yaml") as f:
    data = yaml.safe_load(f)


# проверка поста с определенным заголовком
def test_step1(authorization, test_text1):
    header = {"X-Auth-Token": authorization}
    res = requests.get(data["url"] + "api/posts", params={"owner": "notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert test_text1 in listres, "test1 FAIL"


# создание поста
def test_step2(authorization):
    header = {"X-Auth-Token": authorization}
    res = requests.post(data["url"] + "api/posts",
                        params={"title": data["title"],
                                "description": data["description"],
                                "content": data["content"]},
                        headers=header)
    assert res.status_code == 200, "test2 FAIL"


# проверка созданного поста по его описанию
def test_step3(authorization):
    header = {"X-Auth-Token": authorization}
    res = requests.get(data["url"] + "api/posts", headers=header)
    listres = [i["description"] for i in res.json()["data"]]
    assert data["description"] in listres, "test3 FAIL"