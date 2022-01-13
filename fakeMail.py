import requests
from bs4 import BeautifulSoup

def getFakeMail():
    url = 'https://10minutemail.net/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    mail = soup.find("button", {"id": "copy-button"})
    return mail['data-clipboard-text']


