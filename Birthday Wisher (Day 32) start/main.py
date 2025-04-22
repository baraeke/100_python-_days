# import smtplib

# my_email ="ifiemi2love@gmail.com"
# my_password = "vctfeuwtenmagfoa"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="eke0211@pg.babcock.edu.ng",
#         msg="Subject: Save my number\n\nThis is my number: 0905566666543")

import smtplib
import datetime as dt
import random

my_email ="ifiemi2love@gmail.com"
my_password = "vctfeuwtenmagfoa"

today_date = dt.datetime(2025, 4, 22) # Represents April 22, 2025
day = today_date.weekday()

with open("quotes.txt", "r") as data_file:
    qoutes = [line for line in data_file]
    msg = random.choice(qoutes)
    if day == 1:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="eke0211@pg.babcock.edu.ng",
                msg=f"Subject: Today's Qoute\n\n{msg}")