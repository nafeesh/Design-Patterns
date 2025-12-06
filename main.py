
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



def main():
    s1 = EagerSingleton()
    s2 = EagerSingleton()
    print(s1 is s2)


if __name__ == "__main__":
    main()
