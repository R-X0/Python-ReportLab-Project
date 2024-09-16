from jinja2 import Environment, BaseLoader

class TemplateParser:
    """
    Class responsible for parsing and rendering templates using Jinja2.
    """
    def __init__(self, template):
        """
        Initialize the TemplateParser with a template string.
        """
        self.template = template

    def render(self, context):
        """
        Render the template with the provided context.
        """
        # Create a Jinja2 environment without any loader.
        env = Environment(loader=BaseLoader())
        # Load the template from the provided string.
        template = env.from_string(self.template)
        # Render the template with the context.
        return template.render(context)
