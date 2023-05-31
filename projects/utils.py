from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProjects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tag = Tag.objects.filter(name__icontains=search_query)
    projectsObj = Project.objects.distinct().filter(Q(title__icontains=search_query) |
                                                    Q(description__icontains=search_query) |
                                                    Q(owner__name__icontains=search_query) | Q(tags__in=tag))
    return projectsObj, search_query


def paginateProjects(request, projectsObj, results):
    page = request.GET.get('page')
    paginator = Paginator(projectsObj, results)
    try:
        projectsObj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projectsObj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projectsObj = paginator.page(page)
    leftIndex = max(1, int(page) - 4)
    rightIndex = min(int(page) + 5, paginator.num_pages + 1)
    custom_range = range(leftIndex, rightIndex)
    return custom_range, projectsObj
