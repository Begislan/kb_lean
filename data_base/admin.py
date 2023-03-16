from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class NameCategiriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class RazAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class GlavAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ThemeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("theme",)}


class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("fio",)}


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(NameCategories, CategoriesAdmin)
admin.site.register(Raz, RazAdmin)
admin.site.register(Glav, GlavAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(News)
admin.site.register(About, AboutAdmin)
