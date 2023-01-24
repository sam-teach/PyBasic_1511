# """
# Decorators - функціі які у якості параметра приймають функцію,
#  та повертають в якості результатат теж функцію
# """
#
#
# def decor(some_fun):
#     def inner_fun(li: list):
#         result = some_fun(li)
#         if result < 0: result = 0
#         return result
#
#     return inner_fun
#
#
# @decor
# def my_sum(li: list):
#     return sum(li)
#
#
# li = [1, -2, -3, 4, -5]
# print(my_sum(li))
#
#
# def pretty_text(fun_printing_text):
#     def output():
#         print('*' * 10)
#         fun_printing_text()
#         print('*' * 10)
#     return output
#
# @pretty_text
# def print_hello():
#     print('Hello')
#
# print_hello()

"""
requests - бібліотека HTTP
"""
# import requests
#
# url = "http://api.forismatic.com/api/1.0/"
# params = {
#     "method": "getQuote",
#     "format": "json",
#     "key": 5,
#     "lang": "ru"
# }
#
# response = requests.get(url, params=params)
# print(response.text)

import requests
from requests_oauthlib import OAuth1
import os


key = os.environ['key']
secret = os.environ['secret']
auth = OAuth1(key, secret)
endpoint = "http://api.thenounproject.com/icon/3"

response = requests.get(endpoint, auth=auth)
result = response.json()
icon_url = requests.get(result['icon']['icon_url'])
print(icon_url.content)
with open('file.svg','wb') as file:
    file.write(icon_url.content)


print(os.environ['aaa'])