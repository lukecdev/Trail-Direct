from django.contrib import admin
from .models import ProductReview

admin.site.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'body', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'product', 'body')
    actions = ['approve_comments']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
