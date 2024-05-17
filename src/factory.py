from functools import wraps


class Factory:
    def __init__(self):
        self.agents = {}

    def register(self, name=None):
        def decorator(func):
            task_name = func.__name__ if name is None else name
            self.agents[task_name] = func
            @wraps(func)
            def wrapper(*args, **kwargs):           
                result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator