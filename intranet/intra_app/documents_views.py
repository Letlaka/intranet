from django.views.generic.base import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document
from .permissions import AccessDocumentPermission

class DocumentDownloadView(View):
    permission_classes = [AccessDocumentPermission]


    def get(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        return redirect(document.document_file.url)