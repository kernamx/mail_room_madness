"""Test file for the mail room module."""
import mail_room2
import pytest
import pdb


def test_list_donors_no_donors():
    """Should return string stating that there are no donors."""
    assert mail_room2.list_donors() == "There are currently no donors"


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
