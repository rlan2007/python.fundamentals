#! /usr/bin/python3

import requests

def main():
    pass
    URL = input()
    response = requests.get(URL)
    return response.text


if __name__ == "__main__":
    print(main())