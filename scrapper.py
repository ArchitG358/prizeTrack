import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/Logitech-Stream-Webcam-Streaming-Recording/dp/B01M35CNS8/ref=sr_1_6?keywords=webcam&qid=1584297219&s=electronics&sr=1-6"
# URL1 = "https://www.amazon.in/Logitech-C310-HD-Webcam-Black/dp/B008QS9KMW/ref=pd_sbs_147_2/262-4643686-3005848?_encoding=UTF8&pd_rd_i=B008QS9KMW&pd_rd_r=977d1667-88a9-47d2-98a5-23a5725ec6da&pd_rd_w=BgzHF&pd_rd_wg=UgB8Y&pf_rd_p=fbf43daf-8fb3-47b5-9deb-ae9cce3969a9&pf_rd_r=DW8D5MDQ7D40WTMD6SDC&psc=1&refRID=DW8D5MDQ7D40WTMD6SDC"
# URL2 = "https://www.amazon.in/dp/B07W7LH3ZK/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B07W7LH3ZK&pd_rd_w=8L0xK&pf_rd_p=357151f8-058c-46f1-b7d1-fa3647ce3999&pd_rd_wg=QcLGW&pf_rd_r=XN02K7H0S07E577MS8QW&pd_rd_r=9908f42f-ff83-47cd-943d-18f671c4830d&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMFQwOFBFQU9OWjMyJmVuY3J5cHRlZElkPUEwMTQ0OTEwMTE3Rjk0UDJYRUNINSZlbmNyeXB0ZWRBZElkPUEwMjI2NDk5NTdTOElVTjFRREszJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

FROM = input("Email: ")       #pricetracker358@gmail.com
pswd = input("Password: ")    #google.co.
TO = input("Enter email for updates ")

def send_mail(title):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(FROM,pswd)

    sub = "Price got lower check out"
    body = f"PRODUCT:{title}\n{URL}"
    msg = f"Subject: {sub}\n{body}"
    server.sendmail(FROM, TO, msg)
    print("Email sent!!")
    server.quit()

def check():
    price = int(input("Enter the min. cost  "))

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    cost = soup.find(id="priceblock_ourprice").get_text()
    cost_num = float(cost[2:].replace(",", ""))

    if cost_num < price:
        send_mail(title)
    else:
        print("Price is still high!!")

check()