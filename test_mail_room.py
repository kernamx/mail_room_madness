"""Test file for the mail room module."""
import mail_room2
import pytest


def test_add_donor():
    """Test adding a donor."""
    mail_room2.add_donor('John')
    assert 'John' in mail_room2.list_of_donors


def test_add_donor_already_in_list():
    """Test adding a donor."""
    mail_room2.list_of_donors.append('Steve')
    assert len(mail_room2.list_of_donors) == 2
    mail_room2.add_donor("Steve")
    assert len(mail_room2.list_of_donors) == 2
