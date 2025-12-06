# SINGLETON PATTERN: IS A creational design pattern that ensures a class has only one instance and provides a global point of access to it.

# Lazy loading: 
    # Lazy loading is the default behavior of the singleton pattern.
    # It means that the instance is created only when it is needed.
    # This is the most common and recommended way to implement the singleton pattern.

# Eager loading: 
    # Allow fot data preloading and chaching
    # We initialize and load the instance before it is needed.

# Example 1 : Classic Singleton Pattern 
class ClassicSingleton:
    _instance = None

    def __init__(self):
        raise RuntimeError("Use get_instance() instead")

    @classmethod
    def get_instance(cls):
        if cls._instance is None: # NOTE: lazy initialization
            cls._instance = cls()
        return cls._instance


# Example 2 : pythonic way

class PythonicSingleton:
    def __new__(cls):
        if not cls.instance: # lazy initialization
            cls.instance = super(PythonicSingleton, cls).__new__(cls)
        return cls.instance


# Example 3 : Using a metaclass

class Meta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs): # NOTE: lazy initialization
        if cls not in cls._instances:
            cls._instances[cls] = super(Meta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MetaclassSingleton(metaclass=Meta):
    def do_something(self):
        pass

    
# Example 4 : Eager loading using metaclass

class SingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        super(SingletonMeta, cls).__init__(name, bases, dct)
        cls._instances[cls] = super(SingletonMeta, cls).__call__()

    def __call__(cls, *args, **kwargs): # NOTE: eager initialization
        return cls._instances[cls]

class EagerSingleton(metaclass=SingletonMeta):
    def do_something(self):
        pass


# Thread-safe implementation
# Critical Section : Area of the code where multiple threads can access the same resource and can affect 
# data in a non-predictible way.

# Lock mechanism : only a single thread can execute the critical section at a time.   

import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance