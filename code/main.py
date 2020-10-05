import subprocess as sp
import pymysql
import pymysql.cursors
from insertions import *
from updates import *
from deletions import *
from functional import *
from analysis import *


def createAccount():
    row = {}
    print("Enter new Account details: ")
    name = (input("Name (Fname Lname): ")).split(' ')
    row['First_name'] = name[0]
    row['Family_name'] = name[1]
    row['Email_id'] = input("Email_id: ")
    row['Password'] = input("Password: ")
    row['Mobile'] = input("Mobile_no: ")
    row['Sex'] = input("Sex: ")

    row['Address'] = []
    n = int(input("Number of Addresses: "))
    for i in range(n):
        row['Address'].append(input("Address {}: ".format(i + 1)))

    subclass = input("Are you a INSTRUCTOR or STUDENT ? : ")

    if subclass == "STUDENT":
        row['Roll_no'] = int(input("Roll_no: "))
        row['Batch'] = input("Batch: ")
    elif subclass == "INSTRUCTOR":
        row['Degree'] = []
        n = int(input("Number of Degrees: "))
        for i in range(n):
            row['Degree'].append(input("Degree {}: ".format(i + 1)))

    print(insert_account(con, row, subclass, True))


def createTeam():
    row = {}
    print("Enter new Team details: ")
    row['Team_name'] = input("Team Name: ")
    row['Course_name'] = input("Course Name: ")
    row['Details'] = input("Details: ")
    row['Admin_id'] = input("Admin Email_id: ")

    row['Textbook'] = []
    n = int(input("Number of Textbooks: "))
    for i in range(n):
        row['Textbook'].append(input("Textbook {}: ".format(i + 1)))

    print(insert_team(con, row, True))


def createChannel():
    row = {}
    print("Enter Channel details: ")
    row['Team_name'] = input("Team Name")
    row['Channel_name'] = input('Channel Name')

    print(insert_channel(con, row))


def addMeeting():
    row = {}
    print("Enter Meeting details: ")
    row['Team_name'] = input("Team Name: ")
    row['Channel_name'] = input("Channel Name: ")
    row['Org_id'] = input("Organiser Email_id: ")
    row['Start_time'] = input("Start Time (YYYY-MM-DD HH:MM:SS): ")
    row['End_time'] = input("End Time (YYYY-MM-DD HH:MM:SS): ")

    print(insert_meeting(con, row, True))


def addMember():
    row = {}
    print("Enter Details: ")
    row['Team_name'] = input("Team Name: ")
    row['Member_id'] = input("Member Email_id: ")

    print(insert_membership(con, row, True))


def addAttendee():
    row = {}
    print("Enter Details: ")
    row['Team_name'] = input("Team Name: ")
    row['Channel_name'] = input("Channel Name: ")
    row['Org_id'] = input("Organiser Email_id: ")
    row['SRoll_no'] = int(input("Attendee Roll_no: "))

    print(insert_attends(con, row, True))


def addQuestion():
    row = {}
    print("Enter Question Details: ")
    row['Q_id'] = int(input("Q_id: "))
    row['Qn_text'] = input("Question Text: ")
    row['Course_name'] = input("Course Name: ")

    print(insert_question(con, row, True))


def addAnswer():
    row = {}
    print("Enter Answer Details")
    row['Q_id'] = int(input("Q_id: "))
    row['Answer'] = input("Answer: ")
    row['Marks'] = int(input("Marks: "))

    print(insert_quesans(con, row, True))


def addQuiz():
    row = {}
    print("Enter Quiz Details: ")
    row['Quiz_no'] = int(input("Quiz_no: "))
    row['Course_name'] = input("Course Name: ")
    row['No_of_qn'] = int(input("Number of Questions: "))

    print(insert_quiz(con, row, True))


def addQuizStudent():
    row = {}
    print("Enter Details: ")
    row['SRoll_no'] = int(input("Student Roll_no: "))
    row['Quiz_no'] = int(input("Quiz_no: "))
    row['Course_name'] = input("Course Name: ")

    print(insert_gives(con, row, True))


