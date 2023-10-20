from django.shortcuts import render

def index(request):
    """The homepage for classifieds."""
    return render(request, 'classifieds/index.html')
