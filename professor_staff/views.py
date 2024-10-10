
from django.shortcuts import render

from .selectors import get_professor_list, get_professor_via_slug
from .services import build_professor_context


def professor_list(request):
    professors = get_professor_list()
    context = build_professor_context(professors)
    return render(request, "professors/list.html", context)

def professor_detail(request, slug):
    professor = get_professor_via_slug(slug)

    return render(request, "professors/detail.html", {"professor": professor})
