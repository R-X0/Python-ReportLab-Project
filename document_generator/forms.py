from django import forms
from .models import DocumentTemplate
from ckeditor.widgets import CKEditorWidget

class DocumentTemplateForm(forms.ModelForm):
    """
    Form for creating and editing DocumentTemplate instances.
    """
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = DocumentTemplate
        fields = ['name', 'content', 'paper_size']
