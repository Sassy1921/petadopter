from django.shortcuts import render,redirect

from animals.models import Animal
from animals.models import Contact 
#import pagination
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import get_object_or_404

# Create your views here.
def success(request):
    return render(request,'animals/success.html',{})

def home(request):
    animals = Animal.objects.all()
    full_name = request.POST.get('full_name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    if request.method == 'POST': # If the form has been submitted...
        data = Contact(full_name = full_name,email = email,subject = subject,message = message)
        data.save()
        return redirect('success')
    return render(request,'animals/home.html',{'animals':animals})


def cats(request):
    cats = Animal.objects.filter(animal='Cat').order_by('age')
    p = Paginator(cats,3)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page= p.page(1)
    
    context = {'animals':page}
    return render(request,'animals/cats.html',context)



def dogs(request):
    dogs= Animal.objects.filter(animal='Dog').order_by('age')
    p = Paginator(dogs,3)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page= p.page(1)
    
    context = {'animals':page}
    return render(request,'animals/dogs.html',context)
def birds(request):
    birds = Animal.objects.filter(animal='Bird').order_by('age')
    p = Paginator(birds,3)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page= p.page(1)
    
    context = {'animals':page}
    return render(request,'animals/birds.html',context)
def detail(request,animal_id):
    animal = get_object_or_404(Animal,pk=int(animal_id))
    animals = Animal.objects.all()
    return render(request,'animals/details.html',{'animal':animal, 'animals':animals})
