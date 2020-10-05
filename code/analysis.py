import pymysql
from __main__ import con


# Measure effectiveness of online teaching
def analysis1():
    with con.cursor() as cur:
        try:
            batch = input("Enter Batch: ")
            query = '''
            SELECT QR.SRoll_no, AVG(QR.Total_marks)
            FROM QUIZRESULT AS QR
            WHERE QR.SRoll_no IN (SELECT S.SRoll_no
                                    FROM STUDENTS AS S
                                    WHERE S.Batch = {})
            GROUP BY SRoll_no;'''.format(batch)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                # list no_of_st = [below 50, 50-60, 60-70, 70-80, 80-90, 90-100]
                no_of_st = [0, 0, 0, 0, 0, 0]
                for x in result:
                    if x[1] < 50:
                        no_of_st[0] += 1
                    elif x[1] < 60:
                        no_of_st[1] += 1
                    elif x[1] < 70:
                        no_of_st[2] += 1
                    elif x[1] < 80:
                        no_of_st[3] += 1
                    elif x[1] < 90:
                        no_of_st[4] += 1
                    else:
                        no_of_st[5] += 1
                print("No of students below 50:              {}".format(
                    no_of_st[0]))
                print("No of students above 50 but below 60: {}".format(
                    no_of_st[1]))
                print("No of students above 60 but below 70: {}".format(
                    no_of_st[2]))
                print("No of students above 70 but below 80: {}".format(
                    no_of_st[3]))
                print("No of students above 80 but below 90: {}".format(
                    no_of_st[4]))
                print("No of students above 90             : {}".format(
                    no_of_st[5]))

            else:
                print("No student in the batch")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# Student Report Card
def analysis2():
    with con.cursor() as cur:
        try:
            username = input("Enter Email:")
            cur.execute(
                "SELECT Roll_no FROM STUDENT WHERE Email_id = {};".format(username))
            result = cur.fetchall()
            SRoll_no = result[0][0]

            query = '''
            SELECT QR.SRoll_no, QR.Course_name QR.AVG(QR.Total_marks)
            FROM QUIZRESULT AS QR
            WHERE QR.SRoll_no = {}
            GROUP BY QR.SRoll_no, QR.Course_name;'''.format(SRoll_no)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                total = 0
                print("Roll Number: ".format(SRoll_no))
                print("Course Name \t Percentage")
                count = 0
                for x in result:
                    total += x[2]
                    print("{} \t {}".format(x[1], x[2]))
                    count += 1

                print("SGPA = {}".format(max((total/count + 5) / 10, 10)))

            else:
                print("No student in the batch")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# Relation between student's marks and attendance
def analysis3():
    with con.cursor() as cur:
        try:
            course = input("Type Course Name: ")
            cur.execute(
                "SELECT Team_name FROM TEAM WHERE Course_name = {};".format(course))
            result = cur.fetchall()
            team = result[0][0]
            query = '''
            SELECT SRoll_no, Count(*)
            FROM ATTENDS
            WHERE Team_name = {}
            GROUP BY SRoll_no
            ORDER BY COUNT(*) DESC;'''.format(team)
            cnt = cur.execute(query)
            if cnt > 0:
                print("Top 20 most attending students")
                print("Roll Number \t Attendance")
                result = cur.fetchall()
                count = 1
                for x in result:
                    if count > 20:
                        break
                    else:
                        print("{} \t {}".format(x[0], x[1]))
                print("20 least attending students")
                print("Roll Number \t Attendance")
                result = cur.fetchall()
                count = 1
                for x in reversed(result):
                    if count > 20:
                        break
                    else:
                        print("{} \t {}".format(x[0], x[1]))

            else:
                print("No student in the batch")

            query = '''
            SELECT SRoll_no, AVG(Total_marks)
            FROM QUIZRESULT
            WHERE Course_name = {}
            GROUP BY SRoll_no
            ORDER BY AVG(Total_marks) DESC;'''.format(course)
            cnt = cur.execute(query)
            if cnt > 0:
                print("Top 20 most scoring students")
                print("Roll Number \t Percentage")
                result = cur.fetchall()
                count = 1
                for x in result:
                    if count > 20:
                        break
                    else:
                        print("{} \t {}".format(x[0], x[1]))
                print("20 least scoring students")
                print("Roll Number \t Percentage")
                result = cur.fetchall()
                count = 1
                for x in reversed(result):
                    if count > 20:
                        break
                    else:
                        print("{} \t {}".format(x[0], x[1]))

            else:
                print("No student in the batch")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)
