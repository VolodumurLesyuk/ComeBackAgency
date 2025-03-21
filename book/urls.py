from django.urls import path
from .views import BulkImportBooksView, ExportBooksView

urlpatterns = [
    path('import/', BulkImportBooksView.as_view(), name='bulk_import_books'),
    path('export/', ExportBooksView.as_view(), name='export_books'),
]