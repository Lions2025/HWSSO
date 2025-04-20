import jwt
import datetime
from functools import lru_cache

SECRET_KEY = "your-256-bit-secret"
ALGORITHM = "HS256"

def create_jwt(user_id: str, client_id: str):
    payload = {
        "sub": user_id,
        "iss": "sso-idp",
        "aud": client_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@lru_cache(maxsize=128)
def verify_jwt(token: str, client_id: str):
    try:
        payload = jwt.decode(
            token, 
            SECRET_KEY, 
            algorithms=[ALGORITHM],
            audience=client_id,
            issuer="sso-idp"
        )
        return payload
    except jwt.PyJWTError:
        return None
