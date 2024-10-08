# Document Generator Proof of Concept

This project is a proof of concept for generating legal documents using Django, ReportLab, and Jinja2. Users can create document templates using a WYSIWYG editor (CKEditor), insert dynamic fields from Django models, and generate PDFs that are properly formatted for US Letter or Legal paper sizes.

## Features

- **WYSIWYG Editor**: Create and edit document templates using CKEditor.
- **Dynamic Fields**: Insert fields from Django models using Jinja2 syntax.
- **Automatic Field Inclusion**: New model fields are automatically available in templates without manual registration.
- **PDF Generation**: Generate PDFs with proper formatting using ReportLab.
- **Paper Size Selection**: Choose between US Letter and Legal paper sizes.


Usage
Access the application at http://localhost:8000/document_generator/.
Create, edit, and manage document templates.
Insert dynamic fields from Django models into your templates.
Generate PDFs from templates with proper formatting.

Project Structure
docgen_project/: Main Django project directory.
document_generator/: Django app for document generation.
templates/: Directory containing HTML templates.
static/: Static files for the project.
media/: Uploaded media files.

Files Overview

asgi.py: ASGI config for the project.
wsgi.py: WSGI config for the project.
settings.py: Django settings for the project.
urls.py: URL configurations.
models.py: Defines the DocumentTemplate model.
views.py: Contains view functions for the app.
forms.py: Forms used in the application.
pdf_generator.py: Logic for generating PDFs using ReportLab.
template_language.py: Handles template parsing with Jinja2.
model_fields.py: Retrieves all model fields for dynamic insertion.
admin.py: Admin configurations (currently minimal).
apps.py: App configuration for document_generator.
tests.py: Placeholder for tests (currently empty).#   P y t h o n - R e p o r t L a b - P r o j e c t  
 