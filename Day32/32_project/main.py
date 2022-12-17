import datetime as dt
import pandas
import random
import smtplib

my_email = ""
password = ""

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        msg = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,
                         password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{msg}")

# qtadbhgyshoqpcyo





