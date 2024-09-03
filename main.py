import requests
from secret import TOKEN

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

path ='Myfolder'


def create_folder(path):
    """Создание папки. \n path: Путь к создаваемой папке."""
    response = requests.put(f'{URL}?path={path}', headers=headers)
    code = response.status_code

    return code
    

def delete_folder(path):
    """Удаление папки. \n path: Имя удаляемой папки."""
    response = requests.delete(f'{URL}?path={path}', headers=headers)
    code = response.status_code

    return code   

