from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main_app.models import BankBrunch, User


class CreateBankBrunchView(CreateView):
    model = BankBrunch
    fields = ['name']
    template_name = 'registration/create_brunch.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form: ModelForm):
        user = User.objects.get(pk=self.request.user.pk)
        if user.is_administrator:
            form.add_error(None, 'Вы не можете отвечать более чем за один филиал.')
            return self.form_invalid(form)
        bank_brunch = form.save(False)
        bank_brunch.administrator = self.request.user
        return super().form_valid(form)
