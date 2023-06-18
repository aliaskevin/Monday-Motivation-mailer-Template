import datetime as dt
import smtplib
from random import choice
# Email credentials
my_email = "your email id"
passw = "email password"
# Reading Quotes from text file
with open('quotes.txt') as data:
    lines = data.readlines()
quotes = [_.strip('\n') for _ in lines]
# Finding current weekday
now = dt.datetime.now()
day_of_week = now.weekday()    
# Checking if Monday to email
if day_of_week == 0:
    quote_of_day = choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=passw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="youremail@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote_of_day}\n\nRegards\nMe :)"
        )
