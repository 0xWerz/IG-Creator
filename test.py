from lib2to3.pgen2 import driver
from aiohttp import request


import requests
from selenium import webdriver


driver = webdriver.Chrome('/home/werz/Downloads/browsers-drivers/chromedriver')


url = 'https://youtube.com'
driver.get(url)


