from app.security.jwt import (
    create_access_token,
    decode_access_token
)


user_id = 10

token = create_access_token(user_id)

print("JWT:")
print(token)

decoded = decode_access_token(token)

print("\nDecoded payload:")
print(decoded)