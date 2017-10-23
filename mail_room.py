"""."""


import sys
import operator

# first prompt is would you like to send a thank you or create a report.
list_of_donors = []
donation_history = {'kevin': []}
""""leave for user donation history.  keys will the the
                        users' name and values will be a list of donations."""


def main():
    """Function runs once program is called, calls functions based on input."""
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
        main()


def thank_you():
    """Once send thank you is selected, calls functions based on input."""
    name = input("""
Enter the full name of the donator
or enter list to see a list of all donators
or type quit to return to the orignal prompt

""")
    if type(name) == str:
        if name == 'list':
            print_names()
        elif(name) == 'quit':
            main()
        else:
            check_name(name)
            enter_donation_amount(name)
    else:
        print('''
Please enter a name
            ''')
        thank_you()


def print_names():
    """."""
    for name in list_of_donors:
        print(name)
    if not list_of_donors:
        print("""
There are no donors in the system yet

""")
    thank_you()


def check_name(name):
    """."""
    if name not in list_of_donors:
        list_of_donors.append(name)
    if name not in donation_history:
        donation_history[name] = []


def enter_donation_amount(name):
    """Prompt the user for how much was donated, calls approprate function."""
    donation_amount = input("""
Enter the amount of the donation or type quit to return to the orignal prompt

""")
    if donation_amount == 'quit':
        main()
    try:
        donation_amount = float(donation_amount)
    except ValueError:
        print('''
Please enter a valid donation amount

''')
        enter_donation_amount(name)

    add_donation_history(donation_amount, name)


def add_donation_history(amount, name):
    """."""
    print("""
Thank you, {}, for your generous donation of ${}
""".format(name, amount))
    donation_history[name].append(amount)
    main()


def testable_add_donation_history(amount, name):
    """Modify add testing donation history for testing."""
    donation_history[name].append(amount)
    return """Thank you, {}, for your generous donation of ${}
""".format(name, amount)


def create_report():
    """Will print a list of donors sorted by amount donated."""
    donation_information = []
    for person in donation_history:
        name = person
        total_amount_donated = 0
        number_of_donations = 0
        for amount in donation_history[name]:
            total_amount_donated += amount
            number_of_donations += 1
        average_donation = total_amount_donated / number_of_donations
        donation_information.append((name, total_amount_donated,
                                     number_of_donations, average_donation))
    sorted_donations = sorted(donation_information,
                              key=operator.itemgetter(1), reverse=True)
    for person in sorted_donations:
        print('''
Name of donator: {}
Total amount donated: {}
Number of donations: {}
Average donation: {}
'''.format(person[0], person[1], person[2], person[3]))
    main()
