import tempfile
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from django.contrib import messages
from .models import DocumentTemplate
from .forms import DocumentTemplateForm
from .pdf_generator import PDFGenerator
from .model_fields import get_all_model_fields

def generate_document(request, template_id):
    """
    View to generate a PDF document from a template.
    """
    try:
        # Retrieve the specified template.
        template = get_object_or_404(DocumentTemplate, id=template_id)
        # Get all model fields for context.
        context = get_all_model_fields()
        # Add the current user to the context if authenticated.
        context['current_user'] = request.user if request.user.is_authenticated else None
        # Create a temporary file for the PDF output.
        with tempfile.NamedTemporaryFile(mode='wb', suffix='.pdf', delete=False) as tmp_file:
            tmp_filename = tmp_file.name
        # Initialize the PDF generator with the template and context.
        generator = PDFGenerator(template, context, template.paper_size)
        # Generate the PDF and save it to the temporary file.
        generator.generate(tmp_filename)
        # Open the PDF file for reading.
        pdf_file = open(tmp_filename, 'rb')
        # Create a file response to send the PDF to the user.
        response = FileResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{template.name}.pdf"'
        # Ensure the temporary file is deleted after the response is sent.
        response._resource_closers.append(lambda: os.unlink(tmp_filename))
        return response
    except DocumentTemplate.DoesNotExist:
        # Handle the case where the template does not exist.
        messages.error(request, "Template not found.")
        return redirect('list_templates')
    except PermissionError:
        # Handle permission errors when writing the PDF file.
        messages.error(request, "Permission denied when writing the PDF file.")
        return redirect('list_templates')
    except Exception as e:
        # Handle any other exceptions that may occur.
        messages.error(request, f"An error occurred while generating the PDF: {str(e)}")
        return redirect('list_templates')

def create_edit_template(request, template_id=None):
    """
    View to create or edit a document template.
    """
    # If a template ID is provided, retrieve the existing template.
    if template_id:
        template = get_object_or_404(DocumentTemplate, id=template_id)
    else:
        template = None
    if request.method == 'POST':
        # Initialize the form with POST data and the template instance.
        form = DocumentTemplateForm(request.POST, instance=template)
        if form.is_valid():
            # Save the form data to create or update the template.
            form.save()
            messages.success(request, "Template saved successfully.")
            return redirect('list_templates')
    else:
        # Initialize the form with the existing template instance.
        form = DocumentTemplateForm(instance=template)
    # Get all available model fields to display to the user.
    available_fields = get_all_model_fields()
    return render(request, 'document_generator/create_edit_template.html', {
        'form': form,
        'available_fields': available_fields,
    })

def list_templates(request):
    """
    View to list all document templates.
    """
    # Retrieve all templates from the database.
    templates = DocumentTemplate.objects.all()
    return render(request, 'document_generator/list_templates.html', {'templates': templates})
