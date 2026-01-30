from src.models.loan import Loan
from src.repos.base_repo import Base


class LoanRepo(Base):
    def save(self, loan: Loan):
        sql = """
            INSERT INTO loans (id, lender_name, original_amount, currency_code, current_amount, interest_rate, start_date, status)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """
        with self.get_connection() as conn:
            conn.execute(
                sql,
                (
                    str(loan.id),
                    loan.lender_name,
                    str(loan.original_amount),
                    loan.currency_code.value,
                    str(loan.current_amount),
                    str(loan.interest_rate),
                    loan.start_date,
                    loan.status.value,
                ),
            )

    def get_all(self):
        with self.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM loans ORDER BY date DESC")
            return [self._map_to_obj(row) for row in cursor.fetchall()]

    def _map_to_obj(self, row) -> Loan:
        return Loan(
            id=row["id"],
            original_amount=row["original_amount"],
            current_amount=row["current_amount"],
            currency_code=row["currency_code"],
            interest_rate=row["interest_rate"],
            lender_name=row["lender_name"],
            status=row["status"],
            start_date=row["start_date"],
        )
