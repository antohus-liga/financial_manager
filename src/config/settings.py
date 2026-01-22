from decimal import Decimal


class Settings:
    APP_NAME = "Personal Finance Manager"
    VERSION = "0.0.1"

    DB_NAME = "finance_app.db"

    BASE_CURRENCY = "USD"

    DEFAULT_DISPLAY_CURRENCY = "USD"

    CURRENCY_API_URL = "https://api.frankfurter.app/latest"

    FALLBACK_RATES = {
        "EUR": Decimal("0.92"),
        "GBP": Decimal("0.78"),
        "RUB": Decimal("75.99"),
    }
