from django.contrib import admin
from house.models import House, TypeConstruction, Owner

class HouseAdmin(admin.ModelAdmin):
    pass

class TypeConstructionAdmin(admin.ModelAdmin):
    pass

class OwnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(House, HouseAdmin)
admin.site.register(TypeConstruction, TypeConstructionAdmin)
admin.site.register(Owner, OwnerAdmin)
