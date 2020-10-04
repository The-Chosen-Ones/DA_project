import pymysql


def delete_account(con, email: str, DEBUG=False):
    query = f"DELETE FROM ACCOUNT WHERE Email_id= {email}"
    if DEBUG:
        print(query)
    with con.cursor() as cur:
        try:
            cur.execute(query)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failed to update marks")
            print(">>>>>>>>>>>>>", e)
            return str(e)
    return "success"
