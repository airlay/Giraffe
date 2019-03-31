import json
import io

# create a dictionary
birthday = {
    'Albert Einstein': '03/7/1906',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '11/07/1941',
}

print('Whose birthday do you want to know?')

names = birthday.keys()

info_about_me = {"name": "Ronald", "has_a_dog": True}
with open("info.json", "r") as f:
    info = json.load(f)

print(info)

if info["has_a_dog"]:
    print('{} has a dog'.format(info["name"]))
else:
    print('{} has no dog'.format(info["name"]))

