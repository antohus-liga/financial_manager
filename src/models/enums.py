from enum import Enum


class Currency(Enum):
    EUR = "€"
    USR = "$"
    RUB = "₽"


class ExpenseCategory(Enum):
    HOUSING = "Housing"
    UTILITIES = "Utilities"
    TRANSPORTATION = "Transportation"
    GROCERIES = "Groceries"
    HEALTH = "Health"
    DINING_OUT = "Dining Out"
    ENTERTAINMENT = "Entertainment"
    PERSONAL_CARE = "Personal Care"
    TRAVEL = "Travel"
    DEBT_PAYMENT = "Debt Payment"
    INVESTMENT = "Investment"
    LEND = "Lend"
