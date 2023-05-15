"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) == True
        assert product.check_quantity(500) == True
        assert product.check_quantity(0) == True
        assert product.check_quantity(2000) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        initial_quantity = product.quantity
        quantity_to_buy = 100
        product.buy(quantity_to_buy)
        assert product.quantity == initial_quantity - quantity_to_buy

        initial_quantity = product.quantity
        quantity_to_buy = 200
        product.buy(quantity_to_buy)
        assert product.quantity == initial_quantity - quantity_to_buy

        quantity_to_buy = 1001
        with pytest.raises(ValueError):
            product.buy(quantity_to_buy)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        quantity_to_buy = 1001
        with pytest.raises(ValueError):
            product.buy(quantity_to_buy)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_product_add_to_cart(self, product):
        cart = Cart()
        value_to_add = 1
        initial_quantity = 0

        cart.add_product(product)
        assert cart.products[product] == initial_quantity + value_to_add
        initial_quantity += value_to_add

        cart.add_product(product)
        assert cart.products[product] == initial_quantity + value_to_add
        initial_quantity += value_to_add

        value_to_add = 99
        cart.add_product(product, value_to_add)
        assert cart.products[product] == initial_quantity + value_to_add
        initial_quantity += value_to_add

    def test_remove_product(self, product):
        cart = Cart()
        cart.add_product(product, 3)
        initial_product_quantity = cart.products[product]
        quantity_to_remove = 2
        cart.remove_product(product, quantity_to_remove)
        assert cart.products[product] == initial_product_quantity - quantity_to_remove

        cart.remove_product(product)
        assert not product in cart.products

        cart.add_product(product, 3)
        cart.remove_product(product, 4)
        assert not product in cart.products

        cart.add_product(product, 3)
        cart.remove_product(product, 3)
        assert not product in cart.products

    def test_clear_cart(self, product):
        cart = Cart()
        cart.add_product(product, 3)
        cart.add_product(Product("pen", 10, "This is a pen", 100))
        cart.clear()
        assert len(cart.products) == 0

    def test_total_price(self, product):
        cart = Cart()
        cart.add_product(product, 3)
        cart.add_product(Product("pen", 10, "This is a pen", 100), 2)
        assert cart.get_total_price() == 320

    def test_buy_products(self, product):
        cart = Cart()
        product_2 = Product("pen", 10, "This is a pen", 100)
        initial_dictionary = {product: 3, product_2: 5}
        initial_quantity_product = product.quantity
        initial_quantity_product_2 = product_2.quantity

        for key_product, value_quantity in initial_dictionary.items():
            cart.add_product(key_product, value_quantity)
        cart.buy()

        assert product.quantity == initial_quantity_product - initial_dictionary[product]
        assert product_2.quantity == initial_quantity_product_2 - initial_dictionary[product_2]

    def test_buy_product_more_than_quantity_in_store(self, product):
        cart = Cart()
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy()