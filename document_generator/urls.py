from django.urls import path
from . import views

# URL patterns for the 'document_generator' app.
urlpatterns = [
    path('templates/', views.list_templates, name='list_templates'),
    path('generate/<int:template_id>/', views.generate_document, name='generate_document'),
    path('template/create/', views.create_edit_template, name='create_template'),
    path('template/edit/<int:template_id>/', views.create_edit_template, name='edit_template'),
]
