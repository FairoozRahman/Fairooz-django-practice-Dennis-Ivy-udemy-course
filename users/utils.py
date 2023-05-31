from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    skills = Skill.objects.filter(name__icontains=search_query)
    profilesObj = Profile.objects.distinct().filter(Q(name__icontains=search_query) |
                                                    Q(short_intro__icontains=search_query) | Q(skill__in=skills))
    return profilesObj, search_query


def paginateProfiles(request, profilesObj, results):
    page = request.GET.get('page')
    paginator = Paginator(profilesObj, results)
    try:
        profilesObj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profilesObj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profilesObj = paginator.page(page)
    leftIndex = max(1, int(page) - 4)
    rightIndex = min(int(page) + 5, paginator.num_pages + 1)
    custom_range = range(leftIndex, rightIndex)
    return custom_range, profilesObj
