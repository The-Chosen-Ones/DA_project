def validate_email(email: str) -> bool:
    from re import search
    # regex = r"^ (?=[A-Z0-9][A-Z0-9@._ % +-]{5, 253}$)[A-Z0-9._ % +-]{1, 64}@(?: (?=[A-Z0-9-]{1, 63}\.)[A-Z0-9]+(?: -[A-Z0-9]+) *\.){1, 8}[A-Z]{2, 63}$"
    regex = r"[^@]+@[^@]+\.[^@]+"
    return True if search(regex, email) else False


def validate_text(text: str, sizemin=0, sizemax=80, alnum=False) -> bool:
    return True if type(text) == str and sizemin <= len(text) <= sizemax and (not alnum or text.isalnum()) else False


def check_valid(type: str, val) -> bool:
    return validators[type](val)


validators = {
    "Name": validate_text,
    "First_name": validate_text,
    "Family_name": validate_text,
    "Email_id": validate_email,
    "Password": lambda val: validate_text(val, sizemin=8, sizemax=15, alnum=True),
    "Mobile": lambda x: type(x) == int and len(str(x)) == 10,
    "Sex": lambda x: x in {'M', 'F', 'O'},
    "Address": validate_text,
    "Degree": validate_text,
    "Roll_no": lambda x: type(x) == int and len(str(x)) == 10,
    "Batch": lambda val: validate_text(val, sizemax=10),
    "cgpa": lambda x: 0 <= x <= 10,
    "Team_name": validate_text,
    "Course_name": lambda x: validate_text(x, sizemax=30),
    "Details": lambda x: validate_text(x, sizemax=100),
    "Textbook": lambda x: validate_text(x, sizemax=30),
    "Channel_name": validate_text,
    "Time": lambda x: True,
    "Quiz_no": lambda x: type(x) == int and x < 1e9,
    "No_of_qn": lambda x: type(x) == int and x < 1e9,
    "Qn_text": lambda x: validate_text(x, sizemax=1000),
    "Q_id": lambda x: type(x) == int and x < 1e9,
    "Answer": lambda x: validate_text(x, sizemax=1000),
    "Marks": lambda x: 0 <= x <= 10,
    "Percentage_marks": lambda x: 0 <= x <= 100,
}

validators["Sup_id"] = validators["Email_id"]
validators["Org_id"] = validators["Email_id"]
validators["Member_id"] = validators["Email_id"]
validators["Inst_Email_id"] = validators["Email_id"]
validators["Start_time"] = validators["Time"]
validators["End_time"] = validators["Time"]
