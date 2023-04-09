# файл для выбора категории пользователем
import json
import os
from project1.spiders.constants import INPUT_TEXT, ERROR_TEXT

# открываем json, и возвращаем словарь с категориями
def get_dict_category(name_file: str = 'catalog_dict.json') -> dict:
    path_to_file = os.path.join(os.getcwd(), 'project1', 'spiders', name_file)
    with open(path_to_file, "r") as file:
        dict_category = json.load(file)

    return dict_category

# показываем какие есть категории и нумеруем их, пользователь должен выбрать номер категории, возвращаем
# словарь покатегорий относящийся к данной кагероии (категория - ключ, словарь подкатегорий - значение)
def get_dict_subcategory(dict_category: dict) -> dict:
    keys = list(dict_category.keys())
    for num, key in enumerate(keys):
        print(num, key)

    while True:
        number_category = input(INPUT_TEXT)
        if number_category.isdigit():
            index_category = int(number_category)
            if index_category >= 0 and index_category < len(keys):
                name_category = keys[index_category]
                dict_subcategory = dict_category[name_category]
                return dict_subcategory
        print(ERROR_TEXT)

# показываем и нумеруем подкатегории, просим пользователя выбрать номер, возвращаем url подкатегории
def get_url_subcategory(dict_subcategory: dict) -> str:
    subcategory_keys = list(dict_subcategory.keys())
    for num, key in enumerate(subcategory_keys):
        print(num, key)
    while True:
        number_subcategory = input(INPUT_TEXT)
        if number_subcategory.isdigit():
            index_subcategory = int(number_subcategory)
            if index_subcategory >= 0 and index_subcategory < len(subcategory_keys):
                name_subcategory = subcategory_keys[index_subcategory]
                url_subcategory = dict_subcategory[name_subcategory]
                return url_subcategory
        print(ERROR_TEXT)


dict_category = get_dict_category()
dict_subcategory = get_dict_subcategory(dict_category)
url_subcategory = get_url_subcategory(dict_subcategory)


