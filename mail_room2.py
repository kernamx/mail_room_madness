"""Python module to simulate a mail room."""
import sys
import operator

list_of_donors = []
donation_history = {}


def add_donor(name):
    """Add a donor to the list of donors is they are not already in it."""
    if name not in list_of_donors:
        list_of_donors.append(name)
        donation_history[name] = []
