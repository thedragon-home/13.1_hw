class Category:
    '''
    About Category name, description, goods
    '''

    name: str
    description: str
    goods: list

    total_num_in_categories = 0
    unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods
        Category.total_num_in_categories += 1
        for product in goods:
            Category.unique_products += 1

class Product:
    '''
    About Product price, name, description, quontity
    '''

    name: str
    description: str
    price: float
    quontity_in_stock: int

    def __init__(self, name, descriotion, price, quontity_in_stock):
        self.name = name
        self.description = descriotion
        self.price = price
        self.quontity_in_stock = quontity_in_stock

# if __name__ == '__main__':
#     product = Product('Apple', 'red apples', '200', '10')
#
#     print(product)
#     print(product.name)
#     print(product.description)
#     print(product.price)
#     print(product.quontity_in_stock)