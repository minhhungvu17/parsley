from functools import wraps


class Factory:
    def __init__(self):
        self.agents = {}

    def register(self, func, name=None):
        name = func.__name__ if name is None else name
        self.agents[name] = func
        @wraps(func)
        def wrapper(*args, **kwargs):           
            print(f"Execute in wrapper {func.__name__}")
            self.agents[name] = func
            result = func(*args, **kwargs)
            return result
        return wrapper