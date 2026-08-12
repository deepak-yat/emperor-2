from sqlalchemy import select

from app.database import SessionLocal
from app.models.employee import Employee
from app.models.user import User
from app.models.role import Role
from app.security.password import hash_password


def create_admin():

    db = SessionLocal()

    try:
        # 1. Check whether admin already exists
        existing_admin = db.scalar(
            select(User).where(
                User.user_name == "admin"
            )
        )

        if existing_admin:
            print("Admin already exists.")
            return

        # 2. Find the Admin role
        admin_role = db.scalar(
            select(Role).where(
                Role.role_name == "Admin"
            )
        )

        if not admin_role:
            print("Admin role not found.")
            return

        # 3. Create the employee record
        employee = Employee(
            name="System Admin",
            email="admin@company.com",
            salary=0,
            department_id=1
        )

        db.add(employee)

        # Get employee.id before creating User
        db.flush()

        # 4. Create the User account
        admin_user = User(
            user_name="admin",
            user_email="admin@company.com",
            hashed_password=hash_password("Admin@123"),
            employee_id=employee.id,
            role_id=admin_role.role_id,
            is_approved=True,
            is_active=True
        )

        db.add(admin_user)

        db.commit()

        print("Admin created successfully.")
        print("Username: admin")
        print("Password: Admin@123")

    except Exception as error:

        db.rollback()

        print("Failed to create admin.")
        print(error)

    finally:

        db.close()


if __name__ == "__main__":
    create_admin()