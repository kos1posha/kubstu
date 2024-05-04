from db.connection import DBConnection


class DatabaseModel:
    def __init__(self, table, key=None):
        self._table = table
        self._key = key or 'id'
        self._connection = DBConnection()

    def all(self):
        return self._connection.select_rows(self._table)

    def get_by_id(self, id):
        try:
            return self._connection.select_rows(self._table, f'id = "{id}"')[0]
        except:
            return None

    def get(self, *args, **kwargs):
        key_value = kwargs.get(self._key) or args[0]
        try:
            return self._connection.select_rows(self._table, f'{self._key} = "{key_value}"')[0]
        except:
            return None

    def insert(self, *args, **kwargs):
        value = kwargs.get('value') or args[0]
        return self._connection.insert_rows(self._table, value)

    def remove(self, *args, **kwargs):
        key_value = kwargs.get(self._key) or args[0]
        return self._connection.delete_rows(self._table, f'{self._key} = "{key_value}"')


class Categories(DatabaseModel):
    def __init__(self):
        super().__init__('categories', 'title')

    def get(self, title):
        return super().get(title)

    def insert(self, title, description=None):
        return super().insert((title, description or 'Описание отсутствует'))

    def remove(self, title):
        return super().remove(title)


class Products(DatabaseModel):
    def __init__(self):
        super().__init__('products', 'code')

    def get(self, code):
        return super().get(code)

    def insert(self, code, title, category, on_storage_count, weight, price, description=None, has_complectation=None):
        description = description or 'Описание отсутствует'
        has_complectation = has_complectation or 0
        category_id = Categories().get(category)[0]
        return super().insert((code, title, category_id, on_storage_count, weight, price, description, has_complectation))

    def remove(self, code):
        return super().remove(code)

    def update_count(self, code, count):
        return self._connection.execute(f'UPDATE products SET on_storage_count = {count} WHERE code = {code}')

    def of_category(self, category_title):
        category_id = Categories().get(category_title)[0]
        return self._connection.execute(f'SELECT * FROM products WHERE category_id = {category_id}')

    def by_categories(self):
        category_list = Categories().all()
        return {c_row: self.of_category(c_row[1]) for c_row in category_list}


class __comeHistory(DatabaseModel):
    def get(self, id):
        return super().get(id)

    def insert(self, product_code, count, dt):
        product = Products().get(product_code)
        category = Categories().get_by_id(product[3])
        return super().insert((dt, product[1], product[2], category[1], product[6], count))

    def remove(self, id):
        return super().remove(id)


class IncomeHistory(__comeHistory):
    def __init__(self):
        super().__init__('income_history', 'id')


class OutcomeHistory(__comeHistory):
    def __init__(self):
        super().__init__('outcome_history', 'id')


categories = Categories()
products = Products()
income_history = IncomeHistory()
outcome_history = OutcomeHistory()
