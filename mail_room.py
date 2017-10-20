"""."""


protmpt = " " #multiple prompts
#first prompt is would you like to send a thank you or create a report.
list_of_donors = 
donation_history = {} #leave for user donation history.  keys will the the users' name and values will be a list of donations.

def get_user_input(prompt, validator=None):
    """Ask the user to select the opition, calls the function based on the input of the user."""
    reply = None  
    while reply is None:
        reply = raw_input(prompt)
        if validate_input(reply):
            return reply
        else:
            print("bad input")
            get_user_input(prompt, validate=None)


def validate_input(response, acceptable_response):
    """This is checking if the user input is valid."""
    #if the response is quit return to original prompt.
    #if the response is quit at the original prompt then quit the script.
    if response == good response:
        return True
    else:
        return False


def response_to_user(input):
    """Base on how the user response to the prompt will call the next function.  
    If input == 'thank you':
    call the thank_you function.  etc..."""




def thank_you():
    """This will create a thank you email and print it to the console."""
    reply = raw_input("please enter your name.")
    #if reply is not in list_of_donors then add the name to the list.
    #prompt the user how much they want to donate.
    #call the validate_input function to make sure they input a number.
    #then added the amount to donation history .
    #then print to the console thanking the user for donations.
    #return the user to original prompt.


def create_report():
    """This is going to print a list of donors sorted by total historical donation amount."""
    #include donor name, total donated, number of donations and average donation amount as values in each row.
    #print to the console a table with name, total amount, number of donations, average donation
    #return the user back to original prompt.


def sort_donors():
    """This is going to sort the donation values from high to low."""
