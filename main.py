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

    def add_to_list(self, product): # Метод добавления товара в список товаров категории
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


class ReprMixin:

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, description={self.description})"


class Product(ABC):
    '''
    About Product price, name, description, quontity
    '''

    name: str
    description: str
    price: float
    quontity_in_stock: int
    collor: str

    @abstractmethod
    def __init__(self, name, description, price, quontity_in_stock, collor):
        self.name = name
        self.description = description
        self.price = price
        self.quontity_in_stock = quontity_in_stock
        self.collor = collor

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

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
        print(f"Создан объект: {self.__class__.__name__}")

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
        print(f"Создан объект: {self.__class__.__name__}")


# Создаем объекты Smartphone
iphone = Smartphone("iPhone 15", "The latest iPhone model", 1000, 10, "A17 Bionic", "iPhone 15", "256GB", "black")
samsung = Smartphone("Samsung Galaxy S23", "Flagship Samsung phone", 900, 15, "Snap 8 Gen3", "Galaxy S23", "128GB", "silver")

# Создаем объекты Grass
wheat = Grass("Wheat seeds", "High-quality wheat seeds", 5, 100, "USA", "7 days", "brown")
barley = Grass("Barley seeds", "Premium barley seeds", 4, 80, "Canada", "5 days", "yellow")

# Создаем категории
phones_category = Category("Phones", 'new phone')
seeds_category = Category("Seeds", 'new seeds')

# Добавляем продукты в категории
phones_category.add_to_list(iphone)
phones_category.add_to_list(samsung)
seeds_category.add_to_list(wheat)
seeds_category.add_to_list(barley)

# Проверяем сумму цен продуктов одного типа
total_phone_price = iphone + samsung
print(f"Total price of smartphones: ${total_phone_price}")

total_seed_price = wheat + barley
print(f"Total price of seeds: ${total_seed_price}")
