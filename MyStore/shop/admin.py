from django.contrib import admin


from .models import Category, Product, Team, AboutUs, Blog, Promotion, Insta, Gallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    preserve_filters = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    ...


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    ...


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    ...


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    ...


@admin.register(Insta)
class InstaAdmin(admin.ModelAdmin):
    ...


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    ...
