from src.models.expense import Expense
from src.repos.base_repo import Base


class ExpenseRepo(Base):
    def save(self, expense: Expense):
        sql = """
            INSERT INTO expenses (id, amount_original, currency_code, exchange_rate, amount_base, payee, category, date, loan_id, notes)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        with self.get_connection() as conn:
            conn.execute(
                sql,
                (
                    str(expense.id),
                    str(expense.amount_original),
                    expense.currency_code.value,
                    str(expense.exchange_rate),
                    str(expense.amount_base),
                    expense.payee,
                    expense.category.value,
                    expense.date,
                    str(expense.loan_id),
                    expense.notes,
                ),
            )
