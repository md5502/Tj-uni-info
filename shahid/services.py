


def build_shahid_list_context(shahid_list):
    context = {}

    context["shahid_list"] = []
      # Check for search query and filter events


    for item in shahid_list:
        shahid = {}
        shahid["full_name"] = item.first_name + " " + item.last_name
        shahid["life_story"] = item.life_story
        shahid["slug"] = item.slug
        shahid["martyrdom_location"] = item.martyrdom_location
        shahid["profile_image"] = item.profile_image

        context["shahid_list"].append(shahid)
    return context
