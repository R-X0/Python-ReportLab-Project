# your_project/jinja2_environment.py

from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

def environment(**options):
    # Create a Jinja2 Environment with the given options
    env = Environment(**options)
    
    # Add global functions and variables to the environment
    env.globals.update({
        'static': staticfiles_storage.url,  # For static file URLs
        'url': reverse,  # For reversing URLs
    })
    
    return env
