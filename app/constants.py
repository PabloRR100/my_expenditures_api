from enum import Enum


class Category(str, Enum):
    SALARY = "Salary"
    EXTRA_INCOME = "Extra Income"
    HOME = "Home"
    GROCERIES = "Groceries"
    RESTAURANTS = "Restaurants"
    PARTY = "Party"
    TRAVEL = "Travel"
    BILLS = "Bills"
    HEALTHCARE = "Healthcare"
    BEAUTY = "Beauty"
    ENTERTAINMENT = "Entertainment"
    SAVINGS = "Savings"
    CLOUD = "Cloud"
    STOCK = "Stock"


class Transaction(str, Enum):
    INCOME = "Income"
    EXPENSE = "Expense"
