from django.shortcuts import render
from .models import Profile, Gallery


def home(request):
    context = {
        'profiles': Profile.objects.all(),
        'pics': Gallery.objects.all(),
    }
    return render(request, "home.html", context)
