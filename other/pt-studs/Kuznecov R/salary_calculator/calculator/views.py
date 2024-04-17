from decimal import Decimal

from django.forms import model_to_dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, FormView, UpdateView

from calculator.forms import CalculateSalaryForm, MonthChoices
from calculator.models import DefaultTaxes, Employee, Position


class BaseTemplateContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'positions': Position.objects.all(),
            'employees': Employee.objects.all(),
        })
        return context


class CalculateSalaryView(BaseTemplateContextMixin, FormView):
    template_name = 'calculate_salary.html'
    form_class = CalculateSalaryForm

    def form_valid(self, form):
        def q(v): return v.quantize(Decimal('0.00'))

        def d(v): return q(Decimal.from_float(v))

        def f(v): r, k = q(v).__str__().split('.'); return f'{r}.{k} рублей'

        employee, personal_taxes, pensionary_taxes, month, worked_days, missed_days, bonus = form.cleaned_data.values()
        work_ratio = 1 - d(missed_days if missed_days is not None else 0) / d(worked_days)
        worked_salary = q(employee.position.salary * work_ratio)
        worked_salary_plus = worked_salary + (bonus or 0)
        personal_taxes_value = worked_salary * personal_taxes / 100
        pensionary_taxes_value = worked_salary * pensionary_taxes / 100
        taxed_salary = q(worked_salary_plus - personal_taxes_value)
        taxed_labor = q(worked_salary_plus + pensionary_taxes_value)
        context = self.get_context_data()
        context.update({
            'employee': employee,
            'bonus': f(bonus) if bonus else 'Отсутствуют',
            'month': MonthChoices.labels[int(month)],
            'worked_salary': f(worked_salary_plus),
            'personal_taxes_value': f(personal_taxes_value),
            'pensionary_taxes_value': f(pensionary_taxes_value),
            'taxed_salary': f(taxed_salary),
            'taxed_labor': f(taxed_labor),
            'total_taxes': f(personal_taxes_value + pensionary_taxes_value),
        })
        return render(self.request, 'calculate_salary_report.html', context)


class CreatePositionView(BaseTemplateContextMixin, CreateView):
    model = Position
    fields = '__all__'
    template_name = 'create_position.html'
    success_url = reverse_lazy('calculate_salary')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs['placeholder'] = 'Введите название должности'
        form.fields['salary'].label = 'Заработная ставка'
        form.fields['salary'].widget.attrs['placeholder'] = 'Введите ставку за месяц'
        return form


class UpdatePositionView(BaseTemplateContextMixin, UpdateView):
    model = Position
    fields = '__all__'
    template_name = 'update_position.html'
    success_url = reverse_lazy('calculate_salary')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'position_pk': self.kwargs['pk']})
        return context

    def get_object(self, queryset=None):
        return Position.objects.filter(pk=self.kwargs.get('pk')).first()

    def get_initial(self):
        obj = self.get_object()
        initial = model_to_dict(obj, fields=['name'])
        initial['salary'] = obj.salary_initial
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs['placeholder'] = 'Введите название должности'
        form.fields['salary'].label = 'Заработная ставка'
        form.fields['salary'].widget.attrs['placeholder'] = 'Введите ставку за месяц'
        return form


class DeletePositionView(DeleteView):
    success_url = reverse_lazy('calculate_salary')

    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Position.objects.filter(pk=self.kwargs.get('pk')).first()


class CreateEmployeeView(BaseTemplateContextMixin, CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'create_employee.html'
    success_url = reverse_lazy('calculate_salary')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        form.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        form.fields['position'].empty_label = 'Выберите должность'
        return form


class UpdateEmployeeView(BaseTemplateContextMixin, UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'update_employee.html'
    success_url = reverse_lazy('calculate_salary')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'employee_pk': self.kwargs['pk']})
        return context

    def get_object(self, queryset=None):
        return Employee.objects.filter(pk=self.kwargs.get('pk')).first()

    def get_initial(self):
        obj = self.get_object()
        initial = model_to_dict(obj, exclude=['id'])
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        form.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        form.fields['position'].empty_label = 'Выберите должность'
        return form


class DeleteEmployeeView(DeleteView):
    success_url = reverse_lazy('calculate_salary')

    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Employee.objects.filter(pk=self.kwargs.get('pk')).first()


class UpdateDefaultTaxesView(BaseTemplateContextMixin, UpdateView):
    model = DefaultTaxes
    fields = '__all__'
    template_name = 'update_taxes.html'
    success_url = reverse_lazy('update_taxes')

    def get_object(self, queryset=None):
        return DefaultTaxes.objects.filter(pk=1).first()

    def get_initial(self):
        obj = self.get_object()
        initial = model_to_dict(obj, exclude=['id'])
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['personal'].widget.attrs['placeholder'] = 'Налог на доходы физических лиц'
        form.fields['personal'].help_text = 'Вычитается из ставки сотрудника.'
        form.fields['pensionary'].widget.attrs['placeholder'] = 'Пенсионные отчисления'
        form.fields['pensionary'].help_text = 'Не вычитается из ставки сотрудника.'
        return form
