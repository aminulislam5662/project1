from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from  .forms import ProductForms

from eApp.models import Person, ProductImages, products

def index(request):
        db_data= products.objects.all()
        return render(request,"eApp/index.html",{'db_data':db_data})


def upload(request):
        form = ProductForms()
        context={'form':form}
        if request.method =='POST':
                prod = products()
                prod.title= request.POST['title']
                prod.oldprice= request.POST['oldprice']
                prod.newprice= request.POST['newprice']
                prod.description= request.POST['description']
                prod.specification= request.POST['specification']
                prod.reviews= request.POST['reviews']
                prod.comments= request.POST['comments']
                prod.reviews= request.POST['reviews']
                prod.images= request.FILES.get('image')
                productimages= request.FILES.getlist('productImages')

                if form.is_valid:
                        for index, image in enumerate(productimages):
                                print(index)
                                print(image)
                                new_file= ProductImages(
                                       
                                        file= image
                                )
                                new_file.save()            
                prod.save()


        return render(request,"eApp/uploadproduct.html",context)


def exercise(request):
        person = Person.objects.get(id=1)
        for interest in person.interests.all():
         print(interest)
        return render(request,'eApp/exercise.html')

# Create your views here.

# python manage.py makemigrations eApp



from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, PostForm
from .models import Images

# @login_required
def blogpost(request):
 
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
    
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
    
    
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()
    
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/blog/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'eApp/blog.html',
                  {'postForm': postForm, 'formset': formset})