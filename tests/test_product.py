import pytest
from main import Category, Product


@pytest.fixture
def category_example():
    return Category('Fruits', 'different kind of fruits', ['apple', 'banana', 'orange'])

@pytest.fixture
def product_example():
    return Product('Apple', 'red apples', '200', '10')

def test_category(category_example):
    assert category_example.name == 'Fruits'
    assert category_example.description == 'different kind of fruits'
    assert category_example.goods == ['apple', 'banana', 'orange']

def test_product(product_example):
    assert product_example.name == 'Apple'
    assert product_example.description == 'red apples'
    assert product_example.price == '200'
    assert product_example.quontity_in_stock == '10'
