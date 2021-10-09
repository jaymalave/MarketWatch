import smtplib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://economictimes.indiatimes.com/indices/nifty_50_companies")
print("Nifty 50")
print(" ")

ncheck = driver.find_element_by_xpath("/html/body/main/section/div[1]/div[1]/div[2]/div[1]")

print(ncheck.text)

conv_price = float(ncheck.text)

driver.close()


def send_mail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('jay.malave73@gmail.com', 'Google45!')

        subject = 'Nifty Price Check'

        body = 'Nifty has hit 14500'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('jay.malave73@gmail.com', 'manoj.malave@gmail.com', msg)
        smtp.sendmail('jay.malave73@gmail.com', 'jay.malave73@gmail.com', msg)


if conv_price > 14500:
    send_mail()
