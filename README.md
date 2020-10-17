# Team 12

Our submission for J.P. Morgan Chase's 2020 Code for Good.  
Non-profit: American Financial Solutions

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Flask, dotenv & psycopg2.

```bash
pip install Flask
pip install python-dotenv
pip install psycopg2-binary
```

## Usage

```python
python app.py
```

Goto localhost:5000/

## Our Thought Process

 AFS had made it clear that a major painpoint that they were dealing with was their extremely long and daunting form that prospective clients had to fill out. Our goal was to make the process more streamlined, by breaking the form into smaller, more easily digestable chunks. We also "gamified" the form, by using suble design decisions such as showing them what step the user was currently on, as if they were beating levels in a game. We also wanted to give the user more instant feedback, so as they filled out the form they would receive a customized quote, which would encourage them to keep going. All data that the user enters is stored in a database.

 As for their second problem, we wanted to make their quiz much more interactive. We decided to scrap the long video, and instead go with a branching quiz. Depending on how the user answers, they will receive different and personalized questions. When the user feels that the test is tailored towards them, they are more likely to complete it.

 ## The Team!:

 [Image of team](https://i.imgur.com/UkKkaiS.jpg)