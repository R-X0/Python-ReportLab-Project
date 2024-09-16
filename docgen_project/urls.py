from django.contrib import admin
from django.urls import path, include

# URL patterns for the project.
urlpatterns = [
    path('admin/', admin.site.urls),
    # Include URLs from the 'document_generator' app.
    path('document_generator/', include('document_generator.urls')),
]
