from django.shortcuts import render, redirect

from .models import Category, ClassifiedAd
from .forms import ClassifiedAdForm


def index(request):
    """The homepage for classifieds."""
    context = { 'title':'Classifieds - Home'}
    return render(request, 'classifieds/index.html', context)

def categories(request):
    """Show all categories."""
    categories = Category.objects.order_by('category')
    #{key:val} where key is the name used in the template, val is the data
    # we're sending to the template!
    context = {'categories':categories, 'title':'Classifieds - Categories'}
    return render(request, 'classifieds/categories.html', context)

def category(request, category_id):
    """Show a single category and all its classified ads."""
    category = Category.objects.get(id=category_id)
    entries = category.classifiedad_set.order_by('-date_added')
    context = {'category':category, 'entries':entries,
               'title':f'Classifieds - {category}'}
    return render(request, 'classifieds/category.html', context)

def new_ad(request):
    """Add a new ad."""
    if request.method != 'POST':
        # Create a blank form
        form = ClassifiedAdForm()
    else:
        # process data
        form = ClassifiedAdForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('classifieds:categories')
    context = {'form':form}
    return render(request, 'classifieds/new_ad.html', context)

def individual_ad(request, ad_id):
    """View an individual ad on it's own page."""
    ad = ClassifiedAd.objects.get(id=ad_id)
    category = ad.category
    headline = ad.headline
    body = ad.body
    email = ad.email
    date = ad.date_added
    context = {'category': category, 'headline': headline, 'body':body,
               'email': email, 'date':date,
    'title': f'Classifieds - {category} - {headline}' }
    return render(request, 'classifieds/individual_ad.html', context)
