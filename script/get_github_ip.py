# coding=utf8
# date: 2021-04-07
# desc: get GitHub IP

import requests
import re
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, site):
        threading.Thread.__init__(self)
        self.site = site

    def run(self):
        get_site_ip(self.site)


def get_site_ip(site):
    search_url = 'https://www.ipaddress.com/search/'
    url = search_url + site
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/89.0.4389.128 Safari/537.36'}
    r = requests.get(url, headers=hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    url = re.findall(r'ipv4/[\d.]+', r.text)
    ip = str(url[0]).split('/')[1]
    print('{} {}'.format(ip, site))


def get_from_ipaddress():
    site_list = ['github.com', 'assets-cdn.github.com', 'github.global.ssl.fastly.net']
    for site in site_list:
        t = MyThread(site)
        t.start()


def get_from_hellogithub():
    url = 'https://raw.hellogithub.com/hosts'
    r = requests.get(url)
    print(r.text)


def main():
    # get_from_ipaddress()  # not work now
    get_from_hellogithub()
    time.sleep(3)


if __name__ == '__main__':
    main()
