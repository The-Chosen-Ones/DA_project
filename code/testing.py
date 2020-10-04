import pymysql

from insertions import *

con = pymysql.connect(host='127.0.0.1',
                      user="root",
                      password="hihi",
                      db="DfOEP",
                      port=5005,
                      cursorclass=pymysql.cursors.DictCursor)

row = {
    "Email_id": "prof@mail.com",
    "First_name": "pro",
    "Family_name": "f",
    "Password": "password",
    "Mobile": "1023456789",
    "Sex": "M",
    "Address": ["lab 332323"],
    "Degree": ["mtech", "btech", "phd"],
    "Sup_id": "prof@mail.com"
}

print(insert_acccount(con, row, "INSTRUCTOR", True))
