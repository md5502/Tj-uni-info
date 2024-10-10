def build_professor_context(professors) -> dict:
    context = {}
    context["professors"] = []
    for item in professors:
        professor = {
            "name": item.name,
            "fname": item.fname,
            "position": item.position,
            "tag": item.tag,
            "slug": item.slug,
            "profile": item.profile_image,
        }
        context["professors"].append(professor)

    return context
