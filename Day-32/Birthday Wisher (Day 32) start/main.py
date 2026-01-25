import smtplib
import datetime as dt
import random

MY_EMAIL = "torus00001@gmail.com"
MY_PASSWORD = "XXXXXXXXXXXXXX" # put password in it

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs= "ple030999@gmail.com",
                            msg=f"Subject: Thursday Motivation\n\n{quote}"
                            )




#---------------------------- Learning from Lesson ----------------------------
# import smtplib
#
# my_email = "torus00001@gmail.com"
# #This password from App Password of my_email only
# password = "nccscbozanfdiulo"
#
# # Simple Mail Transfer Protocol (SMTP) is the standard
# # internet protocol for sending and relaying email messages between servers
# connection = smtplib.SMTP("smtp.gmail.com")
# #for gmail: smtp.gmail.com
# #for yahoo: smtp.mail.yahoo.com
#
# # Transport Layer Security (TLS) is a cryptographic
# # protocol that secures internet communications by encrypting data.
# connection.starttls()
# connection.login(user= my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs = "ple030999@gmail.com",
#                     msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()
#
# #--------------------- OR We can also do like this --------------------------
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="ple030999@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")
# #----------------------------------------------------------------------------






#------------------ Working with datetime Module ------------------------------
# import datetime as dt
#
# now = dt.datetime.now()
# print(type(now))
# year = now.year
# print(year)
# month = now.month
# print(month)
# day_of_week = now.weekday()
# print(day_of_week)
#
# if year == 2020:
#     print("Wear a face mask")


# date_of_birth = dt.datetime(year=1999, month=3, day=9, hour=4)
# print(date_of_birth)
#-----------------------------------------------------------------------------