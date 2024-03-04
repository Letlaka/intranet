from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ("ref_number", "document_name")  # Shows both "ref_number" and "name" fields
    list_display_links = ("ref_number",)  # Makes only "ref_number" clickable (optional)
    ordering = ["ref_number"]  # Sorts by "ref_number" in ascending order

admin.site.register(Document, DocumentAdmin)
