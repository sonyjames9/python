from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime as dt
import random

MY_EMAIL = "aawrashopping@gmail.com"
PASSWORD = "zqff xnic bhkq swyt"

now = dt.datetime.now()
weekday =now.weekday()

# msg = MIMEMultipart()
# msg['From'] = MY_EMAIL
# msg['To'] = MY_EMAIL
# msg['Subject'] = "Test Motivation"
# msg.attach(MIMEText(body, 'plain'))

if weekday == 4: 
  with open("100DaysCode/day32/quotes.txt") as quote_file:
    all_quotes =  quote_file.readlines()
    quote = random.choice(all_quotes)
  print(quote)
  connection = smtplib
  body = quote

  with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
      from_addr=MY_EMAIL, 
      to_addrs=MY_EMAIL, 
      msg=f"Subject : Monday Motivation \n\n {quote}")
