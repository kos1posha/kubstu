from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User as DjangoUser

from main_app.models import BankBrunch, Employee, ServiceTicket, User


admin.site.register(ServiceTicket)
admin.site.register(BankBrunch)
admin.site.register(Employee)
admin.site.unregister(Group)
admin.site.unregister(DjangoUser)
admin.site.register(User, UserAdmin)
