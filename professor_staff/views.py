
from django.shortcuts import render

from .selectors import get_professor_list, get_professor_via_slug, get_staff_list, get_staff_via_slug
from .services import build_professor_list_context, build_staff_list_context


def professor_list(request):
    professors = get_professor_list()
    context = build_professor_list_context(professors)
    return render(request, "professors/list.html", context)

def professor_detail(request, slug):
    professor = get_professor_via_slug(slug)
    return render(request, "professors/detail.html", {"professor": professor})


def staff_list(request):
    staffs = get_staff_list()
    context = build_staff_list_context(staffs)
    return render(request, "staffs/list.html", context)

def staff_detail(request, slug):
    staff = get_staff_via_slug(slug)
    return render(request, "staffs/detail.html", {"staff": staff})
