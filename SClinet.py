# Author :Jungang_An
# -*- coding: utf-8 -*-
# Time : 2020/10/10 11:02

import requests


if __name__ == '__main__':
    PDF_url = 'http:xxxx.pdf'
    url = 'http://128.0.0.1:8080/pdf'
    res1 = requests.post(url, {'image_url': PDF_url})
    print(res1)