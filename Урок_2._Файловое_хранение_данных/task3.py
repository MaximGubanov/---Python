import yaml


data_dict = {
    'key_1': ['a', 'b', 'c'],
    'key_2': 555,
    'key_3': {
        'k1': '€',
        'k2': 'ℤ',
        'k3': 'ℚ',
    }
}


with open('file.yaml', 'w') as file_yaml:
    yaml.dump(data_dict, file_yaml, default_flow_style=True, allow_unicode=True)


with open('file.yaml') as file_yaml:
    print(file_yaml.read())
    