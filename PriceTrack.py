import requests
from bs4 import BeautifulSoup as bs
import smtplib

URL = 'https://www.amazon.in/LG-inch-68-58-Monitor-Built/dp/B07B8Q53XB/ref=sr_1_2?crid=18XUOAYAIZKDR&dchild=1&keywords=lg+27+inch+monitor&qid=1627897123&s=computers&sprefix=lg+27%2Ccomputers%2C293&sr=1-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = bs(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()

    price = soup.find(id = "priceblock_ourprice").get_text().replace(",",".")

    converted_price = float(price[1:7])

    print(title.strip())
    print(converted_price)

    if(converted_price < 22.000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('tahirsiddiqh@gmail.com', 'dfxqymdpbzttsplu')

    subject = 'Hey! Price went down'
    body = 'Check the link https://www.amazon.in/LG-inch-68-58-Monitor-Built/dp/B07B8Q53XB/ref=sr_1_2?crid=18XUOAYAIZKDR&dchild=1&keywords=lg+27+inch+monitor&qid=1627897123&s=computers&sprefix=lg+27%2Ccomputers%2C293&sr=1-2'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'tahirsiddiqh@gmail.com',
        'tahirsiddiqh@outlook.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

check_price()