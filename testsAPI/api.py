import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
header = {"accept": "application/json", "Content-Type": "application/json"}


def test_add_pet():
    input_pet = {
        "id": 37,
        "category": {
            "id": 12,
            "name": "Djessi"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 21,
                "name": "Dog"
            }
        ],
        "status": "available"
    }

    res_post = requests.post(url="https://petstore.swagger.io/v2/pet", data=json.dumps(input_pet), headers=header)
# Тест 1. Добавляем питомца
    print(res_post.status_code) # Выводим информацию о сттусе теста
    print(res_post.json())
    res_json = json.loads(res_post.text)
    assert input_pet == res_json # Проверяем итог добавления с изначальной информацией о питомце
    res_get = requests.get(url=f"https://petstore.swagger.io/v2/pet/{input_pet['id']}")
# Тест 2. Находим добавленного питомца
    print(res_get.status_code)
    print(res_get.json())
    assert json.loads(res_get.text) == input_pet

def test_find_Pets_By_Status():
    input_pet = {
        "id": 3487,
        "category": {
            "id": 12,
            "name": "Dassi"
        },
        "name": "cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 27,
                "name": "Cat"
            }
        ],
        "status": "sold"
    }

    res_post = requests.post(url="https://petstore.swagger.io/v2/pet", data=json.dumps(input_pet), headers=header)

    print(res_post.status_code)
    print(res_post.text)
    print(res_post.json())
    res_json = json.loads(res_post.text)
    assert input_pet == res_json

    res_get = requests.get(url=f"https://petstore.swagger.io/v2/pet/findByStatus", params={"status": "sold"})
# Тест 3. Проверяем добавленного питомца по статусу
    print(res_get.status_code)
    assert input_pet in list(json.loads(res_get.text))

    res_delete = requests.delete(url=f"https://petstore.swagger.io/v2/pet/{input_pet['id']}")
# Тест 4. Удаляем питомца.
    out_del = {
  "code": 200,
  "type": "unknown",
  "message": "3487"
}
    assert json.loads(res_delete.text) == out_del
    res_get = requests.get(url=f"https://petstore.swagger.io/v2/pet/{input_pet['id']}")
# Проверяем, что питомец удален
    assert res_get.status_code == 404

def test_put_pet():
    input_pet = {
        "id": 37,
        "category": {
            "id": 12,
            "name": "Djonni"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 21,
                "name": "Dog"
            }
        ],
        "status": "available"
    }

    res_put = requests.put(url="https://petstore.swagger.io/v2/pet", data=json.dumps(input_pet), headers=header)
# Тест 5. Меняем информацию о питомце
    print(res_put.status_code)
    print(res_put.json())

def test_update_Pet_With_Form():
    input_pet = 'name=Bi'
    header = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
    res_update = requests.post(url=f"https://petstore.swagger.io/v2/pet/37", data=input_pet, headers=header)
# Тест 6. Добавляем информацию о питомце
    print(res_update.status_code)
    print(res_update.json())
    res_get = requests.get(url=f"https://petstore.swagger.io/v2/pet/37")
# Проверяем добавление информации о питомце
    print(res_get.json())
