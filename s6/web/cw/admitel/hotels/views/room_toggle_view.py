from django.shortcuts import redirect
from django.views import View

from hotels.models import Room


class RoomToggleView(View):
    def post(self, request):
        room_id = request.POST.get('id')
        if not room_id:
            return redirect('hotels:administrator')
        room = Room.objects.get(id=room_id)
        room.is_busy = not room.is_busy
        room.save()
        return redirect('hotels:administrator')
