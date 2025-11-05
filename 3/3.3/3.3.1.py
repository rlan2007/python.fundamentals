#! /usr/bin/python3

import requests


def get_list_teg(html) -> list[str]:
    """
        Получить список тегов
    Args:
        html (_type_, optional): _description_. Defaults to html.

    Returns:
        list[str]: _description_
    """
    list_teg = []
    stack = []
    text = ''
    teg = False

    for c in html:        
        if c == "<":
            teg = True
            stack.append(c)
        elif c == '>' and (len(stack) != 0):
            stack.pop()
            list_teg.append(text)
            text = ''
            teg = False
        elif teg:
            text += c
    
    return list_teg



def get_list_url(url: str) -> list[str]:
    list_url = []
    res = requests.get(url).text    

    list_url = get_list_teg(res)
    list_url = [i for i in list_url if i.startswith('a href=')]   # фильтрация тегов
    list_url = [i.split('"')[1] for i in list_url]
    list_url = [i.replace('stepic.org', 'stepik.org') for i in list_url]

    
    return list_url


get_list_url('https://stepik.org/media/attachments/lesson/24472/sample0.html')


def main():
    result = ['Yes', 'No']

    url_A = input()
    url_B = input()
     
    # url_A = 'https://stepik.org/media/attachments/lesson/24472/sample0.html'
    # url_B = 'https://stepik.org/media/attachments/lesson/24472/sample2.html'

    list_url = get_list_url(url_A)

    list_links = []

    for i in list_url:        
        list_links.extend(get_list_url(i))
           
    return 'Yes' if url_B in list_links else 'No'



if __name__ == "__main__":
    print(main())
   