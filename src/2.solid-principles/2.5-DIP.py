# Dependency Inversion Principle (DIP)
# High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Abstractions should not depend upon details. Details should depend upon abstractions.

# example 1: without DIP
# it violate DIP because NotificationService depends on EmailNotification and SMSNotification directly.


class EmailNotification:
    def notify(self, message):
        print("Email notification sent: " + message)

class SMSNotification:
    def notify(self, message):
        print("SMS notification sent: " + message)

class NotificationService:
    def __init__(self):
        self.send_email = EmailNotification()
        self.send_sms = SMSNotification()

    def send_notification(self, message, method):
        if method == "email":
            self.send_email.notify(message)
        elif method == "sms":
            self.send_sms.notify(message)


# exmaple 2: with DIP
from abc import abstractmethod, ABC

class IMessageService(ABC):
    @abstractmethod
    def notify(self, message):
        pass    

class EmailNotification(IMessageService):
    def notify(self, message):
        print("Email notification sent: " + message)

class SMSNotification(IMessageService):
    def notify(self, message):
        print("SMS notification sent: " + message)

class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service

    def send_notification(self, message):
        self.message_service.notify(message)


# Note - both high level and low level modules depend on abstractions.
# Here notification service depends on IMessageService abstraction rather than EmailNotification and SMSNotification.   