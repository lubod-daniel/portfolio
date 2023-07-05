from django.contrib import admin
from .models import *

# Register your models here.
class folioadmin (admin.ModelAdmin):
   list_display=('title', 'slug', 'from_date', 'to_date', )
   list_filter=('title',)
   prepopulated_fields={'slug':('title',)}
admin.site.register(project)
admin.site.register(image)
admin.site.register(employment)
admin.site.register(qualification)
admin.site.register(professional_course)
admin.site.register(responsibility)
admin.site.register(skill)
admin.site.register(VisitorMessage)