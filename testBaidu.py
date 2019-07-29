# -*- coding: utf-8 -*-

from selenium import webdriver

# 定義驅動
driver = webdriver.Chrome()
# Open Baidu.com
driver.get('https://www.baidu.com')

# search a word e.g. 'selenium'
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
