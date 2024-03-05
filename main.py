import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com.tr/Sony-SONY-PlayStation-5-Konsol/dp/B08LQZGF76/ref=pd_rhf_gw_s_pd_crcd_d_sccl_1_1/261-6780019-0918446?pd_rd_w=PY8w9&content-id=amzn1.sym.89782163-dd54-4dad-b9f3-80f716133f0b&pf_rd_p=89782163-dd54-4dad-b9f3-80f716133f0b&pf_rd_r=775X4AKCM1NJ9YKP181V&pd_rd_wg=WLDxp&pd_rd_r=3bc17fca-2c2f-46ca-bae2-bfb5691f03a7&pd_rd_i=B08LQZGF76&th=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


def price_check(URL, max_price):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #title = soup.find(id="productTitle").getText().strip()
    price = soup.find("span", class_="a-price-whole").getText().strip()

    new_price = float(price[0: -1].replace(",", "."))

    print(new_price)

    if (new_price <= max_price):
        send_email("TO_EMAIL", URL)
    else:
        print("Urun fiyati dusmedi!")


def send_email(to_email, url):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("FROM_EMAIL", "APP_PASSWORD")

    subject = "Fiyat Dustu!"
    body = "Urun linki: " + url

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("FROM_EMAIL", "TO_EMAIL", msg)
    print("Mesaj gönderildi.")
    server.quit()


while (True):
    price_check(URL, 21000)
    time.sleep(86400)
