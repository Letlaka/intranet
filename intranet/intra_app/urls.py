from django.urls import path
from intra_app.documents_views import DocumentDownloadView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ict/", views.ict, name="ict"),
    path("hr/", views.hr, name="hr"),
    path("404/", views.error404, name="404"),
        path(
        "download_document/<int:pk>/",
        DocumentDownloadView.as_view(),
        name="download_document"),
]
