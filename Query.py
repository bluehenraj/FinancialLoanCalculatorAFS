import os
import psycopg2
from connections import get_connection
from dotenv import load_dotenv

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,
    first_name varchar(25) not null, last_name varchar(25) not null, income INTEGER not null, debt_total INTEGER not null,
    rent INTEGER default 1600, prop_tax FLOAT default 1.05, phone_number varchar(14) default 3025551206, power INTEGER default 80,
    water INTEGER default 72, garbage INTEGER default 14, cable INTEGER default 104, prescriptions INTEGER default 90,
    doctor_visits INTEGER default 150, carpayment1 INTEGER default 280, carpayment2 INTEGER default 280,
    autoinsurance INTEGER default 140, gasoline INTEGER default 150, groceries INTEGER default 200, pchi INTEGER default 80);"""

CREATE_TABLE_EMAIL = """CREATE TABLE IF NOT EXISTS emails(email TEXT, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id));"""

INSERT_INFO = """INSERT INTO users(first_name, last_name, income, debt_total, rent, prop_tax, phone_number,
    power, water, garbage, cable, prescriptions, doctor_visits, carpayment1, carpayment2,
    autoinsurance, gasoline, groceries, pchi) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

INSERT_EMAIL = """INSERT INTO emails (email, user_id) VALUES (%s,%s);"""

SELECT_INFO = """SELECT * from users where id = (%s);"""

class Query:
    def __init__(self, fn, ln, income, debt, rent, prop_tax, phone_number, power, water, garbage, cable,
                 prescriptions, doctor_visits, carpayment1, carpayment2, autoinsurance, gasoline,
                 groceries, pchi):
        self.first_name = fn
        self.last_name = ln
        self.income = income
        self.debt_total = debt
        self.rent = rent
        self.prop_tax = prop_tax
        self.phone_number = phone_number
        self.power = power
        self.water = water
        self.garbage = garbage
        self.cable = cable
        self.prescriptions = prescriptions
        self.doctor_visits = doctor_visits
        self.carpayment1 = carpayment1
        self.carpayment2 = carpayment2
        self.autoinsurance = autoinsurance
        self.gasoline = gasoline
        self.groceries = groceries
        self.pchi = pchi

    def __str__(self):
        return f"""\tFirst Name: {self.first_name}
        Last Name: {self.last_name}
        Income: {self.income}
        Debt Total: {self.debt_total}
        Rent: {self.rent}
        Property Tax: {self.prop_tax}
        Phone Number: {self.phone_number}
        Power: {self.power}
        Water: {self.water}
        Garbage: {self.garbage}
        Cable: {self.cable}
        Prescriptions: {self.prescriptions}
        Doctor Visits: {self.doctor_visits}
        Car Payment 1: {self.carpayment1} Car Payment 2: {self.carpayment2}
        Auto Insurance: {self.autoinsurance}
        Gasoline: {self.gasoline}
        Groceries: {self.groceries}
        PCHI = {self.pchi}"""

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
                    cursor.execute(INSERT_INFO, (self.first_name, self.last_name, self.income, self.debt_total, self.rent,
                                                 self.prop_tax, self.phone_number, self.power, self.water,
                                                 self.garbage, self.cable, self.prescriptions, self.doctor_visits,
                                                 self.carpayment1, self.carpayment2, self.autoinsurance,
                                                 self.gasoline, self.groceries, self.pchi));

    def insert_email(self, email, corres_id):
        """
        Inserts email and it's corresponding person id into the table
        """
        with get_connection() as connection:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(INSERT_EMAIL, (email, corres_id))

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
