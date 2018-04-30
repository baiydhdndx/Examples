import requests
import re

def get_urls(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    url_addr = r'<img src="(.*?\.gif)" alt="" />'
    url_list = re.findall(url_addr, response.text)    #response.text->字符串   response.json->json对象  response.content->二进制

    return url_list

def get_gif(url, name):
    file_path = 'E:\\workspacee\\Python\\crawler\\case1\\data\\%d.gif' % name
    response = requests.get(url)
    response.encoding = 'utf-8'

    with open(file_path, 'wb') as ft:
        ft.write(response.content)
        print(file_path)

if __name__=='__main__':
    first_urls = ['http://qq.yh31.com/zjbq/0981223.html',
            'http://qq.yh31.com/zjbq/0981223_2.html',
            'http://qq.yh31.com/zjbq/0981223_3.html',
            'http://qq.yh31.com/zjbq/0981223_4.html',
            'http://qq.yh31.com/zjbq/0981223_5.html']
    name_index = 1
    for first_url in first_urls:
        url_list = get_urls(first_url)
        for url in url_list:
            com_url = 'http://qq.yh31.com/' + url
            get_gif(com_url, name_index)
            name_index += 1