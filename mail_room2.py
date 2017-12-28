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
    donation_history[name][0] = name
    donation_history[name][1] += float(amount)
    donation_history[name][2] += 1
    donation_history[name][3] = donation_history[name][1] / donation_history[name][2]
