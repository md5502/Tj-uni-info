from django.db.models import Q

from shahid.selectors import get_shahid_list


def build_shahid_list_context(request):
    context = {}
    shahid_list = get_shahid_list()

    context["shahid_list"] = []
      # Check for search query and filter events
    search_query = request.GET.get("search")
    if search_query:
        shahid_list = shahid_list.filter(Q(first_name__icontains=search_query))


    for item in shahid_list:
        shahid = {}
        shahid["full_name"] = item.first_name + " " + item.last_name
        shahid["life_story"] = item.life_story
        shahid["slug"] = item.slug
        shahid["martyrdom_location"] = item.martyrdom_location
        shahid["profile_image"] = item.profile_image

        context["shahid_list"].append(shahid)
    return context
