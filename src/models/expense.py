from dataclasses import dataclass, field
from uuid import UUID, uuid4
from decimal import Decimal
from typing import Optional
import datetime

from src.models.models_enums import Currency, ExpenseCategory


@dataclass
class Expense:
    amount_base: Decimal
    amount_original: Decimal
    currency_code: Currency
    exchange_rate: Decimal
    payee: str
    category: ExpenseCategory
    id: UUID = field(default_factory=uuid4)
    date: datetime.date = field(default_factory=datetime.date.today)
    loan_id: Optional[UUID] = None
    notes: Optional[str] = None
