# The State Pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. 
# It's often used to implement state machines or finite state machines.

# Let's implement a Document Workflow system. A document can be in Draft, Moderation, or Published states. 
# The publish() method works differently in each.

# Step 1: Define the State Interface
# This abstract class defines the actions available across all states.

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def publish(self, document):
        pass

    @abstractmethod
    def reject(self, document):
        pass


# Step 2: Concrete States
# Each class represents a specific state and implements the behavior for that state.
class Draft(State):
    def publish(self, document):
        print("Draft: Moving to moderation for review.")
        document.state = Moderation()  # Transition to Moderation

    def reject(self, document):
        print("Draft: Cannot reject a draft. It's not submitted yet.")

class Moderation(State):
    def publish(self, document):
        print("Moderation: Approved! Publishing document.")
        document.state = Published()  # Transition to Published

    def reject(self, document):
        print("Moderation: Rejected. Sending back to draft.")
        document.state = Draft()  # Transition back to Draft

class Published(State):
    def publish(self, document):
        print("Published: Already published. Nothing to do.")

    def reject(self, document):
        print("Published: Cannot reject. Unpublishing requires different logic.")


# Step 3. The Context
# This is the main object (the Document) that holds a reference to the current state. It delegates the work to the state object.
class Document:
    def __init__(self):
        self.state = Draft(self)

    def publish(self):
        self.state.publish(self)

    def reject(self):
        self.state.reject(self)

    def set_state(self, state):
        self.state = state


# Step 4. Client Code
def main():
    my_doc = Document()
    print(f"Current State: {type(my_doc.state).__name__}")

    # 1. Try to publish from Draft
    my_doc.publish()  
    # Output: Draft: Moving to moderation for review.
    print(f"Current State: {type(my_doc.state).__name__}")

    # 2. Reviewer rejects it
    my_doc.reject()   
    # Output: Moderation: Rejected. Sending back to draft.
    print(f"Current State: {type(my_doc.state).__name__}")

    # 3. Try again
    my_doc.publish()  # Moves to Moderation
    my_doc.publish()  # Moves to Published
    # Output: Moderation: Approved! Publishing document.
    
    print(f"Current State: {type(my_doc.state).__name__}")

    # 4. Try to publish again
    my_doc.publish()
    # Output: Published: Already published. Nothing to do.

if __name__ == "__main__":
    main()