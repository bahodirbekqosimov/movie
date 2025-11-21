from django.contrib import admin
from .models import Movi

@admin.register(Movi)
class MoviAdmin(admin.ModelAdmin):
    list_display = ['title',"rejissyor",]
    search_fields = ("title", "rejissyor",'desc')
    list_filter = ('category',)
    

    
    