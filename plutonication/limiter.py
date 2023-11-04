"Socket.IO limiter"

# stdlib
from functools import wraps
from typing import Callable
from flask_socketio import disconnect
# 3rd party
import redis
# local
from . import app

r = redis.Redis(app.config['REDIS_HOST'])


def limit_socketio(
    key: str = 'socketio',
    window: int = 1,
    allowance: int = 2
) -> Callable:
    """
    Rate-limiter for Socket.IO event handlers.

    :param key: The key (prefix) of the redis object for tracking request rate
    :param window: Length (in seconds) of the window
    :param allowance: How many requests to allow within the window
    """

    def wrapper(f: Callable):
        from flask_login import current_user

        @wraps(f)
        def func(*args, **kwargs):
            rkey = f'{key}.{current_user.id}'
            u = r.get(rkey)

            if u is None:
                r.setex(rkey, 1, window)
                u = 1
            else:
                u = r.incr(rkey)

            if u > allowance:
                app.logger.debug(f'Rate-limiting {current_user.username}')

                disconnect()
                return None

            return f(*args, **kwargs)

        return func

    return wrapper
