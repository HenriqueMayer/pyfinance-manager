from sqlmodel import SQLModel, create_engine

# TO-DO: move DATABASE_URL to environment variable
DATABASE_URL = "postgresql://admin:admin@localhost:5432/finance_db"

engine = create_engine(DATABASE_URL, echo=True)  # Log SQL statements for debugging


def create_db_and_tables():
    """Create the database and tables based on the defined models."""
    SQLModel.metadata.create_all(engine)
