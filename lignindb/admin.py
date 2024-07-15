from django.contrib import admin
from .models import lignin
from .models import ncbidb
from .models import pagetab
from .models import taxonomytb
from .models import GeneData
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(lignin)

class userDat(admin.ModelAdmin):
    list_display = ('bacteria', 'pathway', 'ph', 'temperature')


@admin.register(ncbidb)
class ncbiDat(admin.ModelAdmin):
    list_display = ('org', 'gene', 'product')

@admin.register(pagetab)
class ncbiDat(admin.ModelAdmin):
    list_display = ('org', 'pathways', 'gene')

@admin.register(taxonomytb)
class ncbiDat(admin.ModelAdmin):
    list_display = ('org', 'comptax', 'taxonomy1')

@admin.register(GeneData)
class ncbiDat(admin.ModelAdmin):
    list_display = ('gene', "organism")