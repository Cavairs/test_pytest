from secret import TOKEN
from main import *



URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'OAuth {TOKEN}'  
}


path = 'Myfolder'

def test_create_folder_success():
    """Тест успешного создания папки"""
    status_code = create_folder(path)
    assert status_code == 201 , 'Папка с создана' 

def test_the_folder_already_exists():
    """Тест если папка уже существует"""
    status_code = create_folder(path)
    assert status_code == 409, 'Папка с таким именем уже существует'

def test_delete_folder():
    """Тест если папка удалена"""
    status_code = delete_folder(path)
    assert status_code == 204, 'Папка удалена'

