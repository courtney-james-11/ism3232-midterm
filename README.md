# ISM3232 Midterm: Harvest Table Catering

- **Name:** Courtney James
- **Version:** BETA
- **Date:** 10/25/26

## What This Program Does

This program genrates a event report for Harvest Table Catering. Based on individual event data, the program calculates the total individual event cost and uses that informatation to report the total amount booked, average event total, client with the largetst event total, and  how many manager sign-offs or second chefs were needed.

## Business Rules

1. The total food cost is equal to the price per guest times the number of guests who attended.
2. Events with fewer than 25 guests recieve no discount, events with 25 to 99 guests recieve a 5% discount, and events with 100 guests or more recieve a 12% discount.
3. If an event is for profit with 100 guests or more, they only can get a 5% discount. A nonprofit event with 100 guests or more still gets the 12% discount.
4. When the discounted cost is less than $500, a service fee of $75 is added to the event total.
5. If the event has a total cost of more than $2500, a managers sign0ff is required.
6. If an event has more than 80 guests or an event total of $3000 or more, a second chef is required.

## How to Run

python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip freeze > requirements.txt
python3 main.py

## How to Test

ruff format .
ruff check .
pytest -v

20 tests were written for this program.

## Files in This Repository

1. business_rules.py: This file contain 8 functions related to the business rules of Harvest Table Catering.
2. main.py: This file contains the print statements and code necessary to genrate the Event Report.
3. commands.md: This file lists the commands used in the terminal to create the project folder, environment, and git repository. It also shows the project structure and git commit history.
4. README.md: This file is an overview of the project with instructions on how to use and test the program.
5. requirements.txt: This file lists the required packages installed on my computer to peform the functions of this project.
6. .gitignore: This file keeps .venv/ and __pycache__/ out of the git repository.
7.  __init__.py: This file tells python that the folder is a structured package.
8. test_business_rules.py: This file contains 20 functions that test the rules identified in business_rules.py

## AI Use Statement

I did not use any AI on this exam.