import smtplib
import datetime as dt
import random
my_email = ""
password = ""

now = dt.datetime.now()
hour = now.hour
print(hour)

# enviar sempre as 8h da manhã
if hour == 8:
    with open('quotes.txt', 'r') as file:
        list_quotes = file.read().split('\n')

    choice = random.choice(list_quotes)
    text = f"Subject:For your day...\n\n{choice}"
    to = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to, msg=text)



# qtadbhgyshoqpcyo
# date_my_birth = dt.datetime(year=1995, month=5, day=12, hour=18)
# print(date_my_birth)

