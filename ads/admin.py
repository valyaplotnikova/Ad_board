from django.contrib import admin

from ads.models import Ad, Review


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'author', 'created_at', )
    list_filter = ('title', 'price', 'author',)
    search_fields = ('title', 'price', 'author',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'ad', 'author', 'created_at', )
    list_filter = ('ad', 'author', 'created_at',)
    search_fields = ('ad', 'author', 'created_at',)
