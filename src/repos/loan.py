from src.models.loan import Loan
from src.repos.base import Base


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
