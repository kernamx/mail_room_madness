"""."""


prompts_and_responses = {
    "Would you like to send a thank you or create a repot?":
    ['thank', 'report', 'quit'],
    "Enter your name":
    [""]
}
# first prompt is would you like to send a thank you or create a report.
list_of_donors = []
donation_history = {}
""""leave for user donation history.  keys will the the
                        users' name and values will be a list of donations."""


def main():
    """Function runs once program is called, calls functions based on input."""
    import sys
    reply = raw_input("""Would you like to send a thank you or create a repot?
Enter 1 to send a thank you
Enter 2 to create a report
Enter 3 to quit this script""")
    if reply == '1':
        check_name()
    elif reply == '2':
        create_report()
    elif reply == '3':
        sys.exit
    else:
        print("Bad input! See console for acceptable responses")
        main()




def prompt_user(prompt, validator=None):
    """Ask the user to select the opition, calls the function based on.

     the input of the user.
     """
    reply = None
    while reply is None:
        reply = raw_input(prompt)  # asking user
        if validate_input(reply):
            return reply
        else:
            print("bad input")
            get_user_input(prompt, validate=None)


def validate_input(question, response, acceptable_responses):
    """The function is checking if the user input is valid."""
    # if the response is quit return to original prompt.
    # if the response is quit at the original prompt then quit the script.
    if response == good_response:
        return True
    else:
        return False


def response_to_user(input):
    """Base on how the user response to the prompt will call the next function.  
    If input == 'thank you':
    call the thank_you function.  etc..."""


def print_names():
    print('list of names')
    prompt_user(enter_name)


def check_name(name):

    if name_not_in_list:
        list_of_donors.append(name)
    prompt_user(donation_amount)

def add_to_donations(name, amount):

    # then added the amount to donation history .
    # then print to the console thanking the user for donations.
    # return the user to original prompt.


def create_report():
    """This is going to print a list of donors sorted by total historical donation amount."""
    # include donor name, total donated, number of donations and average donation amount as values in each row.
    # print to the console a table with name, total amount, number of donations, average donation
    # return the user back to original prompt.


def sort_donors():
    """This is going to sort the donation values from high to low."""
