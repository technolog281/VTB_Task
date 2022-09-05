import argparse
import json
import os
import tempfile


os.chdir(os.path.expanduser("~"))
file_path = os.path.join(tempfile.gettempdir(), 'storage.data')
                                        # Проверка наличия папки task в домашней директории пользователя, создание папки
try:
    os.mkdir('task')
except FileExistsError:
    pass


def get_json():                         # Функция открывает хранилище storage.data, выгружает из него JSON
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        data = f.read()
        if data:
            return json.loads(data)
        return {}


def add(key: str, val: any):            # Функция добавляет в хранилище значение по ключу, либо пару ключ-значение
    json_dict = get_json()
    if key in json_dict:
        json_dict[key].append(val)
    else:
        json_dict[key] = [val]

    with open(file_path, 'w') as f:
        f.write(json.dumps(json_dict))


def show(key: str):                     # Функция извлекает значение ключа
    if key in get_json():
        return ', '.join(map(str, get_json().get(key)))
    elif key == 'all':
        return get_json()
    else:
        return None


if __name__ == '__main__':              # Запуск основного функционала скрипта, определяет аргументы при запуске
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Input KEY argument')
    parser.add_argument('--val', help='Input VALUE argument, or leave the field empty for seen the VALUE',
                        required=False)
    args = parser.parse_args()

    if args.key and args.val:
        add(args.key, args.val)
    elif args.key:
        print(show(args.key))
    else:
        print('Invalid Argument')
