import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Sony-Systemkamera-Klapp-Display-Echtzeit-Autofokus-AF-Punkten/dp/B07MWDKNGN/ref=bmx_1/261-2169693-9658667?_encoding=UTF8&pd_rd_i=B07MWDKNGN&pd_rd_r=a0ccb857-fc6e-44b3-9cf5-ca9c7ffedf2c&pd_rd_w=b3qny&pd_rd_wg=07Oji&pf_rd_p=07e652d0-e9c7-4e49-9d93-bd6d8b013439&pf_rd_r=F30Q8TKB8B7SXBCVT1XN&psc=1&refRID=F30Q8TKB8B7SXBCVT1XN'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html5lib')

    # print(soup.prettify())
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])
    print(title.strip())
    print(converted_price)
    if(converted_price < 800):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('emailaddress', 'password')

    subject = 'Price dropped down!'
    body = 'Check the amazon link https://www.amazon.de/Sony-Systemkamera-Klapp-Display-Echtzeit-Autofokus-AF-Punkten/dp/B07MWDKNGN/ref=bmx_1/261-2169693-9658667?_encoding=UTF8&pd_rd_i=B07MWDKNGN&pd_rd_r=a0ccb857-fc6e-44b3-9cf5-ca9c7ffedf2c&pd_rd_w=b3qny&pd_rd_wg=07Oji&pf_rd_p=07e652d0-e9c7-4e49-9d93-bd6d8b013439&pf_rd_r=F30Q8TKB8B7SXBCVT1XN&psc=1&refRID=F30Q8TKB8B7SXBCVT1XN'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender email',
        'recepiter email',
        msg
    )
    print('Mail sent')

    server.quit()


check_price()