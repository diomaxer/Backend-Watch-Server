from django.contrib import admin
from .models import Images ,Sex, Product, WatchType, Brand, Equipment, MehType, Condition, Colour,\
    Material, Glass, Waterproof, Numbers, ZipType
# Register your models here.

admin.site.register(Product)
admin.site.register(Sex)
admin.site.register(WatchType)
admin.site.register(Brand)
admin.site.register(Equipment)
admin.site.register(MehType)
admin.site.register(Condition)
admin.site.register(Colour)
admin.site.register(Material)
admin.site.register(Glass)
# admin.site.register(BracerMaterial)
# admin.site.register(BracerColour)
# admin.site.register(BezelMaterial)
admin.site.register(Waterproof)
admin.site.register(Numbers)
admin.site.register(ZipType)
# admin.site.register(ZipMaterial)

# Images
admin.site.register(Images)