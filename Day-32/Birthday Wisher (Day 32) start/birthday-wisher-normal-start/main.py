##################### Normal Starting Project ######################
# Update the birthdays.csv with your friends & family's details.
# Make sure one of the entries matches today's date for testing purposes. e.g.
# name,email,year,month,day
# YourName,your_own@email.com,today_year,today_month,today_day
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "torus00001@gmail.com"
MY_PASSWORD = "XXXXXXXXXXXXX" #Put your password in it From App Password

# Check if today matches a birthday in the birthdays.csv
# Create a tuple from today's month and day using datetime. e.g.
today = datetime.now()
today_tuple = (today.month, today.day)


# Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")


# Form of dictionary like this {(birthday_month, birthday_day) : data_row}
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


# Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()

        #importand because contents should = contents.replace if not, it won't work.
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{contents}")




