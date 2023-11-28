from django.contrib import admin
from .models import product, Contact,Resume

    
admin.site.register(Resume)

    
admin.site.register(product)


admin.site.register(Contact)