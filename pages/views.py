from django.shortcuts import render


def home(request):
    """
    This is the landing page view.
    """
    return render(request, "pages/home.html", {})
