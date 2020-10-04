import pymysql
from db_description import *


def general_get_details(con: pymysql.connections.Connection, cols: str, table: str, cond: str, DEBUG=False):
    #  return list of dicts
    query = f"SELECT {cols} FROM {table} WHERE {cond}"
    if DEBUG:
        print(query)
    with con.cursor() as cur:
        try:
            cur.execute(query)
            if cur.rowcount:
                return list(cur.fetchall())
            else:
                return []
        except Exception as e:
            con.rollback()
            print(f"Failed to get {table} details")
            print(">>>>>>>>>>>>>", e)
            return ERROR_CODE


def get_account_details(con: pymysql.connections.Connection, email: str, DEBUG=False):
    ret = general_get_details(
        con, "*", "ACCOUNT", f"Email_id = {email}", DEBUG)
    if ret == ERROR_CODE or ret == []:
        return ERROR_CODE
    return ret[0]


def get_student_details(con: pymysql.connections.Connection, email: str, DEBUG=False):

    ret = general_get_details(
        con, "*", "STUDENT", "Email_id = {}".format(email), DEBUG)
    if ret == ERROR_CODE or ret == []:
        return ERROR_CODE
    row = {}
    row.update(ret[0])

    ret = get_account_details(con, email, DEBUG)
    if ret == ERROR_CODE:
        return ERROR_CODE
    row.update(ret)

    return row


def get_instructor_details(con: pymysql.connections.Connection, email: str, DEBUG=False):

    ret = general_get_details(con, "*", "INSTRUCTOR",
                              "Email_id = {}".format(email), DEBUG)
    if ret == ERROR_CODE or ret == []:
        return ERROR_CODE
    row = {}
    row.update(ret[0])

    ret = get_account_details(con, email, DEBUG)
    if ret == ERROR_CODE:
        return ERROR_CODE
    row.update(ret)

    ret = general_get_details(con, "Degree", "DEGREE",
                              "Email_id = {}".format(email))
    if ret == ERROR_CODE:
        return ERROR_CODE
    row["Degree"] = [row["Degree"] for row in ret]
    return row


def get_team_details(con: pymysql.connections.Connection, tname: str, DEBUG=False):
    ret = general_get_details(
        con, "*", "TEAM", "Team_name = {}".format(tname), DEBUG)
    if ret == ERROR_CODE or ret == []:
        return ERROR_CODE
    row = {}
    row.update(ret[0])

    ret = general_get_details(
        con, "Textbook", "TEXTBOOK", "Team_name = {}".format(tname), DEBUG)
    if ret == ERROR_CODE:
        return ERROR_CODE
    row["Textbook"] = [row["Textbook"] for row in ret]
    return row


def get_channel_details_from_team(con: pymysql.connections.Connection, tname: str, chname:str, DEBUG=False):
    ret = general_get_details(con, "*", "CHANNEL", "Team")