def addResponse():
    row = {}
    print("Enter Response Details: ")
    row['Quiz_no'] = int(input("Quiz_no: "))
    row['Course_name'] = input("Course Name: ")
    row['Q_id'] = int(input("Q_id: "))
    row['SRoll_no'] = int(input("Student Roll_no: "))
    row['Inst_Email_id'] = input("Instructor Email_id: ")
    row['Answer'] = input("Answer: ")

    print(insert_response(con, row, True))


def updateMarks():
    print("Enter Details: ")
    q_id = int(input("Q_id: "))
    ans = input("Answer: ")
    new_marks = int(input("New Marks: "))

    print(update_marks(con, q_id, ans, new_marks, True))


def updateAddress():
    print("Enter Details: ")
    email = input("Email_id: ")
    old_add = input("Old Address: ")
    new_add = input("New Address: ")

    print(update_address(con, email, old_add, new_add, True))


def updateMobile():
    print("Enter Details: ")
    email = input("Email_id: ")
    new_mob = input("New Mobile Number: ")

    print(update_mobile(con, email, new_mob, True))


def deleteAccount():
    print("Enter Details: ")
    email = input("Email_id: ")

    print(delete_account(con, email, True))


def dispatch(ch):
    try:
        if(ch == 1):
            createAccount()
        elif(ch == 2):
            createTeam()
        elif(ch == 3):
            addMember()
        elif(ch == 4):
            createChannel()
        elif(ch == 5):
            addMeeting()
        elif(ch == 6):
            addAttendee()
        elif(ch == 7):
            addQuestion()
        elif(ch == 8):
            addAnswer()
        elif(ch == 9):
            addQuiz()
        elif(ch == 10):
            addQuizStudent()
        elif(ch == 11):
            addResponse()
        elif(ch == 12):
            updateMarks()
        elif(ch == 13):
            updateAddress()
        elif(ch == 14):
            updateMobile()
        elif(ch == 15):
            deleteAccount()
        elif(ch == 16):
            sel1(con)
        elif(ch == 17):
            sel2(con)
        elif(ch == 18):
            sel3(con)
        elif(ch == 19):
            sel4(con)
        elif(ch == 20):
            proj1(con)
        elif(ch == 21):
            proj2(con)
        elif(ch == 22):
            agg1(con)
        elif(ch == 23):
            agg2(con)
        elif(ch == 24):
            search(con)
        elif(ch == 25):
            analysis1(con)
        elif(ch == 26):
            analysis2(con)
        elif(ch == 27):
            analysis3(con)
        else:
            print("Invalid Option")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        tmp = input("Enter any key to CONTINUE>")


con = []
while(1):
    tmp = sp.call('clear', shell=True)

    username = "pranjai"
    password = "Pranjai@2606"
    port = input("Enter port num(leave blank for default):")
    if port == "":
        port = 3306
    else:
        port = int(port)

    try:
        con
        con = pymysql.connect(host='localhost', user=username, password=password, port=port,
                              db='DfOEP', cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        while(1):
            tmp = sp.call('clear', shell=True)
            print("0. Exit")
            print("1. Create a new Account.")
            print("2. Create a new Team.")
            print("3. Add Member to a Team.")
            print("4. Create a new Channel.")
            print("5. Add a new Meeting.")
            print("6. Add Attendee for a Meeting.")
            print("7. Add a Question.")
            print("8. Add Answer and Marks for a Question")
            print("9. Add a Quiz.")
            print("10. Add Student who gives a Quiz.")
            print("11. Add Response for a Quiz.")
            print("12. Update Marks of a Question.")
            print("13. Update Address of an Account.")
            print("14. Update Mobile Number of an Account.")
            print("15. Delete an Account.")
            print("16. Print Course Details and preferred textbooks of a Team.")
            print("17. List Members of a Team.")
            print("18. List Members of a Meeting.")
            print("19. Find Marks per Question of a Quiz.")
            print("20. Details of all Students in a Batch.")
            print("21 Top 10 scoring Students in a Batch.")
            print("22. Average Marks of Students in Quizzes for the Course.")
            print("23. Attendance of a Student")
            print("24. Search Student Details.")
            print("25. Measure effectiveness of online teaching.")
            print("26. Student Report Card.")
            print("27. Relation between Student's Marks and Attendance.")

            ch = int(input("Enter choice > "))
            tmp = sp.call('clear', shell=True)
            if ch == 0:
                break
            else:
                dispatch(ch)
                tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        break
