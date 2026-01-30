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

    def get_all(self):
        with self.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM incomes ORDER BY date DESC")
            return [self._map_to_obj(row) for row in cursor.fetchall()]

    def _map_to_obj(self, row) -> Income:
        return Income(
            id=row["id"],
            amount_base=row["amount_base"],
            amount_original=row["amount_original"],
            currency_code=row["currency_code"],
            exchange_rate=row["exchange_rate"],
            source=row["source"],
            date=row["date"],
            notes=row["notes"],
        )
