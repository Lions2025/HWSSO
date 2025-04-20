import jwt
import datetime
from functools import lru_cache

SECRET_KEY = "your-256-bit-secret-key-keep-it-safe!"
ALGORITHM = "HS256"

def create_jwt(payload):
    payload.update({
        "iss": "sso-idp",
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    })
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@lru_cache(maxsize=128)
def verify_jwt(token):
    try:
        return jwt.decode(
            token, 
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"verify_aud": False}
        )
    except jwt.PyJWTError:
        return None
