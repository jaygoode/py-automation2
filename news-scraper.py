import requests

from bs4 import BeautifulSoup

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()

content = ''


def extract_news(url):
    print('Extracting hacker news stories')
    cnt = ''
    cnt += ('<b>HN top stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>')
                if tag.text != 'More' else '')
    return (cnt)

    cnt = extract_news('https://news.vcombinator.com/')
    content += cnt
    content += ('<br>-----<br>')
    content += ('<br><br>End of message.')
