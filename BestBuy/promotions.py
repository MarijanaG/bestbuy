from abc import ABC, abstractmethod
from products import Product

# Promotion Abstract Base Class
class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, products, quantity):
        pass


# Percentage Discount Promotion
class PercentageDiscount(Promotion):
    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, products, quantity):
        discount = products.price * (self.percentage / 100)
        return (products.price - discount) * quantity


class SecondItemHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, products, quantity):
        full_price_items = quantity // 2 + quantity % 2  # Full price for half of the quantity
        half_price_items = quantity // 2  # Half price for the second half
        return (full_price_items * products.price) + (half_price_items * products.price * 0.5)


# Buy Two Get One Free Promotion
class BuyTwoGetOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, products, quantity):
        full_price_items = quantity - (quantity // 3)  # 1 free for every 3 items
        return full_price_items * products.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        # Call the parent class's constructor, setting quantity to 0
        super().__init__(name, price, quantity=0)

    def show(self):
        return f"{self.name} (Price: ${self.price}, Non-stocked) - {self.promotion.name if self.promotion else 'No promotion'}"



class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        promo_info = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name} (Price: ${self.price}, Quantity: {self.quantity}, Max: {self.maximum}) - {promo_info}"

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of {self.name}.")
        return super().buy(quantity)
