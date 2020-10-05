import pymysql
from validation import check_valid
from db_description import *


def general_insertion(con, table: str, row: dict, DEBUG=False):
    for i in row.keys():
        if not check_valid(i, row[i]):
            return "error in {} validation".format(i)

    with con.cursor() as cur:
        query = "INSERT INTO {}(".format(table)
        for attr in Attributes[table]:
            query += "{},".format(attr)
        query = query[:-1] + ") VALUES("
        for attr in Attributes[table]:
            query += "\"{}\",".format(row[attr])
        query = query[:-1] + ")"
        if DEBUG:
            print(query)
        try:
            cur.execute(query)
            con.commit()
            return SUCCESS_CODE
        except Exception as e:
            con.rollback()
            print("Failed to insert into {}".format(table))
            print(">>>>>>>>>>>>>", e)
            return str(e)


def insert_account(con, row: dict, subclass, DEBUG=False):
    if subclass not in {"INSTRUCTOR", "STUDENT"}:
        return "error in subclass"

    for tb in ["ACCOUNT", subclass]:
        tmp_row = {x: row[x] for x in Attributes[tb]}
        ret = general_insertion(con, tb, tmp_row, DEBUG)
        if ret != SUCCESS_CODE:
            return ret

    for add in row["Address"]:
        tmp_row = {
            "Email_id": row["Email_id"],
            "Address": add,
        }
        ret = general_insertion(con, "ADDRESS", tmp_row, DEBUG)
        if ret != SUCCESS_CODE:
            return ret
    if subclass == "INSTRUCTOR":
        # ins will have multi degrees
        for deg in row["Degree"]:
            tmp_row = {
                "Email_id": row["Email_id"],
                "Degree": deg
            }
            ret = general_insertion(con, "DEGREE", tmp_row, DEBUG)
            if ret != SUCCESS_CODE:
                return ret

    return SUCCESS_CODE


def insert_team(con, row: dict, DEBUG=False):
    team_row = {x: row[x] for x in Attributes["TEAM"]}
    ret = general_insertion(con, "TEAM", team_row, DEBUG)
    if ret != SUCCESS_CODE:
        return ret
    for tb in row["Textbook"]:
        tmp_row = {
            "Team_name": row["Team_name"],
            "Textbook": tb
        }
        ret = general_insertion(con, "TEXTBOOK", tmp_row, DEBUG)
        if ret != SUCCESS_CODE:
            return ret
    return SUCCESS_CODE


def insert_response(con, row: dict, DEBUG=False):
    for tb in {"RESPONSE", "QUESANS"}:
        resp_row = {x: row[x] for x in Attributes[tb]}
        ret = general_insertion(con, tb, resp_row, DEBUG)
        if ret != SUCCESS_CODE:
            return ret
    return SUCCESS_CODE


def insert_channel(con, row: dict, DEBUG=False):
    return general_insertion(con, "CHANNEL", row, DEBUG)


def insert_meeting(con, row: dict, DEBUG=False):
    return general_insertion(con, "MEETING", row, DEBUG)


def insert_attends(con, row: dict, DEBUG=False):
    return general_insertion(con, "ATTENDS", row, DEBUG)


def insert_membership(con, row: dict, DEBUG=False):
    return general_insertion(con, "MEMBERSHIP", row,  DEBUG)


def insert_gives(con, row: dict, DEBUG=False):
    return general_insertion(con, "GIVES", row, DEBUG)


def insert_quiz(con, row: dict, DEBUG=False):
    return general_insertion(con, "QUIZ", row, DEBUG)


def insert_question(con, row: dict, DEBUG=False):
    return general_insertion(con, "QUESTION", row, DEBUG)


def insert_quesans(con, row: dict, DEBUG=False):
    return general_insertion(con, "QUESANS", row, DEBUG)


def insert_address(con, row: dict, DEBUG=False):
    return general_insertion(con, "ADDRESS", row, DEBUG)
