import requests
from bs4 import BeautifulSoup
import re


def get_robots_txt(url):
    resp = requests.get(url + '/robots.txt')
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')

        allowed = re.findall(r"Allow: \/(.+)\s", soup.get_text())
        disallowed = re.findall(r"Disallow: \/(.+)\s", soup.get_text())

        # return both allowed directories and disallowed directories
        return allowed, disallowed

    return list(), list()


# print(get_robots_txt("https://www.informatics.uci.edu"))
