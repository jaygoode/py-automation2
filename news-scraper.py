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


# send mail

print('composing Email...')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'johnny_nyl@hotmail.com'
TO = 'johnny_nyl@hotmail.com'
PASS = '******'

msg = MIMEMultipart()

msg['Subject'] = 'Top news stories HN' + \
    ' ' + str(now.day) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initiating server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email sent!')

server.quit()
