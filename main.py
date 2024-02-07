class Category:
    '''
    Category
    '''
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
    Product
    '''
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