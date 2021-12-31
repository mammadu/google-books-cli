from setuptools import setup

setup(
    name = 'google-books-cli'
    , version = '0.1'
    , description = "CLI program to search google books and create/edit reading lists"
    , url='https://github.com/mammadu/google-books-cli'
    , python_requires='>=3.6'
    , install_requires = [
        'pandas'
        , 'requests'
        , 'pytest'
    ]
)