from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    """
        Abstract base class representing a promotion that can be applied to a product."""
    def __init__(self, name):
        """
                Initializes the Promotion class with the given name."""
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        # Default behavior: no promotion, just regular price
        return product.price * quantity


class PercentageDiscount(Promotion):
    """Represents a percentage discount promotion that applies a discount to a product."""
    def __init__(self, name, percentage):
        """Initializes the PercentageDiscount class with a promotion name and discount percentage."""
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        """Applies the percentage discount to a product and calculates the total cost for the given quantity."""
        discount = product.price * (self.percentage / 100)
        return (product.price - discount) * quantity


class SecondItemHalfPrice(Promotion):
    """Represents a promotion where the second item is half price.
       The quantity is split in half, and the second half of the items is charged at half price.
       """
    def __init__(self, name):
        """Initializes the SecondItemHalfPrice class with a promotion name."""
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """Applies the second item half price promotion to the given quantity of the product."""
        full_price_items = quantity // 2 + quantity % 2  # Full price for half of the quantity
        half_price_items = quantity // 2  # Half price for the second half
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class BuyTwoGetOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        paid_items = quantity - free_items
        total_cost = paid_items * product.price
        return total_cost, free_items

class NonStockedProduct(Product):
    """Represents a non-stocked product, which cannot be added to a store's inventory."""
    def __init__(self, name, price):
        """Initializes the NonStockedProduct class with a name and price,setting quantity to 0."""
        super().__init__(name, price, quantity=0)

    def show(self):
        """Displays the details of the non-stocked product."""
        return f"{self.name} (Price: ${self.price}, Non-stocked) - {self.promotion.name if self.promotion else 'No promotion'}"


class LimitedProduct(Product):
    """Represents a limited product that has a maximum purchase quantity."""
    def __init__(self, name, price, quantity, maximum):
        """Initializes the LimitedProduct class with a name, price, quantity, and maximum purchase limit."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """Displays the details of the limited product, including the promotion if any."""
        promo_info = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name} (Price: ${self.price}, Quantity: {self.quantity}, Max: {self.maximum}) - {promo_info}"

    def buy(self, quantity):
        """Attempts to buy the given quantity of the limited product, ensuring it does not exceed the maximum allowed."""
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of {self.name}.")
        return super().buy(quantity)
