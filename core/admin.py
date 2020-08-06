from django.contrib import admin
from .models import Profile, Gallery


admin.site.register(Profile)
admin.site.register(Gallery)
admin.site.site_header = "E-bizCard Admin"
admin.site.site_title = "E-BizCard Admin Portal"
admin.site.index_title = "Welcome to E-BizCard Admin Portal"
