from django.contrib import admin

from .models import Menu, UserDetail, ItemSize


# Register your models here.
class UserDetailAdmin(admin.ModelAdmin):
    model = UserDetail
    filter_horizontal = ("cart",)
    list_display = ["get_user", "address", "city", "province", "country"]

    def get_user(self, obj):
        return obj.user.username


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ["item", "base_price"]


admin.site.register(UserDetail, UserDetailAdmin)
admin.site.register(ItemSize)
admin.site.register(Menu, MenuAdmin)
