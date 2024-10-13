from django.db.models import Q

from .selectors import get_association_list


def build_association_context(request) -> dict:
    context = {}
    context["associations"] = []
    associations = get_association_list()

    search_query = request.GET.get("search")
    if search_query:
        associations = associations.filter(Q(name__icontains=search_query))

    for item in associations:
        association = {}
        association["name"] = item.name
        association["logo"] = item.logo
        association["description"] = item.description
        association["slug"] = item.slug
        context["associations"].append(association)

    return context
