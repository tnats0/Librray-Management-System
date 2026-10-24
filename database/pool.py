import os
from contextlib import contextmanager

import dotenv
from mysql.connector import pooling, Error

dotenv.load_dotenv(".env")


def _need(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}")
    return value


_pool = pooling.MySQLConnectionPool(
    pool_name="library_pool",
    pool_size=int(os.getenv("DBPoolSize")),  
    pool_reset_session=True,                      
    host=os.getenv("DBHost"),
    port=int(os.getenv("DBPort")),
    user=_need("DBUserName"),
    password=_need("DBPassword"),
    database=_need("DBName"),
    connection_timeout=10,
)


@contextmanager
def get_cursor(commit: bool = False):
    connection = _pool.get_connection()
    cursor = connection.cursor(buffered=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    except Error:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()