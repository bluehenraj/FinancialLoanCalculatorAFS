import os
import psycopg2
from connections import get_connection
from dotenv import load_dotenv

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,
    first_name varchar(25) not null, last_name varchar(25) not null, grocery_cost int default 200,
    auto_cost int default 100, housing_cost int default 1600, debt_total int not null, income int not null);"""

INSERT_INFO = """INSERT INTO users(first_name, last_name, grocery_cost, auto_cost, housing_cost, debt_total,
    income) values(%s,%s,%s,%s,%s,%s,%s);"""

SELECT_INFO = """SELECT first_name, last_name, grocery_cost, auto_cost, housing_cost, debt_total, income from
    users where id = (%s);"""

class Query:
    def __init__(self, first_name, last_name, grocery_cost, auto_cost, housing_cost, debt_total, income):
        self.first_name = first_name
        self.last_name = last_name
        self.grocery_cost = grocery_cost
        self.auto_cost = auto_cost
        self.housing_cost = housing_cost
        self.debt_total = debt_total
        self.income = income

    def __str__(self):
        return f"""First Name: {self.first_name}\nLast Name: {self.last_name}\nGrocery Cost: {self.grocery_cost}\nAuto Cost: {self.auto_cost}\nHousing Cost: {self.housing_cost}\nDebt Total: {self.debt_total}\nIncome: {self.income}"""

    def create_tables(self):
        """
        Creates the table (copy safe)
        """
        with get_connection() as connection:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(CREATE_TABLE)

    def insert_all(self):
        """
        Inserts data when ALL data is known
        """
        with get_connection() as connection:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(INSERT_INFO, (self.first_name, self.last_name, self.grocery_cost,
                            self.auto_cost, self.housing_cost, self.debt_total, self.income));

    def select_all(self, person_id):
        """
        Selects all data based off the passed person id
        Returns: A list of one tuple containing the attributes of the person_id passed
        """
        rows = []
        with get_connection() as connection:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(SELECT_INFO, (person_id,))
                    rows = cursor.fetchall()
        return rows
