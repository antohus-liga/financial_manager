import sqlite3
from contextlib import contextmanager


class Base:
    def __init__(self, db_path: str = "finance_app.db"):
        self.db_path = db_path
        self._create_tables()

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def _create_tables(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS loans (
                    id TEXT PRIMARY KEY,
                    lender_name TEXT NOT NULL,
                    original_amount TEXT NOT NULL,
                    currency_code TEXT,
                    current_amount TEXT NOT NULL,
                    interest_rate TEXT,
                    start_date TEXT,
                    status TEXT DEFAULT 'ACTIVE'
                );
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id TEXT PRIMARY KEY,
                    amount_original TEXT NOT NULL,
                    currency_code TEXT,
                    exchange_rate TEXT,
                    amount_base TEXT,
                    payee TEXT,
                    category TEXT,
                    date TEXT NOT NULL,
                    loan_id TEXT,
                    notes TEXT,
                    FOREIGN KEY (loan_id) REFERENCES loans (id) ON DELETE SET NULL
                );
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS incomes (
                    id TEXT PRIMARY KEY,
                    amount_original TEXT NOT NULL,
                    currency_code TEXT,
                    exchange_rate TEXT,
                    amount_base TEXT,
                    source TEXT,
                    date TEXT NOT NULL,
                    notes TEXT
                );
            """
            )

            conn.commit()
