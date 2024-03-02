# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib
# 
# my_email = "aawrashopping@gmail.com"
# password = "yraf xnic bhkq rwyt"
# 
# msg = MIMEMultipart()
# msg['From'] = my_email
# msg['To'] = my_email
# msg['Subject'] = "Test Mail"
# body = "Test mail from python"
# msg.attach(MIMEText(body, 'plain'))
# 
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#   connection.login(user=my_email, password=password)
#   connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg.as_string())

import datetime as dt
now = dt.datetime.now()
year = now.year
hour = now.hour
month = now.month
minute = now.minute
day_week = now.weekday()
print(now, year, hour, month, minute, day_week)