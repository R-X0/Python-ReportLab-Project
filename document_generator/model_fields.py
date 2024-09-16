from django.apps import apps

def get_all_model_fields():
    """
    Retrieve all model fields from all installed apps.
    Returns a dictionary with model names as keys and lists of field names as values.
    """
    all_fields = {}
    # Iterate over all models in the installed apps.
    for model in apps.get_models():
        model_name = model.__name__
        # Get all field names for the model.
        fields = [field.name for field in model._meta.fields]
        all_fields[model_name] = fields
    return all_fields
