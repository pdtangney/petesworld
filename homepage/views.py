from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for homepage. The main site homepage."""
    return render(request, 'homepage/index.html')
