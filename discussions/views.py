from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
    """The home page for discussions."""
    return render(request, 'discussions/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'discussions/topics.html', context)
