from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_so', 'created_at', 'updated_at')
    search_fields = ('title_en', 'content_en')
    list_filter = ('created_at', 'updated_at')
    fields = ('title_en', 'content_en', 'title_so', 'content_so')  # Show both EN and SO fields
    readonly_fields = ('title_so', 'content_so')  # Prevent editing translated fields

    def get_queryset(self, request):
        # Optional: Restrict writers to their own articles
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(author=request.user)
        return qs