from functools import wraps
from flask import request, jsonify
import jwt

SECRET_KEY = "your-256-bit-secret-key-keep-it-safe!"

def authenticate(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        return {
            "sub": payload.get('sub'),
            "email": payload.get('email'),
            "client_id": payload.get('client_id')
        }
    except jwt.PyJWTError:
        return None

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token or not authenticate(token):
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated
