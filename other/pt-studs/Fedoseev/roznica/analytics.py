import matplotlib as mpl
import matplotlib.pyplot as plt

from db import models as dbm


mpl.rcParams['toolbar'] = 'None'


def count_numbers_by_range(numbers):
    result = {}
    for i in range(0, max(numbers), 10000):
        result[str(i + 10000)] = sum(1 for num in numbers if i <= num < i + 10000)
    return result


def product_count_by_category():
    category_counts = {k[1]: len(v) for k, v in dbm.products.by_categories().items()}
    categories = list(category_counts.keys())
    quantities = list(category_counts.values())

    plt.style.use('dark_background')
    plt.bar(range(len(categories)), quantities, color='y')
    plt.xlabel('Категории')
    plt.ylabel('Количество продуктов')
    plt.title('Количество продуктов на складе по категориям')
    plt.yticks(range(max(quantities) + 2))
    plt.xticks(range(len(categories)), categories)
    plt.gcf().canvas.manager.set_window_title('Количество продуктов на складе по категориям')
    plt.show()


def product_price_distribution():
    price_products_count = count_numbers_by_range([product[6] for product in dbm.products.all()])
    keys, values = list(price_products_count.keys()), list(price_products_count.values())

    plt.style.use('dark_background')
    plt.bar(keys, values, color='g', alpha=0.5)
    plt.title('Распределение цен на продукты')
    plt.xlabel('Цена (₽)')
    plt.yticks(range(max(values) + 1))
    plt.ylabel('Количество продуктов')
    plt.gcf().canvas.manager.set_window_title('Распределение цен на продукты')
    plt.show()


def total_weight_by_category():
    weights_by_category = {k[1]: sum(p[4] * p[5] for p in v) for k, v in dbm.products.by_categories().items()}
    keys, values = list(weights_by_category.keys()), list(weights_by_category.values())

    plt.style.use('dark_background')
    plt.bar(keys, values, color='b', alpha=0.5)
    plt.title('Суммарный вес продуктов по категориям')
    plt.xlabel('Категории')
    plt.yticks(range(0, max(values) + 1, 1000))
    plt.ylabel('Вес (гр.)')
    plt.gcf().canvas.manager.set_window_title('Суммарный вес продуктов по категориям')
    plt.show()


def average_price_by_category():
    price_by_category = {k[1]: sum(p[4] * p[6] for p in v) for k, v in dbm.products.by_categories().items()}
    keys, values = list(price_by_category.keys()), list(price_by_category.values())

    plt.style.use('dark_background')
    plt.fill_between(keys, values, color='r', alpha=0.5)
    plt.title('Средняя цена продуктов по категориям')
    plt.xlabel('Категории')
    plt.yticks(range(0, max(values) + 1, 10000))
    plt.ylabel('Цена')
    plt.gcf().canvas.manager.set_window_title('Средняя цена продуктов по категориям')
    plt.show()
