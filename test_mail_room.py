"""Test file for the mail room module."""
import pytest


def test_create_report(name, total, number, average):
    """."""
    from mail_room import create_report
