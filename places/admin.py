from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


class ImageInline(SortableTabularInline):
    model = Image
    extra = 3
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.get_url(),
                width=200,
                height=200,
            )
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (ImageInline,)
