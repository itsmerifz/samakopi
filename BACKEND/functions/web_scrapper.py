from bs4 import BeautifulSoup
import requests
import re

def get_web_texts(link: str) -> str:
  try:
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')
    content = soup.find_all('p')
    text = ''
    for i in content:
      text += i.text
    text = re.sub('[^A-Za-z]+', ' ', text.lower())
    return text
  except Exception as e:
    return str(e)
  