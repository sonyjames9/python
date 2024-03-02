import datetime as dt
import pandas
import random
import smtplib


MY_EMAIL = "aawrashopping@gmail.com"
PASSWORD = "zqff xnic bhkq swyt"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("100DaysCode/day32/birthdays.csv")

birthday_dicts = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dicts:
  birthday_person = birthday_dicts[today_tuple]
  file_path = f"100DaysCode/day32/letter_templates/letter_{random.randint(1, 3)}.txt"

  with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", birthday_person["name"])
  
  with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs=birthday_person["email"],
      msg=f"Subject: Happy birthday !\n\n {contents}")
    