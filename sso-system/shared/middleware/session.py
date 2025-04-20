from redis import Redis
from functools import wraps

redis = Redis(host='redis', port=6379, db=0)

def session_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        session_id = request.cookies.get('session_id')
        if not session_id or not redis.exists(session_id):
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated
