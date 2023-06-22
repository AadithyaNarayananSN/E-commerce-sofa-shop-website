import os

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from eproject.settings import EMAIL_HOST_USER

# Create your views here.


def index(request):
    return render(request,'index.html')



def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['password2']
            mb = a.cleaned_data['mobile']
            ad = a.cleaned_data['address']
            if ps == cp:
                b = regmodel(name=nm, email=em, password=ps, mobile=mb, address=ad)
                b.save()
                return redirect(login)
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Registration failed")
    return render(request, 'register.html')




def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regmodel.objects.all()
            for i in b:
                request.session['id'] = i.id
                print(request.session['id'])
                if i.email == em and i.password == ps:

                    # return HttpResponse("Login success")
                    return redirect(userprofile)

            else:
                return HttpResponse("Login failed")
    else:
        return render(request,'login.html')


def shoplogin(request):
    if request.method == 'POST':
        a = shoplogform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            cd = a.cleaned_data['code']
            if em == "couches@gmail.com" and cd == 33355:
                    return redirect(productdisplay)
            else:
                return HttpResponse("Login failed")
        else:
            return HttpResponse("not valid")
    else:
        return render(request, 'shoplogin.html')







def productdetails(request):
    if request.method == 'POST':
        a = productform(request.POST,request.FILES)
        if a.is_valid():
            nm = a.cleaned_data['name']
            pr = a.cleaned_data['price']
            im = a.cleaned_data['image']

            b = productmodel(name=nm,price=pr,image=im)
            b.save()

            return redirect(productdisplay)
        else:
            return HttpResponse("File upload failed")
    else:
        return render(request,'productdetails.html')


def productdisplay(request):
    a = productmodel.objects.all()
    namelist = []
    pricelist = []
    imagelist = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        imagelist.append(str(img).split('/')[-1])
        nm = i.name
        namelist.append(nm)
        pl = i.price
        pricelist.append(pl)
    mylist = zip(imagelist,namelist,pricelist,id)
    return render(request,'productdisplay.html',{'list':mylist})


def editproduct(request, id):
    a = productmodel.objects.get(id=id)
    image = str(a.image).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(a.image) > 0:
                os.remove(a.image.path)
            a.image = request.FILES['image']
        a.name = request.POST.get('name')
        a.price = request.POST.get('price')
        # a.description = request.POST.get('description')
        a.save()
        return redirect(productdisplay)
    return render(request, 'editproduct.html', {'a': a, 'image': image})


def deleteproduct(request,id):
    a = productmodel.objects.get(id = id)
    if len(a.image)>0:
        os.remove(a.image.path)
    a.delete()
    return redirect(productdisplay)


def footer(request):
    return render(request,'footer.html')


def userprofile(request):
    a = productmodel.objects.all()
    namelist = []
    pricelist = []
    imagelist = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        imagelist.append(str(img).split('/')[-1])
        nm = i.name
        namelist.append(nm)
        pl = i.price
        pricelist.append(pl)
    mylist = zip(imagelist,namelist,pricelist,id)
    return render(request,'userprofile.html',{'list':mylist})


def wishlist(request,id):
    a = productmodel.objects.get(id=id)
    id1=request.session['id']
    b = wishlistmodel(uid=id1,pid=id,name=a.name,price=a.price,image=a.image)
    b.save()
    return redirect(mywish)





def mywish(request):
    a = wishlistmodel.objects.all()
    namelist = []
    pricelist = []
    imagelist = []

    id = []
    uid=[]


    for i in a:
        ui=i.uid
        uid.append(ui)
        id1 = i.id
        id.append(id1)
        img = i.image
        imagelist.append(str(img).split('/')[-1])
        nm = i.name
        namelist.append(nm)
        pl = i.price
        pricelist.append(pl)
    ui = request.session['id']
    mylist = zip(imagelist, namelist, pricelist, id,uid)
    return render(request,'mywish.html',{'mylist':mylist,'id':ui})



def removewish(request,id):
    a = wishlistmodel.objects.get(id=id)
    a.delete()
    return redirect(mywish)



def cart(request,id):
    a = productmodel.objects.get(id=id)
    id1=request.session['id']
    print(id1)
    b = cartmodel(uid=id1,pid=id,name=a.name,price=a.price,image=a.image)
    b.save()
    return redirect(mycart)




def mycart(request):
    a = cartmodel.objects.all()
    namelist = []
    pricelist = []
    imagelist = []
    id = []
    u=[]

    for i in a:
        ui=i.uid
        u.append(ui)
        id1 = i.id
        id.append(id1)
        img = i.image
        imagelist.append(str(img).split('/')[-1])
        nm = i.name
        namelist.append(nm)
        pl = i.price
        pricelist.append(pl)
    ab=request.session['id']
    print(ab)
    mylist = zip(imagelist,namelist, pricelist,id,u)

    return render(request,'mycart.html',{'mylist':mylist,'ab':ab})




def removecart(request,id):
    a = cartmodel.objects.get(id=id)
    a.delete()
    return redirect(mycart)



def success(request):
    return render(request,'success.html')


def wishlisttocart(request, id):
    a = wishlistmodel.objects.get(id=id)
    b = cartmodel(image=a.image, name=a.name, price=a.price,pid=a.pid,uid=a.uid)
    b.save()
    # return HttpResponse("Product added to Cart")
    return redirect(mycart)



def buyproduct(request, id):
    b = cartmodel.objects.get(id=id)
    nm = b.name
    pr = b.price
    if request.method == 'POST':
        a = paymentform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            pr = a.cleaned_data['price']
            fn = a.cleaned_data['fname']
            ad = a.cleaned_data['address']
            em = a.cleaned_data['email']
            nmb = a.cleaned_data['number']
            pm = a.cleaned_data['paymode']
            b = paymentmodel(name=nm, price=pr, fname=fn, address=ad, email=em, number=nmb, paymode=pm)
            b.save()
            subject = f"Order Placed for {nm}"
            message = f"Hello {fn} ,\n \t  your order for our product  {nm} has been placed successfully. You can expect delivery within 4 days." \
                      f"\n\n Order Details:\n Product Name: {nm}\n Price : {pr} Rupees\n\n\n Customer details:\n Name: {fn}\n Address: {ad}\n Email: {em} \n Number: {nmb}\n Payment Mode: {pm}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return render(request, 'success.html',{'fn':fn})

        else:
            return HttpResponse("Order Failed!")
    else:
        return render(request, 'buyproduct.html', {'nm':nm, 'pr':pr})





def vieworder(request):
    a = paymentmodel.objects.all()
    return render(request,'vieworder.html',{'a':a})
