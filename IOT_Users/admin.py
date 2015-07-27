from django.contrib import admin
from IOT_Users.models import *

class IOTUserAdmin(admin.ModelAdmin):
	pass

admin.site.register(IOTUser, IOTUserAdmin)