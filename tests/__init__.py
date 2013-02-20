from io import BytesIO
from functools import wraps

def with_fd(data):
    def wrap(func):
        @wraps(func)
        def create_fd():
            fd = BytesIO(data)

            return func(fd)

        return create_fd

    return wrap

