from django.db import models
from ckeditor.fields import RichTextField

class DocumentTemplate(models.Model):
    """
    Model representing a document template.
    """
    name = models.CharField(max_length=255)
    content = RichTextField()
    paper_size = models.CharField(
        max_length=20,
        choices=[
            ('letter', 'US Letter'),
            ('legal', 'US Legal'),
        ],
        default='letter'
    )

    def __str__(self):
        return self.name
