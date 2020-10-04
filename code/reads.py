import pymysql
from db_description import *


def get_account_details(con: pymysql.connections.Connection, email: str, DEBUG=False):
    query = "SELECT * FROM ACCOUNT WHERE Email_id = {}".format(email)
    if DEBUG:
        print(query)
    with con.cursor() as cur:
        try:
            cur.execute(query)
            if cur.rowcount:
                return cur.fetchone()
        except Exception as e:
            con.rollback()
            print("Failed to get acc details")
            print(">>>>>>>>>>>>>", e)
            return ERROR_CODE
    return ERROR_CODE


def get_student_details(con: pymysql.connections.Connection, email: str, DEBUG=False):
    query = "SELECT * FROM STUDENT WHERE Email_id = {}".format(email)
    if DEBUG:
        print(query)
    st_row = {}
    with con.cursor() as cur:
        try:
            cur.execute(query)
            if not cur.rowcount:
                return ERROR_CODE
            else:
                st_row = cur.fetchone()
        except Exception as e:
            con.rollback()
            print("Failed to get student details")
            print(">>>>>>>>>>>>>", e)
            return ERROR_CODE

    acc_row = get_account_details(con, email, DEBUG)
    if acc_row == ERROR_CODE:
        return ERROR_CODE
    row = {}
    row.update(st_row)
    row.update(acc_row)
    return row


def get_instructor_details(con: pymysql.connections.Connection, email: str, DEBUG=False):
    query = "SELECT * FROM INSTRUCTOR WHERE Email_id = {}".format(email)
    if DEBUG:
        print(query)
    inst_row = {}
    with con.cursor() as cur:
        try:
            cur.execute(query)
            if cur.rowcount:
                inst_row = cur.fetchone()
            else:
                return ERROR_CODE
        except Exception as e:
            con.rollback()
            print("Failed to get instructor details")
            print(">>>>>>>>>>>>>", e)
            return ERROR_CODE

    acc_row = get_account_details(con, email, DEBUG)
    if acc_row == ERROR_CODE:
        return ERROR_CODE
    row = {}
    row.update(inst_row)
    row.update(acc_row)
    query = f"SELECT Degree FROM DEGREE WHERE Email_id = {email}"
    row["DEGREE"] = []
    if DEBUG:
        print(query)
    with con.cursor() as cur:
        try:
            cur.execute(query)
            if cur.rowcount:
                row["DEGREE"] = list(cur.fetchall().values())
        except Exception as e:
            print(">>>>>>>>>>>>>", e)
    return row
