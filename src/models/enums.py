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


class IncomeSource(Enum):
    PRIMARY_PAYCHECK = "Primary Paycheck"
    BONUSES = "Bonuses"
    TIPS = "Tips/Gratuites"
    FREELANCE = "Freelance"
    E_COMMERCE = "E-commerce"
    DIVIDENDS = "Dividends"
    INTEREST = "Interest"
    RENTAL_INCOME = "Rental Income"
    CASHBACK = "Cashback/Rewards"
    MONEY_BACK = "Money Back"
