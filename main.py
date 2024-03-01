from abc import ABC, abstractmethod


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
        if isinstance(product, Product):
            self.__goods.append(product)
            Category.unique_products += 1
        else:
            print("Ошибка: Можно добавлять только объекты типа Product или его наследников.")

    @property
    def goods(self):
        return self.__goods

    def __len__(self):
        return len(self.__goods)

    def __str__(self):
        return f'{self.name}, количество продуктов:{Category.unique_products} шт.'

    def average_price(self):
        total_price = sum(product.price for product in self.__goods)
        total_num_products = len(self.__goods)
        try:
            average_price = total_price / total_num_products
        except ZeroDivisionError:
            print("Ошибка: Нельзя вычислить средний ценник, так как в категории нет товаров.")
            return 0
        return average_price


class ReprMixin:

    #Попытался поменять в smartphone и grass родители не получилось
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f'Создан объект {self.__class__.__name__} ' + ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Product(ReprMixin, BaseProduct):
    '''
    About Product price, name, description, quontity
    '''

    name: str
    description: str
    price: float
    quontity_in_stock: int
    collor: str

    def __init__(self, name, description, price, quontity_in_stock, collor):
        self.name = name
        self.description = description
        self.price = price
        self.quontity_in_stock = quontity_in_stock
        self.collor = collor
        super().__init__()

    @classmethod
    def add_product(cls, name, description, price, quontity_in_stock, color):
        if quontity_in_stock == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен.')
        return cls(name, description, price, quontity_in_stock, color)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректно.")
        else:
            self._price = value

    def __str__(self):
        return f'Продукт: {self.name}, Цена: {self.price} руб., Остаток: {self.quontity_in_stock} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            total_value = (self.price * self.quontity_in_stock) + (other.price * other.quontity_in_stock)
            return total_value
        else:
            raise ValueError('Ошибка типа! Нельзя складывать продукты разных типов.')


class Smartphone(Product, ReprMixin):
    """
    Smartphone
    """
    performance: float
    model: str
    memory_capacity: int

    def __init__(self, name, description, price, quontity_in_stock, performance, model, memory_capacity, color):
        super().__init__(name, description, price, quontity_in_stock, color)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._price = value
        else:
            raise ValueError("Цена должна быть положительным числом")


class Grass(Product, ReprMixin):
    """
    Grass
    """
    country_of_manufacture: str
    germination_time: int

    def __init__(self, name, description, price, quontity_in_stock, country_of_manufacture, germination_time, color):
        super().__init__(name, description, price, quontity_in_stock, color)
        self.country_of_manufacture = country_of_manufacture
        self.germination_time = germination_time


if __name__ == "__main__":
    ################### TASK 1 ###################################
    # try:
    #     product1 = Product.add_product("Товар 1", "Описание товара 1", 100, 5, 'yellow')
    #     product2 = Product.add_product("Товар 2", "Описание товара 2", 150, 0, 'blue')  # Попытка добавить товар с нулевым количеством
    # except ValueError as e:
    #     print(f"Исключение: {e}")
    # else:
    #     print("Товары успешно добавлены.")


    ################### TASK 2 ##################################
    # # Создаем экземпляр категории
    # category1 = Category("Категория 1", "Описание категории 1")
    #
    # # Добавляем несколько товаров в категорию
    # product1 = Product.add_product("Товар 1", "Описание товара 1", 100, 5, "красный")
    # product2 = Product.add_product("Товар 2", "Описание товара 2", 150, 3, "синий")
    # category1.add_to_list(product1)
    # category1.add_to_list(product2)
    #
    # # Вызываем метод для подсчета средней цены
    # average_price = category1.average_price()
    # print(f"Средний ценник всех товаров в категории: {average_price} руб.")



