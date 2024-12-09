from django.contrib import admin
from .models import ShopItem, ShopItemImage


class ShopItemImageInline(admin.TabularInline):
    model = ShopItemImage
    extra = 1  # Allows adding one additional image inline in the admin

@admin.action(description="Delete selected images")
def delete_selected_images(modeladmin, request, queryset):
    for image in queryset:
        image.delete_image()

@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')
    inlines = [ShopItemImageInline]
    # actions = [delete_selected_images]

@admin.register(ShopItemImage)
class ShopItemImageAdmin(admin.ModelAdmin):
    list_display = ('shop_item', 'image_name')
    actions = [delete_selected_images]


