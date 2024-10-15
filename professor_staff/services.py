def build_professor_list_context(professors) -> dict:
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


def build_staff_list_context(staffs) -> dict:
    context = {}
    context["staffs"] = []
    for item in staffs:
        staff = {
            "name": item.name,
            "fname": item.fname,
            "position": item.position,
            "tag": item.tag,
            "slug": item.slug,
            "profile": item.profile_image,
        }
        context["staffs"].append(staff)
    return context
