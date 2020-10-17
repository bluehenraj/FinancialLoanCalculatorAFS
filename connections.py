import os
from contextlib import contextmanager
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Assign the environment variables
database_url = os.environ["DATABASE_URL"]

pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=database_url)

# Context manager for giving out connections from the pool
@contextmanager
def get_connection():
    connection = pool.getconn()

    try:
        yield connection
    finally:
        pool.putconn(connection)
