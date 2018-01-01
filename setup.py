# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="mail-room",
    description="A python simulation of a mail room for a charity",
    version=0.1,
    author='Max Wolff',
    author_email="maxawolff@hotmail.com",
    license='MIT',
    py_modules=['mail_room2'],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    entry_points={
        'console_scripts': [
            "mailroom = mail_room2:mail_room"
        ]
    }
)
