from flask import redirect, session
from functools import wraps

def isLoggedIn(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if "username" not in session:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_func
