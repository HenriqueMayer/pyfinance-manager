# Proof of Concept for Database Connection using SQLModel and PostgreSQL

from sqlmodel import SQLModel, create_engine, text

# Define the database connection URL
DATABASE_URL = "postgresql://admin:admin@localhost:5432/finance_db"
engine = create_engine(DATABASE_URL, echo=True)


def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 'Hello, World!'"))
            print(result.scalar())
            print("Connection to the database was successful!")
    except Exception as e:
        print("Failed to connect to the database.", e)


if __name__ == "__main__":
    test_connection()
