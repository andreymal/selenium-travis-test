#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import sys

from selenium import webdriver


def main():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('no-sandbox')

    browser = webdriver.Chrome(chrome_options=options)
    browser.get('https://www.google.com/')

    if 'Google' not in browser.title:
        print('FAIL')
        return 1

    print('OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
