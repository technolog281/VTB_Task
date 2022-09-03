import argparse
import json
import os

os.chdir(os.path.expanduser("~"))
file_path = os.path.join(os.getcwd(), 'task', 'storage.data')

try:
    os.mkdir('task')
except FileExistsError:
    pass


def get_json():
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        data = f.read()
        if data:
            return json.loads(data)
        return {}


def add(key: str, val: any):
    json_dict = get_json()
    if key in json_dict:
        json_dict[key].append(val)
    else:
        json_dict[key] = [val]

    with open(file_path, 'w') as f:
        f.write(json.dumps(json_dict))


def show(key: str):
    show_data = get_json()
    if key in show_data:
        show_value = show_data.get(key)
        show_str = ', '.join(map(str, show_value))
        return show_str
    else:
        return None


if __name__ == '__main__':
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
