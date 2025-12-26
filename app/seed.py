from sqlmodel import Session, select
from app.database import engine, create_db_and_tables
from app.models import Account, AccountType, Category


def create_initial_data():
    """Populate the database with initial categories and accounts."""
    # Ensure tables exist before inserting
    create_db_and_tables()

    with Session(engine) as session:
        print("🌱 Starting seed: populating initial data...")

        # Fetch existing names to avoid duplicates (idempotent seed)
        existing_category_names = set(session.exec(select(Category.name)).all())
        existing_account_names = set(session.exec(select(Account.name)).all())

        # --- 1. CATEGORIES ---
        categories = [
            Category(name="Salary", description="Monthly income"),
            Category(name="Home Office", description="Work-from-home stipend"),
            Category(name="Food", description="Groceries, Restaurants, Delivery"),
            Category(name="Transport", description="Ride-hailing, Fuel, Maintenance"),
            Category(name="Subscriptions", description="Streaming, Software, Services"),
            Category(name="Gym", description="Gym membership"),
            Category(name="Shopping", description="Clothes, Electronics, Leisure"),
            Category(
                name="Investments", description="Contributions to fixed/variable income"
            ),
            Category(name="Housing", description="Rent, HOA, Electricity, Internet"),
        ]
        categories_to_create = [
            c for c in categories if c.name not in existing_category_names
        ]
        if categories_to_create:
            session.add_all(categories_to_create)

        # --- 2. ACCOUNTS ---
        accounts = [
            Account(name="Mercado Pago", account_type=AccountType.CHECKING),
            Account(name="Inter Bank", account_type=AccountType.CHECKING),
            Account(name="Nubank Credit Card", account_type=AccountType.CREDIT),
            Account(name="Inter Credit Card", account_type=AccountType.CREDIT),
            Account(name="Renner Credit Card", account_type=AccountType.CREDIT),
            Account(name="Cash Balance", account_type=AccountType.CASH),
            Account(name="Piggy Bank", account_type=AccountType.SAVINGS),
            Account(name="Brokerage", account_type=AccountType.INVESTMENT),
        ]
        accounts_to_create = [
            a for a in accounts if a.name not in existing_account_names
        ]
        if accounts_to_create:
            session.add_all(accounts_to_create)

        # --- 3. COMMIT ---
        session.commit()

        print("✅ Seed completed successfully.")
        print(f"   - Categories created: {len(categories_to_create)}")
        print(f"   - Accounts created: {len(accounts_to_create)}")


if __name__ == "__main__":
    create_initial_data()
