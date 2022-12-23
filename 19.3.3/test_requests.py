import requests
import json


"""Для тестов используются рандомные данные"""

def test_add_pet():
    input_pet = {
        "id": 15,
        "category": {
            "id": 17,
            "name": "Bobik"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 19,
                "name": "Dog"
            }
        ],
        "status": "available"
    }
 header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res = requests.post(url='https://petstore.swagger.io/v2/pet', headers=header, data=json.dumps(input_pet))
    print(res)
    print(res.text)
    print(res.json())



def test_find_by_status():

    status = 'available'
    header = {'accept': 'application/json'}

    res = requests.get(url='https://petstore.swagger.io/v2/pet/findByStatus', headers=header, params=status)
    print(res)
    print(res.text)
    print(res.json())


def test_find_by_id():

    pet_id = '15'
    header = {'accept': 'application/json'}

    res = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=header)
    print(res)
    print(res.text)
    print(res.json())
def test_update_pet():
    data = {
        "id": 15,
        "category": {
            "id": 4,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 6,
                "name": "string"
            }
        ],
        "status": "available"

        }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res = requests.put(url='https://petstore.swagger.io/v2/pet', headers=header, data=json.dumps(data, ensure_ascii=False))

    print(res)
    print(res.text)
    print(res.json())

def test_update_with_form_data():
    pet_id = '15'
    data = {
        'name': 'Bobik',
        'status': 'available'
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

    res = requests.post(url=f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=header, data=data)
    print(res)
    print(res.text)
    print(res.json())


def test_upload_image():

    """Здесь используются рандомные значения - в этой связи результат теста 400"""

    pet_id = '20'
    header = {'accept': 'application/json', 'Content-Type': 'multipart/form-data'}

    file = {'file': 'animal.jpg', 'type': 'image/jpeg'}

    res = requests.post(url=f'https://petstore.swagger.io/v2/pet/{pet_id}/uploadImage', headers=header, data=file)
    print(res)


def test_delete_pet():

    pet_id = '15'
    header = {'accept': 'application/json', 'api_key': 'special-key'}

    res = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=header)
    print(res)
    print(res.text)
    print(res.json())
