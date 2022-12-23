from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0
    print(len(result['pets']))
    print('Вот столько питомцев:', len(result['pets']))


def test_add_new_pet_with_valid_data(name='Mike', animal_type='dog',
                                     age='5', pet_photo='images/wolf.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Joky", "dog", "5", "images/dog.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Кот', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
  '''Далее мои Тесты для задания 19.7'''


def test_create_pet_simple_with_valid_data(name='Loky', animal_type='parrot', age=20):
    """Проверяем что можно добавить питомца с корректными данными без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_get_my_pets_with_valid_key(filter='my_pets'):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее запрашиваем длину списка"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_my_pets(auth_key, filter)

    assert status == 200
    print("my_pets")
    assert len(result['pets']) > 0
    print('Вот столько питомцев:', len(result['pets']))


def test_change_age_as_int():
    """Пытаемся изменить возраст с числовым значением"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id = pf.get_list_of_pets(auth_key, filter="my_pets")[1]['pets'][0]['id']
    new_age = 155
    try:
        status, result = pf.update_pet_info(auth_key, pet_id, name='test', animal_type='dog', age=new_age)
    except AssertionError:
        print('Please use correct format of age')


def test_change_age_as_str():
    """Пытаемся изменить возраст со строковым значением"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id = pf.get_list_of_pets(auth_key, filter="my_pets")[1]['pets'][0]['id']
    new_age = '100'
    status, result = pf.update_pet_info(auth_key, pet_id, name='test', animal_type='dog', age=new_age)
    assert status == 200
    assert result['age'] == new_age


def test_change_name_with_wrong_id():
    """Пытаемся изменить имя питомца с неверным id"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id = "hyytbd6556y"
    new_name = 'Frank'
    status, result = pf.update_pet_info(auth_key, pet_id, name=new_name, animal_type='dog', age=2)
    assert status == 400
    print('Please use correct id')


def test_get_pets_with_wrong_api_key():
    """проверка что сервер отывечает 403 при неверном key"""

    wrong_key = {
        'key': 'ea738148a1f19838e1c5d141'
    }
    status, result = pf.get_list_of_pets(auth_key=wrong_key)
    assert status == 403, f'Error status code, expected: 403, got: {status}'


def test_change_my_pet_name():
    """проверка что имя изменилось при передаче валидного имени"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id = pf.get_list_of_pets(auth_key=auth_key, filter="my_pets")[1]['pets'][0]['id']  # get the first pet id
    new_name = 'TestName'
    status, result = pf.update_pet_info(auth_key=auth_key, pet_id=pet_id, name=new_name, animal_type='', age=8)
    assert result['name'] == new_name, f"Wrong changed name expected is: {new_name} but actual is: {result['name']}"


def test_change_animal_type():
    """Изменяем тип питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id = pf.get_list_of_pets(auth_key, filter="my_pets")[1]['pets'][0]['id']
    new_type = 'groundhog'
    status, result = pf.update_pet_info(auth_key, pet_id, name='', animal_type=new_type, age=15)
    assert result['animal_type'] == new_type


def test_add_new_pet_with_invalid_photo(name='Bob', animal_type='dog',
                                     age='4', pet_photo='images/uhiughj.jpg'):
    """Пытаемся добавить питомца с некорректными данными"""

    # Пытаемся получить путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    try:
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    except FileNotFoundError:
        print('File does not exist')


def test_add_new_pet_with_no_data():
    """Пытаемся добавить питомца без данных"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    try:
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    except NameError:
        print('Please use correct data')
