from django.contrib import admin
from feed.models import Record

# Register your models here.

# admin.site.register(Record)

@admin.register(Record)
class RecordAdminPanel(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub', 'state')
    list_filter = ('state', 'created_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author', )
    date_hierarchy = 'pub'
    ordering = ('-state',)
