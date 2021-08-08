from django.contrib import admin
from .models import contact,product,recentproject,career,jobopening
# Register your models here.
admin.site.register(contact)
admin.site.register(product)
admin.site.register(recentproject)
admin.site.register(career)
admin.site.register(jobopening)