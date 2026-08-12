from app.security.password import (
    hash_password,
    verify_password
)


password = "Admin@123"

hashed = hash_password(password)

print("Original password:")
print(password)

print("\nHashed password:")
print(hashed)

print("\nCorrect password:")
print(
    verify_password(
        password,
        hashed
    )
)

print("\nWrong password:")
print(
    verify_password(
        "WrongPassword",
        hashed
    )
)