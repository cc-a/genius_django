from django.shortcuts import render

from .forms import UserInfoForm
from .models import AccessRecord


def info(request):
    form = UserInfoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request, "info.html")


def index(request):
    return render(request, "home.html")


def access(request):
    AccessRecord.objects.create()
    return render(request, "access.html")
