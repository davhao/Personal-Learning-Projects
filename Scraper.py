from bs4 import BeautifulSoup
import requests
import smtplib
import time

URL = 'https://www.amazon.de/Lenovo-ThinkPad-Carbon-Ultrabook-20KH0035GE/dp/B07BYFV3ZD/ref=sr_1_3?__mk_de_DE=ÅMÅŽÕÑ&keywords=x1+carbon&qid=1568690568&sr=8-3'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.600):
        send_mail()

    print(title.strip())
    print(price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('davidjhao2000@gmail.com', 'sxxwuiblvbiowpjp')

    subject = 'PRICE HAS FALLEN'
    body = 'GO BUY IT NOW!!!'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'davidjhao2000@gmail.com',
        'davidjhao2000@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(86400)