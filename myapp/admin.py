from django.contrib import admin
from .models import User,Contact,Event,Book_Event
# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(Book_Event)