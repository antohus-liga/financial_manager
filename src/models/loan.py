from dataclasses import dataclass, field
from uuid import UUID, uuid4
from decimal import Decimal
import datetime

from src.models.models_enums import Currency, LoanStatus


@dataclass
class Loan:
    lender_name: str
    original_amount: Decimal
    currency_code: Currency
    current_amount: Decimal
    interest_rate: Decimal
    start_date: datetime.date = field(default_factory=datetime.date.today)
    status: LoanStatus = LoanStatus.ACTIVE
    id: UUID = field(default_factory=uuid4)
