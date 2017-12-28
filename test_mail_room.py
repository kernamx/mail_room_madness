"""Test file for the mail room module."""
import mail_room2
import pytest
import pdb


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
    assert mail_room2.donation_history["Steve"] == []
    assert mail_room2.donation_history["John"] == []
