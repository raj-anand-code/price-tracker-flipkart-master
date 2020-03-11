import smtplib
import requests
import time
from bs4 import BeautifulSoup


URL = 'https://www.flipkart.com/boat-rockerz-400-super-extra-bass-bluetooth-headset-mic/p/itmf3vhg5m9smugx?pid=ACCEJZXYKSG2T9GS&lid=LSTACCEJZXYKSG2T9GSOJDHG6&marketplace=FLIPKART&spotlightTagId=BestsellerId_0pm%2Ffcn&srno=b_1_1&otracker=hp_omu_Flipstart%2BDeals%2BOf%2BThe%2BDay_2_2.dealCard.OMU_JWYY3CHTQC09_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Flipstart%2BDeals%2BOf%2BThe%2BDay_NA_dealCard_cc_2_NA_view-all_2&fm=neo%2Fmerchandising&iid=3a791ca6-dbfa-4456-8dc8-b162f2e11cb1.ACCEJZXYKSG2T9GS.SEARCH&ppt=browse&ppn=browse&ssid=wxphjybiv40000001577955223392'

headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def price_tracker():

    page= requests.get(URL , headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    price = soup.find("div",class_="_1vC4OE _3qQ9m1").get_text()

    #print(price)
    #<div class="_1vC4OE _3qQ9m1">₹1,399</div>

    real_price = price[1:]
    real_price = real_price.replace(',','')
    real_price = int(real_price)
    print(real_price)

    if(real_price < 1100):
        send_notification()


def send_notification():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('emailid','passwordfrom2stepverification')

    sub = "Headphones Price"
    body = "Check this out  https://www.flipkart.com/boat-rockerz-400-super-extra-bass-bluetooth-headset-mic/p/itmf3vhg5m9smugx?pid=ACCEJZXYKSG2T9GS&lid=LSTACCEJZXYKSG2T9GSOJDHG6&marketplace=FLIPKART&spotlightTagId=BestsellerId_0pm%2Ffcn&srno=b_1_1&otracker=hp_omu_Flipstart%2BDeals%2BOf%2BThe%2BDay_2_2.dealCard.OMU_JWYY3CHTQC09_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Flipstart%2BDeals%2BOf%2BThe%2BDay_NA_dealCard_cc_2_NA_view-all_2&fm=neo%2Fmerchandising&iid=3a791ca6-dbfa-4456-8dc8-b162f2e11cb1.ACCEJZXYKSG2T9GS.SEARCH&ppt=browse&ppn=browse&ssid=wxphjybiv40000001577955223392"

    msg = f"{subject}\n\n{body}"

    server.sendmail(
        'from',
        'to',
        msg
    )


while(True):
    price_tracker()
    time.sleep(86400)