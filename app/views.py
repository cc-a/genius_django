from django.shortcuts import render

from .forms import UserInfoForm
from .models import AccessRecord


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
