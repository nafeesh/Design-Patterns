# Single-Responsibility Principle 
# A class should have only one reason to change.

# Example 1: without SRP

class TODO:

    # Task Manager
    def __init__(self):
        self.tasks   = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    # UI
   def display_tasks(self):
        for task in self.tasks:
            print(task)

    # Input
    def input_task(self):
        task = input("Enter task: ")
        self.add_task(task)

    def remove_task(self):
        task = input("Enter task: ")
        self.remove_task(task)

# In above example, TODO class has multiple responsibilities. thats violate SRP.

# Example 2: with SRP

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class TaskPresenter:
    @staticmethod # this class doesn't have any state
    def display_tasks(tasks):
        for task in tasks:
            print(task)



class TaskInput:
    @staticmethod # this class doesn't have any state
    def input_task():
        task = input("Enter task: ")
        return task
        
    @staticmethod # this class doesn't have any state
    def remove_task():
        task = input("Enter task: ")
        return task