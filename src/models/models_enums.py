from enum import Enum


class Currency(Enum):
    EUR = "EUR"
    USD = "USD"
    RUB = "RUB"

    @property
    def symbol(self):
        map = {
            "USD": "$",
            "EUR": "€",
            "RUB": "₽",
        }
        return map.get(self.value, "$")


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


class LoanStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    PROSPECT = "Prospect"
