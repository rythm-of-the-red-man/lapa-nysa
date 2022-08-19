from django.contrib import admin

from adoptions.models import Animal
from adoptions.models import Photo
from django.utils.safestring import mark_safe

class PhotoTabularInline(admin.TabularInline):
    model = Photo
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        # ex. the name of column is "image"
        if obj.image:
            return mark_safe(
                '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(
                    obj.image_url
                )
            )
        else:
            return '(No image)'

    image_preview.short_description = 'Preview'
# Register your models here.
@admin.register(Animal)
class AminalAdmin(admin.ModelAdmin):
    list_display = ['name','breed','age','sex','size','spice']
    search_fields = ["name"]
    list_filter=['spice','size']
    inlines = [PhotoTabularInline]

