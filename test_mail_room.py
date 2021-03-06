"""Test file for the mail room module."""
import mail_room2


def test_list_donors_no_donors():
    """Should return string stating that there are no donors."""
    assert mail_room2.list_donors() == "There are currently no donors"


def test_create_report_no_donors():
    """Should reflect that there are no donors in report."""
    assert mail_room2.create_report() == "There are currently no donors"


def test_add_donor():
    """Test adding a donor."""
    mail_room2.add_donor('John')
    assert 'John' in mail_room2.list_of_donors


def test_add_donor_already_in_list():
    """Test adding a donor already in list doesn't re add them."""
    mail_room2.add_donor('Steve')
    assert len(mail_room2.list_of_donors) == 2
    mail_room2.add_donor("Steve")
    assert len(mail_room2.list_of_donors) == 2


def test_donation_history_updates_with_new_user():
    """If a new user is added, their donation history should be an empty dict."""
    assert mail_room2.donation_history["Steve"] == ["Steve", 0, 0, 0]
    assert mail_room2.donation_history["John"] == ["John", 0, 0, 0]


def test_verify_amount_correct_string():
    """Return True on convertable string."""
    assert mail_room2.verify_donation('3.6') is True


def test_verify_amount_incorrect_string():
    """Return False on non-convertable string."""
    assert mail_room2.verify_donation('three point six') is False


def test_list_donors_returns_names_of_donors():
    """The names of all donors should be in the reutrn statement."""
    assert "Steve" in mail_room2.list_donors()
    assert "John" in mail_room2.list_donors()


def test_add_donation():
    """Adding a donation should update a users donation history."""
    mail_room2.add_donation("Steve", 100)
    assert mail_room2.donation_history["Steve"][1] == 100
    assert mail_room2.donation_history["Steve"][2] == 1
    assert mail_room2.donation_history["Steve"][3] == 100


def test_add_second_donation_same_user():
    """Adding a donation should update a users donation history."""
    mail_room2.add_donation("Steve", 10)
    assert mail_room2.donation_history["Steve"][1] == 110
    assert mail_room2.donation_history["Steve"][2] == 2
    assert mail_room2.donation_history["Steve"][3] == 55


def test_add_third_donation_new_user():
    """Adding a donation should update a users donation history."""
    mail_room2.add_donation("John", 1)
    assert mail_room2.donation_history["John"][1] == 1
    assert mail_room2.donation_history["John"][2] == 1
    assert mail_room2.donation_history["John"][3] == 1


def test_send_thank_you():
    """Test email is printed correctly."""
    res = mail_room2.thank_you("Bob", '1')
    assert res == "Thank you Bob, for your generous donation of $1"


def test_create_report_two_donors():
    """Test that the donation report is correct with two donors."""
    res = mail_room2.create_report()
    assert res == '\nName of donator: John\nTotal amount donated: 1.0\nNumber of donations: 1\nAverage donation: 1.0\n\nName of donator: Steve\nTotal amount donated: 110.0\nNumber of donations: 2\nAverage donation: 55.0\n'


def test_list_donors_three_donors():
    """Test output of list donors with > 3 donors."""
    mail_room2.add_donor('Tim')
    res = mail_room2.list_donors()
    assert res == 'The current donors are John, Steve, and Tim'


def test_list_donors_one_donor():
    """Test output of list donors with 1 donors."""
    mail_room2.list_of_donors = []
    mail_room2.add_donor("Max")
    res = mail_room2.list_donors()
    assert res == "The only donor is Max"
