"""Test file for the mail room module."""
# import pytest


# def test_create_report(name, total, number, average):
#     """."""
#     from mail_room import create_report


def test_testable_add_donation_history():
    """."""
    from mail_room import testable_add_donation_history
    assert testable_add_donation_history(300, 'kevin') == \
        'Thank you, kevin, for your generous donation of $300\n'


def test_testable_add_donation_history_dict():
    """."""
    from mail_room import testable_add_donation_history
    from mail_room import donation_history
    testable_add_donation_history(300, 'kevin')
    assert donation_history['kevin'] == [300, 300]
