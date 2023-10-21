from django.shortcuts import render

from .models import Category, ClassifiedAd

def index(request):
    """The homepage for classifieds."""
    return render(request, 'classifieds/index.html')

def categories(request):
    """Show all categories."""
    categories = Category.objects.order_by('category')
    #{key:val} where key is the name used in the template, val is the data
    # we're sending to the template!
    context = {'categories':categories}
    return render(request, 'classifieds/categories.html', context)

def category(request, category_id):
    """Show a single category and all its classified ads."""
    category = Category.objects.get(id=category_id)
    entries = category.classifiedad_set.order_by('-date_added')
    context = {'category':category, 'entries':entries}
    return render(request, 'classifieds/category.html', context)
