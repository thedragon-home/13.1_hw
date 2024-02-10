import pytest
from main import Category, Product


@pytest.fixture
def category_example():
    return Category("Electronics", "Category for electronic devices")

@pytest.fixture
def product_example():
    return Product.add_product("Laptop", "Powerful laptop", 1500.0, 10)

def test_category(category_example):
    assert category_example.name == 'Electronics'
    assert category_example.description == 'Category for electronic devices'

def test_product(product_example):
    assert product_example.name == 'Laptop'
    assert product_example.description == 'Powerful laptop'
    assert product_example.price == 1500.0
    assert product_example.quontity_in_stock == 10
