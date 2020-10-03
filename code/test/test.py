from validation import validate_email, check_validate


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
    assert(check_validate("Sex", 'M'))
    assert(check_validate("Mobile_number", 9123456780))
    assert(check_validate("First_name", "Joe"))
    assert(check_validate("Password", "hiehose08424"))
    assert(check_validate("Email_id", "hi@bye.com"))
    assert(not check_validate("Email_id", "hibye.com"))
    print("Gen validn. tests passed")


test_email_valid()
test_gen_valid()
