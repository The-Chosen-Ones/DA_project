Attributes = {}
SUCCESS_CODE = "success"
ERROR_CODE = "error"

Attributes["ACCOUNT"] = [
    "Email_id",
    "First_name",
    "Family_name",
    "Password",
    "Mobile",
    "Sex",
]

Attributes["ADDRESS"] = [
    "Email_id",
    "Address"
]

Attributes["INSTRUCTOR"] = [
    "Email_id",
    "Sup_id",
]

Attributes["DEGREE"] = [
    "Email_id",
    "Degree"
]

Attributes["STUDENT"] = [
    "Email_id",
    "Roll_no",
    "Batch"
]

Attributes["TEAM"] = [
    "Team_name",
    "Course_name",
    "Details",
    "Admin_id"
]

Attributes["TEXTBOOK"] = [
    "Team_name",
    "Textbook"
]

Attributes["CHANNEL"] = [
    "Team_name",
    "Channel_name",
]

Attributes["MEETING"] = [
    "Team_name",
    "Channel_name",
    "Org_id",
    "Start_time",
    "End_time",
]

Attributes["ATTENDS"] = [
    "Team_name",
    "Channel_name",
    "Org_id",
    "SRoll_no",
    "Start_time",
]

Attributes["MEMBERSHIP"] = [
    "Team_name",
    "Member_id",
]

Attributes["GIVES"] = [
    "SRoll_no",
    "Quiz_no",
    "Course_name"
]

Attributes["QUIZ"] = [
    "Quiz_no",
    "Course_name",
    "No_of_qn"
]

Attributes["QUESANS"] = [
    "Q_id",
    "Answer",
    "Marks"
]

Attributes["RESPONSE"] = [
    "Quiz_no",
    "Course_name",
    "Q_id",
    "SRoll_no",
    "Inst_Email_id",
    "Answer"
]

Attributes["QUESTION"] = [
    "Q_id",
    "Qn_text",
    "Course_name"
]
