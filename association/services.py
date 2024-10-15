def build_association_context(associations) -> dict:
    context = {}
    context["associations"] = []

    for item in associations:
        association = {}
        association["name"] = item.name
        association["logo"] = item.logo
        association["description"] = item.description
        association["slug"] = item.slug
        context["associations"].append(association)

    return context
