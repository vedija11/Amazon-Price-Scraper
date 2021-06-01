# access a url and pull out data from website
import requests
# parse URL and pull out individual items using BeautifulSoup
from bs4 import BeautifulSoup
# enables to send emails
import smtplib
import time

URL = 'https://www.amazon.in/Boat-Rockerz-400-Bluetooth-Headphones/dp/B01J82IYLW/ref=gbps_img_s-5_9f8e_7e166db3?smid=A14CZOWI0VEHLG&pf_rd_p=b4500f5f-e496-4b18-ab75-623b14149f8e&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=R6BV8CKA61WS2QHE114P'

# give information about browser
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

def check_price():
    # returns all data from URL
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')       # parses everything
    # print(soup.prettify())

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:7].replace(",", ""))

    if converted_price < 1000:
        send_mail()
    else:
        print('Prices are high yet!')

    print("Product Name: ", title.strip())
    print("Product Price: ", converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()           # encrypts connection
    server.ehlo()

    server.login('vedija.jagtap99@gmail.com', 'PR@nvi11')
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Boat-Rockerz-400-Bluetooth-Headphones/dp/B01J82IYLW/ref=gbps_img_s-5_9f8e_7e166db3?smid=A14CZOWI0VEHLG&pf_rd_p=b4500f5f-e496-4b18-ab75-623b14149f8e&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=R6BV8CKA61WS2QHE114P '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('vedija.jagtap99@gmail.com', 'vjagtap@uncc.edu', msg)
    print('Hey, Price Drop Email has been sent!!')

    server.quit()

while(True):
    check_price()
    time.sleep(60)

