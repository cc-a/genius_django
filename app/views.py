from django.shortcuts import render

from stats import calc_stats

from .forms import UserInfoForm
from .models import AccessRecord, UserInfo


def info(request):
    """Display/process form with new user information."""
    form = UserInfoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request, "info.html")


def index(request):
    """Basic index page."""
    return render(request, "home.html")


def access(request):
    """Page that logs visits."""
    AccessRecord.objects.create()
    return render(request, "access.html")


def stats(request):
    objects = UserInfo.objects.all()
    context = dict()
    context["age_stats"] = calc_stats([obj.age for obj in objects])
    context["size_stats"] = calc_stats([obj.size for obj in objects])
    return render(request, "stats.html", context=context)
