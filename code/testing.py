import pymysql

from insertions import *

con = pymysql.connect(host='127.0.0.1',
                      user="root",
                      password="hihi",
                      db="DfOEP",
                      port=5005,
                      cursorclass=pymysql.cursors.DictCursor)

# row = {
#     "Email_id": "prof@mail.com",
#     "First_name": "pro",
#     "Family_name": "f",
#     "Password": "password",
#     "Mobile": "1023456789",
#     "Sex": "M",
#     "Address": ["lab 332323"],
#     "Degree": ["mtech", "btech", "phd"],
#     "Sup_id": "prof@mail.com"
# }

row = {
    "Team_name": "Ateam",
    "Course_name": "Da2020",
    "Details": "hiihhii",
    "Admin_id": "prof@mail.com",
    "Textbook": ["book1", "book2"]
}

print(insert_team(con, row, True))
