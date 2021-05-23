from django.contrib import admin
from .models import Images, Sex, Product, WatchType, Brand, Equipment, MehType, Condition, Colour,\
    Material, Glass, Waterproof, Numbers, ZipType
from users.models import CustomUser


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'price', 'user', )


# Product
admin.site.register(Product, ProductAdmin)
admin.site.register(Sex)
admin.site.register(WatchType)
admin.site.register(Brand)
admin.site.register(Equipment)
admin.site.register(MehType)
admin.site.register(Condition)
admin.site.register(Colour)
admin.site.register(Material)
admin.site.register(Glass)
admin.site.register(Waterproof)
admin.site.register(Numbers)
admin.site.register(ZipType)


# Images
class ImageAdmin(admin.ModelAdmin):
    list_display = ('ad', 'id', 'image')


admin.site.register(Images, ImageAdmin)
