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


def get_list_domen(html: str) -> list[str]:
    """Получить список доменов

    Args:
        html (str):  HTML-строка с ссылками

    Returns:
        list[str]: Отсортированный список уникальных доменов

    Пример:
    >>> html = '''<a href="http://stepik.org/courses">
    ... <a href='https://stepik.org'>
    ... <a href='http://neerc.ifmo.ru:1345'>
    ... <a href="ftp://mail.ru/distib" >
    ... <a href="ya.ru">
    ... <a href="www.ya.ru">
    ... <a href="../skip_relative_links">'''
    >>> result = get_list_domen(html)
    >>> for domain in result:
    ...     print(domain)
    mail.ru
    neerc.ifmo.ru
    stepik.org
    www.ya.ru
    ya.ru
    """
    list_url = []
    
    html = html.replace("'", '"')
    list_url = get_list_teg(html)
    
    list_url = [i for i in list_url if i.startswith('a href=')]   # фильтрация тегов
    list_url = [i.split('"')[1] for i in list_url]

    list_url = [i.replace('stepic.org', 'stepik.org') for i in list_url]    

    result = [i.split(':')[1] if ':' in i else i for i in list_url]
    result = [i.replace('//', '/') for i in result]
    result = [i.split('/')[1] if '/' in i else i for i in result] 
    result = [i for i in result if '.' in i] 
    result = sorted(list(set(result)))
    return result


def main():    
    URL = input()
    URL = 'http://pastebin.com/raw/7543p0ns'
    response = requests.get(URL).text

    result = get_list_domen(response)
    for domen in result:
        print(domen)
    

def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # tests()
    main()


# import re, requests
# domen = set()

# domen_pattern = re.compile(r'<a[^>]*?href=".*?://?(.*?)[:/"][^>]*?>')

# result = requests.get(input())
# [domen.add(i) for i in domen_pattern.findall(result.text)]
# [print(i) for i in sorted(domen)]