"""Python module to simulate a mail room."""
import sys
import operator

list_of_donors = []
donation_history = {}


def add_donor(name):
    """Add a donor to the list of donors is they are not already in it."""
    if name not in list_of_donors:
        list_of_donors.append(name)
        donation_history[name] = [name, 0, 0, 0]


def verify_donation(amount):
    """Verify that a donation, entered as a string, can be converted to a float."""
    try:
        float(amount)
        return True
    except ValueError:
        return False


def list_donors():
    """Return the names of all of the donors."""
    if list_of_donors:
        string_start = "The current donors are "
        if len(list_of_donors) == 1:
            return 'The only donor is ' + list_of_donors[0]
        elif len(list_of_donors) == 2:
            return 'The current donors are ' + list_of_donors[0] + ' and ' + list_of_donors[1]
        elif len(list_of_donors) > 2:
            for idx, donor in enumerate(list_of_donors):
                if idx < len(list_of_donors - 1):
                    string_start += (donor + ', ')
                else:
                    string_start += ('and ' + donor)
            return string_start
    else:
        return "There are currently no donors"


def add_donation(name, amount):
    """Add a donation to the donation history."""
    donation_history[name][1] += float(amount)
    donation_history[name][2] += 1
    donation_history[name][3] = donation_history[name][1] / donation_history[name][2]


def mail_room():
    """Run the mail room simulation."""
    reply = input("""
Would you like to send a thank you or create a report?
Enter 1 to send a thank you
Enter 2 to create a report
Enter 3 to quit this script

""")
    if reply == '1':
        thank_you()
    elif reply == '2':
        create_report()
    elif reply == '3':
        sys.exit()
    else:
        print('''
Bad input! See console for acceptable responses
''')
        mail_room()


def thank_you(name, amount):
    """Print out a thank you email for a donation."""
    return "Thank you " + name + ", for your generous donation of $" + amount


def create_report():
    """Crate a report of all donations."""
    pass
