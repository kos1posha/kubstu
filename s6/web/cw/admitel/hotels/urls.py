from django.urls import path

from hotels.views import AdministratorView, HotelCreateView, ManagerView, BranchCreateView, BranchDeleteView, RoomCreateView, RoomDeleteView, AdministratorRegistrationView, AdministratorLoginView, HotelLoginView, AdministratorLogoutView, HotelLogoutView, RoomToggleView

app_name = 'hotels'

urlpatterns = [
    path('', AdministratorView.as_view(), name='administrator'),
    path('hotels/new/', HotelCreateView.as_view(), name='new'),
    path('hotels/manage/', ManagerView.as_view(), name='manage'),
    path('branches/new/', BranchCreateView.as_view(), name='new_branch'),
    path('branches/delte/', BranchDeleteView.as_view(), name='delete_branch'),
    path('rooms/new/', RoomCreateView.as_view(), name='new_room'),
    path('rooms/delete/', RoomDeleteView.as_view(), name='delete_room'),
    path('rooms/toggle', RoomToggleView.as_view(), name='toggle_room'),
    path('admininstrators/register/<int:branch_id>/', AdministratorRegistrationView.as_view(), name='register_admin'),
    path('login/administrator/', AdministratorLoginView.as_view(), name='login_a'),
    path('login/hotel/', HotelLoginView.as_view(), name='login_h'),
    path('logout/administrator/', AdministratorLogoutView.as_view(), name='logout_a'),
    path('logout/hotel/', HotelLogoutView.as_view(), name='logout_h'),
]
