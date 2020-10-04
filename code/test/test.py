from validation import validate_email, check_valid


def test_email_valid():
    assert(validate_email('vedansh@gmail.com'))
    assert(validate_email('vedansh@iiit.ac.in'))
    assert(validate_email('vedansh.mittal@gmail.com'))
    assert(validate_email('vedansh.mittal.0.1@iiit.ac.in'))
    assert(not validate_email('vedanshgmail.com'))
    # assert(not validate_email('vedansh@gma@il.com'))
    assert(not validate_email('vedansh@gmail.'))
    print("emails test passed")


def test_gen_valid():
    assert(check_valid("Sex", 'M'))
    assert(check_valid("Mobile_number", 9123456780))
    assert(check_valid("First_name", "Joe"))
    assert(check_valid("Password", "hiehose08424"))
    assert(check_valid("Email_id", "hi@bye.com"))
    assert(not check_valid("Email_id", "hibye.com"))
    print("Gen validn. tests passed")


test_email_valid()
test_gen_valid()
