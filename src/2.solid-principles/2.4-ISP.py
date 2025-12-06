# Interface Segregation Principle (ISP)
# Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.

# example 1: without ISP
# it violate ISP because it is applying all methods to all classes.

class IMultiFunctionDevice:
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass

    def copy(self, document):
        pass


class Printer(IMultiFunctionDevice):
    def print(self, document):
        pass

class Scanner(IMultiFunctionDevice):
    def scan(self, document):
        pass

class Fax(IMultiFunctionDevice):
    def fax(self, document):
        pass

class Copy(IMultiFunctionDevice):
    def copy(self, document):
        pass


# exampel 2: with ISP

class IPrinter:
    def print(self, document):
        pass

class IScanner:
    def scan(self, document):
        pass

class IFax:
    def fax(self, document):
        pass

class ICopy:
    def copy(self, document):
        pass

class Printer(IPrinter):
    def print(self, document):
        pass

class Scanner(IScanner):
    def scan(self, document):
        pass

class Fax(IFax):
    def fax(self, document):
        pass

class Copy(ICopy):
    def copy(self, document):
        pass    

# The refactoring is done by applying ISP. it breaks the imultifunction device into multiple interfaces. 
# more specific interfaces are easier to implement and maintain.