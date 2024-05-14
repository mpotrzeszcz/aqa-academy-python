# aqa-academy-python

# Coding rules

## Excluded folders

1. .venv folder.
   See venv creation https://docs.python.org/3/library/venv.html

## Dependency updates

1. Major libs version needs to be revisited once per month

# How to

1. Set up your env
   1.1 Create venv into .venv folder
   1.2 Install deps from requirenments.txt file

2. Before commit
   2.1 Run black tool
   2.2 Run flake8 tool
   2.3 Run isort tool

3. Run the tests
   3.1 Execute pytest . -s -v command staying in the root of the framework
   3.2 To form a report execute 'pytest . -s -v --html=reports/report.html --self-contained-html' command

# Structure of the framework

1. tests - folders for tests
2. reports - folder to store local reports
3. src/applications - folder for system under test abstractions
4. src/config - folder for configuration of framework
5. src/helpers - folder for single-use functions, etc
