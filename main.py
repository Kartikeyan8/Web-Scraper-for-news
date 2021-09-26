import requests  # http requests
from bs4 import BeautifulSoup  # web scraping

import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime
now = datetime.datetime.now()
content = ''
def extract_news(url):

    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n' +'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i,tag in enumerate(soup.find_all('h1')):
        cnt=cnt+((str(i+1)+'::'+tag.text+"\n" +'<br>'))
    return (cnt)
cont=extract_news('https://scroll.in/')
content += cont
content += ('<br>------<br>')
content +=('<br><br>End of Message')
SERVER='smtp.gmail.com'
PORT='587'
FROM='karti@gmail.com'
To="kart"
TO=["kartik@bmsce.ac.in","karti@gmail.com"]
PASS='********'
message=MIMEMultipart()
message['Subject']='top news of'+ str(now.day)+'-'+str(now.month)
message['From']=FROM
message['To']=To
message.attach(MIMEText(cont,'html'))

server=smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
for a in TO:
    server.sendmail(FROM,a,message.as_string())

server.quit()

print("sent")
