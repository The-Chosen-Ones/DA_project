import pymysql


# list all accounts in the database
def show1(con):
    with con.cursor() as cur:
        try:
            query = '''
            SELECT *
            FROM ACCOUNT;'''
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("{:<16} \t {:<24} \t {:<24} \t {:<10} \t {:<10} \n"
                      "".format('Email_id', 'First_name', 'Family_name', 'Mobile',  'Sex'))
                for x in result:
                    print("{:<16} \t {:<24} \t {:<24} \t {:<10} \t {:<10}"
                          "".format(x['Email_id'], x['First_name'], x['Family_name'], x['Mobile'],  x['Sex']))
            else:
                print("No accounts")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print("{} \n {}".format(e.args[0], e.args[1]))


# address of an account
def show2(con):
    with con.cursor() as cur:
        try:
            email = input("Enter Email address of account: ")
            query = '''
            SELECT Email_id, Address
            FROM ADDRESS
            WHERE Email_id = '{}';'''.format(email)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("Email_id \t Addresses")
                for x in result:
                    print("{:<10} \t {:<10}".format(
                        x['Email_id'], x['Address']))
            else:
                print("No address")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print("{} \n {}".format(e.args[0], e.args[1]))


# list all students in the database
def show3(con):
    with con.cursor() as cur:
        try:
            query = '''
            SELECT *
            FROM STUDENT;'''
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("{:<20} \t {:<10} \t {:<10}\n".format(
                    'Email_id', 'Roll_no', 'Batch'))
                for x in result:
                    print("{:<20} \t {:<10} \t {:<10}".format(
                        x['Email_id'], x['Roll_no'], x['Batch']))
            else:
                print("No student")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print("{} \n {}".format(e.args[0], e.args[1]))


# list all instructors in the database
def show4(con):
    with con.cursor() as cur:
        try:
            query = '''
            SELECT *
            FROM INSTRUCTOR;'''
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("{:<20} \t {:<10}".format(
                    'Email_id', 'Sup_id'))
                for x in result:
                    print("{:<20} \t {:<10}".format(
                        x['Email_id'], x['Sup_id']))
            else:
                print("No instructor")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print("{} \n {}".format(e.args[0], e.args[1]))


# degrees of an instructor
def show5(con):
    with con.cursor() as cur:
        try:
            email = input("Enter Email ID of instructor: ")
            query = '''
            SELECT Email_id, Degree
            FROM DEGREE
            WHERE Email_id = '{}';'''.format(email)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("{:<20} \t {:<10}\n".format(
                    'Email_id', 'Degree'))
                for x in result:
                    print("{:<20} \t {:<10}".format(
                        x['Email_id'], x['Degree']))
            else:
                print("No degrees")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print("{} \n {}".format(e.args[0], e.args[1]))


# list all teams an account is part of
def show6(con):
    with con.cursor() as cur:
        try:
            email = input("Enter Email id: ")
            query = '''
            SELECT Team_name
            FROM MEMBERSHIP
            WHERE Member_id = '{}';'''.format(email)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("Team Names")
                for x in result:
                    print("{}".format(x['Team_name']))
            else:
                print("No teams")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print("{} \n {}".format(e.args[0], e.args[1]))


# list all channels in a team
def show7(con):
    with con.cursor() as cur:
        try:
            team = input("Enter Team Name: ")
            query = '''
            SELECT Channel_name
            FROM CHANNEL
            WHERE Team_name = '{}';'''.format(team)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("Channel Names")
                for x in result:
                    print("{}".format(x['Channel_name']))
            else:
                print("No teams")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print("{} \n {}".format(e.args[0], e.args[1]))


# list all teams in the database
def show8(con):
    with con.cursor() as cur:
        try:
            query = '''
            SELECT *
            FROM TEAM;'''
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("{:<20} \t {:<20} \t {:<10}\n".format(
                    'Team_name', 'Course_name', 'Admin_id'))
                for x in result:
                    print("{:<20} \t {:<20} \t {:<10}".format(
                        x['Team_name'], x['Course_name'], x['Admin_id']))
            else:
                print("No teams")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print("{} \n {}".format(e.args[0], e.args[1]))


# list all quizzes in a course
def show9(con):
    with con.cursor() as cur:
        try:
            course = input("Enter Course Name: ")
            query = '''
            SELECT Quiz_no, No_of_qn
            FROM QUIZ
            WHERE Course_name = '{}';'''.format(course)
            cnt = cur.execute(query)
            if cnt > 0:
                result = cur.fetchall()
                print("Quiz No \t Number of Questions")
                for x in result:
                    print("{:<10} \t {:<10}".format(
                        x['Quiz_no'], x['No_of_qn']))
            else:
                print("No quizzes")

        except Exception as e:
            con.rollback()
            print("Query failed")
            print("{} \n {}".format(e.args[0], e.args[1]))
