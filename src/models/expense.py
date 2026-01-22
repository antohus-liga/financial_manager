from dataclasses import dataclass, field
from uuid import UUID, uuid4
from decimal import Decimal
from typing import Optional
import datetime


@dataclass
class Expense:
    amount: Decimal
    payee: str
    category: str
    id: UUID = field(default_factory=uuid4)
    date: datetime.date = field(default_factory=datetime.date.today)
    loan_id: Optional[UUID] = None
    notes: Optional[str] = None
