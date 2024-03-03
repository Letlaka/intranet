from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

class AccessDocumentPermission(PermissionRequiredMixin):
    """
    Permission to access a specific document.
    """

    permission_required = 'intra_app.access_document'

    def has_permission(self, request, view, obj):
        return super().has_permission(request, view, obj)