import app
from contextlib import contextmanager
from psycoph2.pool import SimpleConnectionPool

pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=database_url)

# Context manager for giving out connections from the pool
@contextmanager
def get_connection():
    connection = pool.getconn()

    try:
        yield connection
    finally:
        pool.putconn()
