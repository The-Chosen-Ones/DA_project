import pymysql
from validation import check_valid
from db_description import SUCCESS_CODE


def update_marks(con, q_id, ans, new_marks, DEBUG=False):
    for attr, val in {"Q_id":  q_id, "Answer": ans, "Marks": new_marks}.items():
        if not check_valid(attr, val):
            return f"error in checking of ({attr} : {val})"

    query = f"UPDATE QUESANS SET Marks = '{new_marks}' WHERE Q_id = '{q_id}' AND Answer = '{ans}'"
    if DEBUG:
        print("query:", query)
    with con.cursor() as cur:
        try:
            cur.execute(query)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failed to update marks")
            print(">>>>>>>>>>>>>", e)
            return str(e)
    return SUCCESS_CODE


def update_address(con, email, old_add, new_add, DEBUG=False):
    for attr, val in {("Email_id",  email), ("Address", old_add), ("Address", new_add)}:
        if not check_valid(attr, val):
            return f"error in checking of ({attr} : {val})"
    query = f"UPDATE ADDRESS SET Address = '{new_add}' WHERE Email_id = '{email}' AND Address= '{old_add}'"
    if DEBUG:
        print("query:", query)

    with con.cursor() as cur:
        try:
            cur.execute(query)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failed to update address")
            print(">>>>>>>>>>>>>", e)
            return str(e)
    return SUCCESS_CODE


def update_mobile(con, email, new_mob, DEBUG=False):
    for attr, val in {"Email_id":  email, "Mobile": new_mob}.items():
        if not check_valid(attr, val):
            return f"error in checking of ({attr} : {val})"
    query = f"UPDATE ACCOUNT SET Mobile = '{new_mob}' WHERE Email_id = '{email}'"
    if DEBUG:
        print("query:", query)

    with con.cursor() as cur:
        try:
            cur.execute(query)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failed to update mobile")
            print(">>>>>>>>>>>>>", e)
            return str(e)
    return SUCCESS_CODE
