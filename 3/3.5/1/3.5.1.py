import requests

# нужно поменять адрес прокси на рабочий. 
# Здесь: https://hidemy.name/ru/proxy-list можно найти рабочий прокси
proxies = {
  'http': 'http://172.67.75.181:80',
  'https': 'http://188.114.96.13:80',
}

numeric = 31
BaseURL = "http://numbersapi.com/"
URL = f"{BaseURL}/{numeric}/math"
params = {'json': True}

response = requests.get(URL, params, proxies=proxies, timeout=5)

print(response.text)