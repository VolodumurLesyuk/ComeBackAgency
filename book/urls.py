from django.urls import path
from .views import BulkImportBooksView

urlpatterns = [
    path('import/', BulkImportBooksView.as_view(), name='bulk_import_books'),
]