import os
import psycopg2
from connections import get_connection
from dotenv import load_dotenv

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,
    first_name varchar(25) not null, last_name varchar(25) not null, prop_tax int default 190,
    phone_number varchar(14) default 3025551234, rent int default 1600, debt_total int not null, income int not null,
    power_bill int default 100, water_bill int default 70, insurance int default 250);"""

INSERT_INFO = """INSERT INTO users(first_name, last_name, prop_tax, phone_number, rent, debt_total, income,
    power_bill, water_bill, insurance) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

SELECT_INFO = """SELECT * from users where id = (%s);"""

class Query:
    def __init__(self, first_name, last_name, prop_tax, phone_number, rent, debt_total, income, power_bill, water_bill, insurance):
        self.first_name = first_name
        self.last_name = last_name
        self.prop_tax = prop_tax
        self.phone_number = phone_number
        self.rent = rent
        self.debt_total = debt_total
        self.income = income
        self.power_bill = power_bill
        self.water_bill = water_bill
        self.insurance = insurance

    def __str__(self):
        return f"""First Name: {self.first_name}
            Last Name: {self.last_name}
            Property Tax: {self.prop_tax}
            Phone Number: {self.phone_number}
            Rent: {self.rent}
            Debt Total: {self.debt_total}
            Income: {self.income}
            Power Bill: {self.power_bill}
            Water Bill: {self.water_bill}
            Insurance: {self.insurance}"""

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
                    cursor.execute(INSERT_INFO, (self.first_name, self.last_name, self.prop_tax,
                                                 self.phone_number, self.rent, self.debt_total,
                                                 self.income, self.power_bill, self.water_bill,
                                                 self.insurance));

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
