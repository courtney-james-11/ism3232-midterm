# Terminal Record: Harvest Table Catering

## 1. Building the project

cd ~/ism3232
mkdir -p ism3232-midterm
cd ~/ism3232/ism3232-midterm
pwd
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip freeze > requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
touch business_rules.py
touch main.py
touch commands.md
touch README.md
mkdir -p tests
touch tests/__init__.py tests/test_business_rules.py
git remote add origin https://github.com/courtney-james-11/ism3232-midterm
git branch -M main
git push -u origin main

## 2. The virtual environment

(.venv) Simon-Laptop% which python3

/home/courtneyjames/ism3232/ism3232-midterm/.venv/bin/python3

After running which python3, I know the virtual environment is active because the output ends in .venv/bin/python3

## 3. The project structure

(.venv) Simon-Laptop% tree -L 2
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

The __pycache__ folder is on my computer but not my github repository because it is listed in my .gitignore file, preventing it from showing up on github.

## 4. Every function and test

(.venv) Simon-Laptop% rg 'def '

tests/test_business_rules.py
16:def test_calculate_food_cost():
20:def test_get_event_discount_none():
24:def test_get_event_discount_5_limit():
28:def test_get_event_discount_5():
32:def test_get_event_discount_12():
36:def test_get_event_discount_12_limit():
40:def test_get_event_discount_limit_guests_fp():
44:def test_get_event_discount_upper_fp():
48:def test_calculate_event_total_no_service_fee():
52:def test_calculate_event_total_service_fee():
56:def test_needs_signoff_true():
60:def test_needs_signoff_false_limit():
64:def test_needs_signoff_false():
68:def test_needs_second_chef_guests_true():
72:def test_needs_second_chef_guests_false_limit():
76:def test_needs_second_chef_total_true_limit():
80:def test_needs_second_chef_total_false():
84:def test_total_booked():
103:def test_largest_event():
122:def test_format_event_line():

business_rules.py
12:def calculate_food_cost(guest_price: float, guests: int) -> float:
17:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
29:def calculate_event_total(
42:def needs_signoff(total: float) -> bool:
47:def needs_second_chef(guests: int, total: float) -> bool:
52:def total_booked(events: list) -> float:
62:def largest_event(events: list) -> str:
77:def format_event_line(

business_rules.py defines 8 functions and tests/test_business_rules.py defines 20.

## 5. Which files print

(.venv) Simon-Laptop% rg -l 'print'

main.py
commands.md

main.py and commands.md prints, but business_rules.py does not because it has no output and only contains functions to be called upon in main.py.

## 6. The commit history
(.venv) Simon-Laptop% git log --oneline

36b961c (HEAD -> main, origin/main) added comments to the top of rules, main, and test files
057229c wrote and tested 6 more pytest to file
3e1173d wrote and tested output of main.py
66778fa wrote and tested functions 7 and 8
6a6925f wrote and tested functions 5 and 6
4180ac2 wrote and tested functions 3 and 4
2629933 wrote and tested functions 1 and 2

There are 7 commits at this point. I still need to commit this file and the readme file to make a total of 9.
