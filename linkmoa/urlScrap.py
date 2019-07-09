from multiprocessing import Pool
from urllib.request import urlopen
import urllib.request
import bs4
import requests
import time

def scrapUrl(list, key):
    start = time.time()
    urlList = []
    print(key +"를 찾아보자!")
    for i in range(0, len(list)):
        print(i+1," 번째 URL : " + list[i])
        if list[i] is not '':
            if crawling(list[i], key) is not False:
                urlList.append(list[i])

    if len(urlList) == 0:
        return 'N'

    print("time : ", time.time() - start )
    urlList = "\n".join(urlList)
    return urlList

def crawling(url, key):
    try:
        main_url = url
        main_html = urlopen(main_url)
    except:
        print('open faild')
        return False
    if key.lower() in main_html.read().decode("utf-8").lower():
        print("찾았당")
        return True

    print("여긴 없당")
    return False