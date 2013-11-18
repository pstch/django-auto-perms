from django.db.models import Q
from django.contrib.contenttypes.models import ContentType


def auto_perms(models,perms):
    """
    Compares Permission objects to each registered Model to a set of defined persmissions

    Arguments:
    model -- list (or single object) of models (or ContentType objects), used to get permission objects poiting to them
    perms -- list (or single object) of permission names (like 'delete')

    Basically, this function iterates through each model (in the 'models' argument) , then gets the ContentType objects for the model.
    Permission objects have a foreign key to ContentType objects, so we are able to get all permissions for the model using ContentType.permission_set.
    Then, we filter these permissions, matching to the beginning of the permission codename with an item of the list in the 'perms' argument.

    """
    required_permissions = []

    if not isinstance(perms, (list, tuple)):
        # Transform single object to list with single item
        perms = [ perms, ]

    if not isinstance(models, (list, tuple)):
        # Transform single object to list with single item
        models = [ models, ]

    # Create Django Q object used to filter beginning of Permission.codename with a list of permission names
    query = Q()
    for perm in perms:
        query = query | Q(codename__startswith = perm)

    # Yallah
    for model in models: # I'm not sure it's possible to reduce this to a single SQL query whithout using Django internals (raw SQL)
        content_type = ContentType.objects.get_for_model(model) if not instance(model, ContentType) else model
        for p in content_type.permission_set.filter(query):
            required_permissions.append(p)

    return required_permissions

