# The Observer Pattern is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects 
# about any events that happen to the object they're observing.


# Let's implement a simple News Feed system where users can subscribe to different categories of news and receive updates when new news are published.


# Step 1: Define the Subject Interface
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# Step 2: Implement Concrete Subject
class NewsFeed(Subject):
    def __init__(self):
        self._observers = []
        self._latest_news = None

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self._latest_news)

    def add_news(self, news):
        self._latest_news = news
        self.notify()


# Step 3: Define the Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, news):
        pass


# Step 4: Implement Concrete Observers
class User(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, news):
        print(f"{self._name} received news: {news}")


# Step 5: Client Code
def main():
    # Create a news feed
    news_feed = NewsFeed()

    # Create observers
    user1 = User("Alice")
    user2 = User("Bob")

    # Attach observers to the news feed
    news_feed.attach(user1)
    news_feed.attach(user2)

    # Add some news
    news_feed.add_news("Breaking News: New vaccine approved!")
    news_feed.add_news("Local event: Community festival next week!")

    # Detach one observer
    news_feed.detach(user1)

    # Add more news
    news_feed.add_news("Important update: Tax season extension!")

if __name__ == "__main__":
    main()