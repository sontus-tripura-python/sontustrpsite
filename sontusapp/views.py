from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import *
# Create your views here.


def Home_page(request):
    about_me = AboutMe.objects.all().order_by('-id')[:1]
    time_line = TimeLine.objects.all()
    context = {'about_me': about_me, 'time_line': time_line}
    return render(request, 'home/home.html', context)

def portfolio(request, category_slug=None):
    category = None
    portfolio_cats = PortfolioCategory.objects.all()
    portfolio = Portfolio.objects.all()
    if category_slug:
        category = get_object_or_404(PortfolioCategory, slug=category_slug)
        portfolio = portfolio.filter(category=category)

    context = {'category':category, 'portfolio_cats': portfolio_cats,
           'portfolio': portfolio}

    return render(request, 'home/portfolio.html', context)
def test_list(request):
    return render(request, 'test.html')
def contact(request):
    if request.method == 'POST':
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        message =request.POST['message']
        #sentTime =request.POST['sentTime']
        if len(name)<6 or len(phone)<11 or len(email)<6 or len(message)<10:
            messages.error(request, "Fail! Please, fill up the form correctly,You missed something")
        else:
            messages.success(request, " thank you ! Your message has been sent successfully. we will contact with you soon ")
        contact = Contact( name=name, email=email, message=message, phone=phone)
        contact.save()
    return render(request, 'home/home.html')
