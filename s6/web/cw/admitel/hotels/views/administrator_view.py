from django.shortcuts import redirect
from django.views.generic import TemplateView

from hotels.models import Hotel, Branch, Room


class AdministratorView(TemplateView):
    template_name = 'administrator_panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return context
        branch = Branch.objects.get(administrator__user=self.request.user)
        context['branch'] = branch
        context['rooms'] = Room.objects.filter(branch=branch)
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            hotel_id = request.session.get('hotel_id')
            if hotel_id:
                if Hotel.objects.filter(id=hotel_id).first():
                    return redirect('hotels:manage')
            return redirect('welcome')
        return super().dispatch(request, *args, **kwargs)
