import pymysql
from __main__ import con

# pass me username of the person logged in and whether
# that person is a Teacher (type = T) or student (type = S)

# print course details and preferred textbooks


def sel1():
    with con.cursor() as cur:
        try:
            username = input("Enter email:")
            name = input("Enter Team Name: ")
            query = '''
            SELECT T.Team_name, T.Course_name, T.Details, TBK.Textbook
            FROM TEAM AS T, TEXTBOOK AS TBK
            WHERE T.Team_name = TBK.Team_name AND 
                                T.Team_name  = {0} AND
                                EXISTS ( SELECT *
                                        FROM MEMBERSHIP AS M
                                        WHERE M.Team_name = {0} AND 
                                        M.Member_id = {1});'''.format(name, username)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("Team Name \t Course Name \t Details \t Textbook")
                for x in result:
                    print("{} \t {} \t {} \t {}".format(
                        x[0], x[1], x[2], x[3]))
            else:
                print("No such team name")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# list members of the team
def sel2():
    with con.cursor() as cur:
        try:
            name = input("Enter Team Name: ")
            query = '''
            SELECT A.First_name, A.Family_name, A.Email_id
            FROM ACCOUNT AS A
            WHERE A.Email_id IN (   SELECT M.Member_id
                                    FROM MEMBERSHIP AS M
                                    WHERE M.Team_name = {});'''.format(name)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("First Name \t Family Name \t Email ID")
                for x in result:
                    print("{} \t {} \t {}".format(x[0], x[1], x[2]))
            else:
                print("No such team name")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# list members of a meeting
def sel3():
    with con.cursor() as cur:
        try:
            username = input("Enter email: ")
            team_name = input("Enter Team Name: ")
            channel_name = input("Enter Channel Name: ")
            instructor = input("Enter Instructor EmailID: ")
            verify = '''
            SELECT *
            FROM MEMBERSHIP AS M
            WHERE M.Team_name = {0} AND 
            M.Member_id = {1};'''.format(team_name, username)

            row_cnt = cur.execute(verify)

            if row_cnt > 0:
                query = '''
                SELECT A.First_name, A.Family_name, A.Email_id
                FROM ACCOUNT AS A
                WHERE A.Email_id = {2} OR 
                A.Email_id IN ( SELECT S.Email_id
                                FROM STUDENT AS S
                                WHERE S.Roll_no IN ( SELECT AT.SRoll_no
                                                    FROM ATTENDS AS AT
                                                    WHERE AT.Team_name = {0} AND
                                                        AT.Channel_name = {1} AND
                                                        AT.Org_id = {2}));'''.format(team_name, channel_name, instructor)
                cnt = cur.execute(query)
                if cnt > 0:
                    result = cur.fetchall()
                    print("First Name \t Family Name \t Email ID")
                    for x in result:
                        print("{} \t {} \t {}".format(x[0], x[1], x[2]))
                else:
                    print("Nobody attended the meeting")

            else:
                print("No such team name")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# find marks per question of a quiz
def sel4():
    with con.cursor() as cur:
        try:
            username = input("Enter email: ")
            course_name = input("Enter Course Name: ")
            qno = input("Enter Quiz Number: ")
            cur.execute(
                "SELECT Roll_no FROM STUDENT WHERE Email_id = {};".format(username))
            result = cur.fetchall()
            SRoll_no = result[0][0]

            query = '''
            SELECT QS.Q_id, QS.Marks
            FROM QUESANS AS QS
            WHERE (QS.Q_id, QS.Answer) IN ( SELECT R.Q_id, R.Answer
                                            FROM RESPONSE AS R
                                            WHERE R.Quiz_no = {} AND
                                            R.Course_name = {} AND
                                            R.SRoll_no = {});'''.format(qno, course_name, SRoll_no)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("QuestionID \t Marks")
                for x in result:
                    print("{} \t {}".format(x[0], x[1]))
            else:
                print("No questions answered in the quiz")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# details of all students in a batch
def proj1():
    with con.cursor() as cur:
        try:
            batch = input("Enter Batch: ")
            query = '''
            SELECT A.Email_id, A.First_name, A.Family_name, A.Mobile, A.Sex
            FROM ACCOUNT AS A
            WHERE A.Email_id IN ( SELECT S.Email_id
                                    FROM STUDENT AS S
                                    WHERE S.Batch = {});'''.format(batch)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("EmailID \t First Name \t Family Name \t Mobile \t Sex")
                for x in result:
                    print("{} \t {} \t {} \t {} \t {}".format(
                        x[0], x[1], x[2], x[3], x[4]))
            else:
                print("No student in the batch")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# top 10 scoring students in a batch
def proj2():
    with con.cursor() as cur:
        try:
            batch = input("Enter Batch: ")
            query = '''
            SELECT QR.SRoll_no, AVG(QR.Total_marks)
            FROM QUIZRESULT AS QR
            WHERE QR.SRoll_no IN (SELECT S.SRoll_no
                                    FROM STUDENTS AS S
                                    WHERE S.Batch = {})
            GROUP BY SRoll_no
            ORDER BY AVG(QR.Total_marks) DESC;'''.format(batch)
            cnt = cur.execute(query)
            if cnt > 0:
                print("Roll Number \t SGPA")
                for _ in range(0, 10, 1):
                    result = cur.fetchone()
                    if result is None:
                        break
                    else:
                        print("{} \t {}".format(
                            result[0], max((result[1] + 5) / 10, 10)))

            else:
                print("No student in the batch")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# average marks of students in quizzes for the course
def agg1():
    with con.cursor() as cur:
        try:
            course = input("Enter Course Name: ")
            query = '''
            SELECT QR.Quiz_no, AVG(QR.Total_marks)
            FROM QUIZRESULT AS QR
            WHERE QR.Course_name = {}
            GROUP BY Quiz_no;'''.format(course)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("Quiz Number \t Average Marks")
                for x in result:
                    print("{} \t {}".format(x[0], x[1]))

            else:
                print("No quizzes in the course yet")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# attendance of the student
def agg2():
    with con.cursor() as cur:
        try:
            username = input("Eneter email: ")
            team_name = input("Enter Team Name: ")
            cur.execute(
                "SELECT SRoll_no FROM STUDENT WHERE Email_id = {};".format(username))
            result = cur.fetchall()
            SRoll_no = result[0][0]
            query = '''
            SELECT SRoll_no, Count(*)
            FROM ATTENDS
            WHERE Team_name = {} AND SRoll_no = {}
            GROUP BY SRoll_no;'''.format(SRoll_no, team_name)
            cnt = cur.execute(query)
            if cnt > 0:
                print("Roll Number \t Number of Meets attended")
                result = cur.fetchall()
                for x in result:
                    print("{} \t {}", x[0], x[1])
            else:
                print("No student in the batch")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)


# search student details
def search(username, type):
    with con.cursor() as cur:
        try:
            st_name = input("Search by Student Name: ")
            query = '''
            SELECT A.Email_id, A.First_name, A.Family_name, A.Mobile, A.Sex
            FROM ACCOUNT AS A
            WHERE A.First_name LIKE {}%;'''.format(st_name)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                for x in result:
                    print(x)
            else:
                print("No student in the batch with such a name")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print(">>>>>>>>>>>>>", e)
