from multiprocessing import Pool
from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
import urllib.request
import bs4
import requests
import time

def scrapUrl(list, key):
    start = time.time()
    urlList = []
    print("key : " + key)
    for i in range(0, len(list)):
        print(i+1," URL : " + list[i])
        if list[i] is not '':
            if crawling(list[i], key) is not False:
                urlList.append(list[i])
    print("time : ", time.time() - start )
    if len(urlList) == 0:
        return 'N'

    urlList = "\n".join(urlList)
    return urlList

def crawling(url, key):
    try:
        main_url = url
        main_html = urlopen(main_url)
    except HTTPError as e:
        print('open faild')
        return False
    except URLError as e:
        print('urlError')
        return False
    except Exception as e:
        print('unknow exception')
        return False
    if key.lower() in main_html.read().decode("utf-8").lower():
        print(key + " is found in " + url)
        return True

    print("Not found")
    return False