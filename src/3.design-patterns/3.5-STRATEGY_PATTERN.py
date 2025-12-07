# The Strategy Pattern is a behavioral design pattern that lets you define a family of algorithms, encapsulate each one, 
# and make them interchangeable. It allows the algorithm to vary independently from the clients that use it.


# Let's implement a Discount System for an e-commerce store. Depending on the customer type or season, 
# the discount calculation strategy changes.


# Step 1: Define the Strategy Interface
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_price(self, price: float) -> float:
        pass


# step 2: Implement Concrete Strategies

# Strategy 1: No Discount
class RegularPriceStrategy(DiscountStrategy):
    def calculate_price(self, price: float) -> float:
        return price

# Strategy 2: 20% Seasonal Discount
class SeasonalDiscountStrategy(DiscountStrategy):
    def calculate_price(self, price: float) -> float:
        return price * 0.80

# Strategy 3: VIP Discount (50% off!)
class VIPDiscountStrategy(DiscountStrategy):
    def calculate_price(self, price: float) -> float:
        return price * 0.50


# step 3. The Context
# This is the class that the client actually interacts with. It holds a reference to a strategy object and delegates the work to it. 
# Notice it allows setting the strategy at runtime.
class PriceCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self._strategy = strategy

    # Allow changing the strategy dynamically
    def set_strategy(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def calculate(self, price: float):
        result = self._strategy.calculate_price(price)
        print(f"Original: ${price} -> Final: ${result:.2f}")


# 4. Client Code
# The client picks the strategy and passes it to the context.
def main():
    # Start with a regular price strategy
    calculator = PriceCalculator(RegularPriceStrategy())
    calculator.calculate(100.0)  # Output: 100.00

    print("--- Switching to Seasonal Sale ---")
    
    # Change behavior at runtime!
    calculator.set_strategy(SeasonalDiscountStrategy())
    calculator.calculate(100.0)  # Output: 80.00

    print("--- Customer logs in as VIP ---")

    # Change behavior again
    calculator.set_strategy(VIPDiscountStrategy())
    calculator.calculate(100.0)  # Output: 50.00

if __name__ == "__main__":
    main()