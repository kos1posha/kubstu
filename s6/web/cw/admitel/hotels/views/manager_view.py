from django.shortcuts import redirect
from django.views.generic import ListView

from hotels.models import Hotel, Branch


class ManagerView(ListView):
    template_name = 'manager_panel.html'

    def get_queryset(self):
        hotel_id = self.request.session.get('hotel_id')
        hotel = Hotel.objects.filter(id=hotel_id).first()
        self.extra_context = {'hotel': hotel}
        if not hotel:
            return redirect('hotels:new')
        return Branch.objects.filter(hotel=hotel)
