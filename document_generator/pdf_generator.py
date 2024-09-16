from reportlab.lib.pagesizes import letter, legal
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.units import inch
from jinja2 import Template

class PDFGenerator:
    """
    Class responsible for generating PDFs from templates and context data.
    """
    def __init__(self, template, context, paper_size='letter'):
        """
        Initialize the PDFGenerator with a template, context, and paper size.
        """
        self.template = template
        self.context = context
        # Set the paper size based on the provided option.
        self.paper_size = letter if paper_size == 'letter' else legal

    def generate(self, output_path):
        """
        Generate the PDF and save it to the specified output path.
        """
        # Render the template content using Jinja2 with the provided context.
        t = Template(self.template.content)
        rendered_content = t.render(self.context)
        # Create a SimpleDocTemplate for the PDF.
        doc = SimpleDocTemplate(
            output_path,
            pagesize=self.paper_size,
            rightMargin=inch,
            leftMargin=inch,
            topMargin=inch,
            bottomMargin=inch
        )
        # Get the default style sheet and select the 'Normal' style.
        styles = getSampleStyleSheet()
        style = styles['Normal']
        # Split the rendered content into paragraphs and create Paragraph objects.
        paragraphs = [Paragraph(p, style) for p in rendered_content.split('\n') if p.strip()]
        # Build the PDF document with the paragraphs.
        doc.build(paragraphs)
