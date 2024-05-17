from src import Factory
from functools import wraps


class Watcher(Factory):
    def __init__(self):
        self.events = {}
        self.data_model = {}
        super().__init__()
    
    def add_event(self, func):
        self.events[func.__name__] = func
        self.data_model[func.__name__] = None
        return self

    def remove_event(self, func):
        self.events.pop(func.__name__)
        self.data_model.pop(func.__name__)
        return self
    
    def exec_event(self, event=None, data=None):
        print(f'Exec hook event')
        if event is None:
            for name in self.events:
                self.data_model[name] = self.events[name](data)
        elif event in self.events.keys():
            self.data_model[event] = self.events[event](data)
        return self
    
    def catch_event(self, func):
        return self.data_model.get(func, None)
    
    def register(self, name=None):
        def decorator(func):
            task_name = func.__name__ if name is None else name
            self.agents[task_name] = func
            @wraps(func)
            def wrapper(*args, **kwargs):           
                result = func(*args, **kwargs)
                print('here')
                self.exec_event(data=result)
                return result
            return wrapper
        return decorator