import pytest
from products import Product


def test_create_normal_product():
    #Test that creating a normal product works.
    product = Product("Laptop", 1200, 5)
    assert product.name == "Laptop"
    assert product.price == 1200
    assert product.quantity == 5
    assert product.is_active() is True

def test_create_product_with_invalid_details():
    #Test a product with invalid details (empty name, negative price)
    invalid_data = [
        ("", 1200, 5),  # Invalid name
        ("Invalid Product", -5, 5),  # Negative price
        ("Invalid Product", 1200, -1)  # Negative quantity
    ]

    for name, price, quantity in invalid_data:
        with pytest.raises(ValueError, match="Invalid product details."):
            Product(name, price, quantity)

def test_product_becomes_inactive_when_quantity_reaches_zero():
    #Test when product is quantity 0, is inactive
    product = Product("Test Product", 1200, 1)
    product.buy(1)
    assert product.is_active() is False

def test_product_purchase_modifies_quantity_and_returns_output():
    #Test that product purchase modifies the quantity and returns the right output
    product = Product("Test Product", 1200, 5)
    cost = product.buy(2)
    assert cost == 2400  # 2 * 1200
    assert product.quantity == 3

def test_buying_larger_quantity_than_exists_invokes_exception():
    #Test that buying a larger quantity than exists invokes exception
    product = Product("Test Product", 1200, 3)
    with pytest.raises(Exception, match="Not enough quantity available."):
        product.buy(5)