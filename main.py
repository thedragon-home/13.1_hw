class Category:
    '''
    About Category name, description, goods
    '''

    name: str
    description: str
    goods: list

    total_num_in_categories = 0
    unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__goods = []
        Category.total_num_in_categories += 1

    def add_to_list(self, product):  # Метод добавления товара в список товаров категории
        self.__goods.append(product)
        Category.unique_products += 1

    @property
    def goods(self):
        result = []
        for product in self.__goods:
            result.append(
                f'Продукт: {product.name}, Цена: {product.price} руб., Остаток: {product.quontity_in_stock} шт.')
        return result

class Product:
    '''
    About Product price, name, description, quontity
    '''

    name: str
    description: str
    price: float
    quontity_in_stock: int

    def __init__(self, name, description, price, quontity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quontity_in_stock = quontity_in_stock

    @classmethod
    def add_product(cls, name, description, price, quontity_in_stock):
        return cls(name, description, price, quontity_in_stock)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректно.")
        else:
            self._price = value

# # Создание объектов категории и товаров
# category1 = Category("Electronics", "Category for electronic devices")
# product1 = Product.add_product("Laptop", "Powerful laptop", 1500.0, 10)
# product2 = Product.add_product("Smartphone", "Latest smartphone model", 800.0, 20)
#
# # Добавление товаров в категорию и вывод информации о товарах в категории
# category1.add_to_list(product1)
# category1.add_to_list(product2)
#
# # Вывод списка товаров в категории
# for product_info in category1.goods:
#     print(product_info)
