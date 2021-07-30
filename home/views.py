from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from products.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def index (request):
    setting = Setting.objects.get(pk=1)
    brands = Brand.objects.all()
    testimo = Testimonial.objects.all()
    category = Category.objects.all()[:3]
    offer = Product.objects.get(offer=True)
    banner = Product.objects.get(banner=True)
    feat =Product.objects.filter(featured=True)
    late =Product.objects.filter(latest=True)
    late2 =Product.objects.filter(latest=True).order_by('-id')

    context = {
        'setting': setting,
        'brands': brands,
        'testimo': testimo,
        'category': category,
        'offer': offer,
        'banner':banner,
        'featured':feat,
        'latest': late,
        'latest2': late2,
    }

    return render (request, 'index.html', context)

def about (request):
    
    setting = Setting.objects.get(pk=1)
    brands = Brand.objects.all()
    # category = Category.objects.all()

    context = {
        'setting': setting,
        'brands': brands,
        # 'category': category,
    }

    return render (request, 'about.html', context)


def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent! Our Customer Service Team will reach you soon.")
            return redirect ('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    brands = Brand.objects.all()

    context = {'setting': setting,
                'form': form,
                'brands': brands,
    }

    return render (request, 'contact.html', context)

def category(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    brands = Brand.objects.all()
    offer = Product.objects.get(offer=True)

    context = {
        'category': category,
        'setting': setting,
        'brands': brands,
        'offer': offer,
    }

    return render (request, 'category.html', context)
    # return HttpResponse ('Hey there.')


def product_list(request, id, slug):
    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    images = Images.objects.filter(product_id = id)
    paginator = Paginator(products,2)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'setting': setting,
        'category': category,
        'catdata': catdata,
        'products': paged_products,
    }

    return render(request, 'products.html', context)
    

def prod_detail (request, id, slug):
    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    product = Product.objects.get (pk=id)
    images = Images.objects.filter(product_id=id)


    context = {
        'setting': setting,
        'category': category,
        'products': products,
        'product': product,
        'images': images,
    }

    return render(request, 'product-details.html', context)