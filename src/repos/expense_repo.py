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

    def get_all(self):
        with self.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM expenses ORDER BY date DESC")
            return [self._map_to_obj(row) for row in cursor.fetchall()]

    def _map_to_obj(self, row) -> Expense:
        return Expense(
            id=row["id"],
            amount_base=row["amount_base"],
            amount_original=row["amount_original"],
            currency_code=row["currency_code"],
            exchange_rate=row["exchange_rate"],
            payee=row["payee"],
            category=row["category"],
            date=row["date"],
            loan_id=row["loan_id"],
            notes=row["notes"],
        )

    def delete(self, expense_id):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
