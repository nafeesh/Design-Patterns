# The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to work together. It acts as a bridge between two unrelated interfaces.


# Imagine you have an e-commerce app that supports a standard internal payment system. 
# You now want to add a third-party payment gateway (like Stripe or PayPal), but their method names are completely different.

# step 1. The Target Interface (What your app expects)
# This is the standard interface your application is already built to use.
class PaymentProcessor:
    def pay(self, amount):
        pass


# step 2. The Adaptee (The Incompatible Class)
# This is the third-party library or legacy class you want to use. 
# Note that it doesn't have a pay() method; it has make_payment() and takes arguments differently.
class StripePaymentService:
    def make_payment(self, total_amount, currency):
        print(f"Stripe: Processing payment of {total_amount} {currency}")


# step 3. The Adapter
# This class implements the Target interface (PaymentProcessor) but delegates the actual work to the Adaptee (StripePaymentService). 
# It translates the call.

class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_service):
        self.stripe_service = stripe_service

    def pay(self, amount):
        # The adapter translates the 'pay' call into 'make_payment'
        # It also handles any data conversion (e.g., hardcoding 'USD')
        self.stripe_service.make_payment(amount, "USD")

# step 4. Client Code
# The client code works with the PaymentProcessor interface and doesn't need to know that Stripe works differently.
def process_order(processor: PaymentProcessor, amount):
    processor.pay(amount)

def main():
    # Scenario 1: Using the standard/internal system (if we had one)
    # internal_processor = InternalProcessor()
    # process_order(internal_processor, 50)

    # Scenario 2: Using the incompatible 3rd party service via Adapter
    stripe_service = StripePaymentService()
    stripe_adapter = StripeAdapter(stripe_service)

    print("Client: I am paying $100 via the Adapter:")
    process_order(stripe_adapter, 100)

if __name__ == "__main__":
    main()