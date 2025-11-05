# import requests

# url = 'https://docs.python.org/3.5'

# res = requests.get(url)
# print(res.status_code)
# print(res.headers)

# print(res.content)
# print(res.text)

# ###########################

# import requests

# url = 'https://docs.python.org/3.5'

# res = requests.get(url)
# print(res.status_code)
# print(res.headers['Content-Type'])

# print(res.content)
# print(res.text)


###########################

import requests

url = 'https://yandex.ru/search'
params = {'text': "Stepic"}

res = requests.get(url, params)
print(res.status_code)
print(res.headers['Content-Type'])

print(res.url)
print(res.content)
print(res.text)