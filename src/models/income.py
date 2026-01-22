from dataclasses import dataclass, field
import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID, uuid4

from src.models.enums import Currency, IncomeSource


@dataclass
class Income:
    amount_original: Decimal
    currency_code: Currency
    exchange_rate: Decimal
    amount_base: Decimal
    source: IncomeSource
    id: UUID = field(default_factory=uuid4)
    date: datetime.date = field(default_factory=datetime.date.today)
    notes: Optional[str] = None
