from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from salon.models import Category, Product, Purchase


# noinspection PyUnresolvedReferences
class PurchaseProcessViewMixin:
    http_method_names = ['post']

    def clear_session_purchase_id(self):
        self.request.session.pop('purchase_id')
        self.request.session.save()

    def get_or_create_purchase(self):
        purchase_id = self.request.session.get('purchase_id')
        if purchase_id:
            try: return Purchase.objects.get(id=purchase_id)
            except: pass
        purchase = Purchase()
        purchase.save()
        self.request.session['purchase_id'] = purchase.id
        return purchase


# noinspection PyUnresolvedReferences
class MainContextMixin(PurchaseProcessViewMixin):
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'purchase': self.get_or_create_purchase(),
        })
        return context


class HistoryView(MainContextMixin, TemplateView):
    template_name = 'history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'done_purchases': Purchase.objects.filter(done=True).order_by('-datetime'),
        })
        return context


class CatalogView(MainContextMixin, TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all(),
        })
        return context


class AddProductToBasketView(PurchaseProcessViewMixin, View):
    def post(self, request, *args, **kwargs):
        purchase = self.get_or_create_purchase()
        product_id = self.kwargs.get('id')
        product = Product.objects.get(id=product_id)
        purchase.basket.add(product)
        purchase.save()
        messages.success(request, f'Товар {product.name} успешно добавлен в корзину')
        return redirect('catalog')


class RemoveProductFromBasketView(PurchaseProcessViewMixin, View):
    def post(self, request, *args, **kwargs):
        purchase = self.get_or_create_purchase()
        purchase_basket_id = self.kwargs.get('id')
        product = Product.objects.get(id=purchase_basket_id)
        purchase.basket.remove(product)
        purchase.save()
        return redirect('catalog')


class DonePurchaseView(PurchaseProcessViewMixin, View):
    def post(self, request, *args, **kwargs):
        purchase = self.get_or_create_purchase()
        purchase.set_done()
        self.clear_session_purchase_id()
        messages.success(request, f'Заказ на сумму {purchase.total_cost_format} успешно создан')
        return redirect('catalog')


class ClearBasketView(PurchaseProcessViewMixin, View):
    def post(self, request, *args, **kwargs):
        purchase = self.get_or_create_purchase()
        purchase.basket.clear()
        purchase.save()
        return redirect('catalog')
