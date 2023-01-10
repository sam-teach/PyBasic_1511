'''
Сериализация
'''
# JSON
import json

user = {
    'firstname': 'Taras',
    'lastname': 'Bulba',
    'age': 237,
    'email': 'taras_childfree@ukraine.ua',
    'items': [
        'sword',
        'horse',
        'sigar',
        'sombrero',
    ],
}
json_string = json.dumps(user)
print('json_string ->', type(json_string), json_string)
new_object = json.loads(json_string)
print('new_object ->', type(new_object), new_object)

li = [
    'sword',
    'horse',
    'sigar',
    'sombrero',
]
json_li_string = json.dumps(li)
print('json_li_string ->', type(json_li_string), json_li_string)
new_li_object = json.loads(json_li_string)
print('new_li_object ->', type(new_li_object), new_li_object)

with open('files/serialize.txt', 'wt') as file:
    json.dump(user, file)

with open('files/serialize.txt', 'rt') as file:
    new_object = json.load(file)
    print('new_object ->', type(new_object), new_object)
