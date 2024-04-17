from django.apps import apps
from django.contrib.auth import get_user_model
from django.db.models import CASCADE, ForeignKey, Model, TextField, CharField


user_model = get_user_model()


class Storage(Model):
    class Meta:
        verbose_name = 'Хранилище'
        verbose_name_plural = 'Хранилища'

    name = CharField(verbose_name='Название хранилища', max_length=30)
    description = TextField(verbose_name='Описание', help_text='При необходимости, вы можете указать дополнительную информацию', blank=True, null=True, max_length=80)
    user = ForeignKey(to=get_user_model(), verbose_name='Владелец', on_delete=CASCADE)

    def __str__(self):
        return f'{self.name} ({self.user})'

    @property
    def products(self):
        Product = apps.get_model('sklad_app', 'Product')
        return Product.objects.filter(storage=self)

    @property
    def product_unique_count(self):
        return len(self.products)

    @property
    def product_total_count(self):
        counts = [product.count for product in self.products]
        return sum(counts)

    @property
    def products_weight(self):
        weights = [product.total_weight for product in self.products]
        return sum(weights)
