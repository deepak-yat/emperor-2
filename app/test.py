from sqlalchemy import text

from app.database import engine


try:
    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT current_database()")
        )

        print("Connected to:", result.scalar())

except Exception as e:
    print("Database connection failed:")
    print(e)