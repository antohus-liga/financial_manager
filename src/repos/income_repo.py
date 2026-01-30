from src.models.income import Income
from src.repos.base_repo import Base


class IncomeRepo(Base):
    def save(self, income: Income):
        sql = """
            INSERT INTO incomes (id, amount_original, currency_code, exchange_rate, amount_base, source, date, notes)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """
        with self.get_connection() as conn:
            conn.execute(
                sql,
                (
                    str(income.id),
                    str(income.amount_original),
                    income.currency_code.value,
                    str(income.exchange_rate),
                    str(income.amount_base),
                    income.source.value,
                    income.date,
                    income.notes,
                ),
            )
