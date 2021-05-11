from django.shortcuts import render,HttpResponseRedirect,reverse,HttpResponse
from django.core.files.storage import FileSystemStorage
from cakeart.models import *
from bakers.utils import render_to_pdf 
from django.template.loader import get_template
# import pandas as pd
import csv


# Create your views here.
def loadtable1(request):
    if 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"bakers/tbl_bootstrap.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))
    #return render(request,"")

def viewcategory(request):
    if 'email' in request.session:
        cat=Category.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"bakers/category.html",{'all_cust':user,'msg':cat})
    else:
        return HttpResponseRedirect(reverse('login'))
    #return render(request,"")

def addproduct(request):
    if 'email' in request.session:
        all_cat=Category.objects.all()
        all_thm=Theme.objects.all()
        all_shps=Shape.objects.all()
        all_flvr=Flavour.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"bakers/addproduct.html",{'all_cust':user,'msg':all_cat,'thm':all_thm,'shp':all_shps,'flvr':all_flvr})
    else:
        return HttpResponseRedirect(reverse('login'))

def insertproduct(request):
    prodnm=request.POST['pnm']
    prodprc=request.POST['pprc']
    prodtype=request.POST['ptp']
    proddesc=request.POST['pdesc']
    category=request.POST['cat']
    prodimg=request.FILES.get('pimg')
    theme=request.POST['thme']
    proddec=request.POST['pdec']
    shape=request.POST['sha']
    flavor=request.POST['fla']
    usr=request.session['firstname']
    flr=Flavour.objects.get(flavour_name=flavor)
    cate=Category.objects.get(category_name=category)
    themes=Theme.objects.get(theme_name=theme)
    em=User.objects.get(firstname=usr)
    dec=Decoration.objects.create(decoration_name=proddec)
    shp=Shape.objects.get(shape_name=shape)
    prod=Product.objects.create(product_name=prodnm,product_price=prodprc,product_type=prodtype,product_desc=proddesc,category_id=cate,user_id=em,product_image=prodimg,theme_id=themes,decoration_id=dec,shape_id=shp,flavor_id=flr)
    return HttpResponseRedirect(reverse('showprod'))

def showprod(request):
    if 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        usr=User.objects.get(id=request.session['id'])
        all_prod=Product.objects.filter(user_id=usr)
        return render(request,"bakers/showproducts.html",{'all_cust':user,'allprod':all_prod})
    else:
        return HttpResponseRedirect(reverse('login'))

def editproduct(request,pk):
    if 'email' in request.session:
        all_cat=Category.objects.all()
        all_thm=Theme.objects.all()
        all_shps=Shape.objects.all()
        all_flvr=Flavour.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        pro=Product.objects.get(pk=pk)
        return render(request,"bakers/editprodpg.html",{'all_cust':user,'reguser':pro,'msg':all_cat,'thm':all_thm,'shp':all_shps,'flvr':all_flvr})
    else:
        return HttpResponseRedirect(reverse('login'))
    pro=Product.objects.get(pk=pk)
    return render(request,"bakers/editprodpg.html",{'reguser':pro}) 

def editpro(request,pk):
    prod=Product.objects.get(pk=pk)
    prod.product_name=request.POST['pnm']
    prod.product_price=request.POST['pprc']
    prod.product_type=request.POST['ptp']
    prod.product_desc=request.POST['pdesc']
    category=request.POST['cat']
    prod.product_image=request.FILES.get('pimg')
    theme=request.POST['thme']
    proddec=request.POST['pdec']
    shape=request.POST['sha']
    flavor=request.POST['fla']
    usr=request.session['firstname']
    prod.flavor_id=Flavour.objects.get(flavour_name=flavor)
    prod.category_id=Category.objects.get(category_name=category)
    prod.theme_id=Theme.objects.get(theme_name=theme)
    prod.user_id=User.objects.get(firstname=usr)
    prod.decoration_id=Decoration.objects.create(decoration_name=proddec)
    prod.shape_id=Shape.objects.get(shape_name=shape)
    prod.save()
    return HttpResponseRedirect(reverse('showprod'))

def deleteproduct(request,pk):
    pro=Product.objects.get(pk=pk)
    pro.delete()
    return HttpResponseRedirect(reverse("showprod"))

def reqpasswrd(request):
    if 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"bakers/reqchngepwd.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))

def changepassword(request):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        id=request.session['id']
        usr=User.objects.get(id=id)
        old_password=user.pwd
        current = request.POST['currentpwd']
        new_password = request.POST['new']
        confirm = request.POST['confirm']
        if old_password == current and new_password == confirm:
            usr.pwd = confirm
            usr.save()
            message = "Your Password has been changed successfully:)"
            return render(request, "bakers/tbl_bootstrap.html",{'msg':message,'all_cust':user})
        else:
            error_msg = "Incorrect Password , Try Again  !!"
            return render(request, "bakers/reqchngepwd.html", {'error_msg': error_msg,'all_cust':user}) 
    else:
        return HttpResponseRedirect(reverse('login'))

def profile(request,pk):
    if 'email' in request.session:
        usr=User.objects.get(pk=pk)
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"bakers/editprofile.html",{'all_cust':user,'profile':usr})
    else:
        return HttpResponseRedirect(reverse('login'))

def editprofile(request,pk):
    user=User.objects.get(pk=pk)
    user.firstname=request.POST['fnm']
    user.lastname=request.POST['lnm']
    user.DOB=request.POST['dob']
    user.contact=request.POST['cont']
    user.address=request.POST['add']
    user.pinc=request.POST['pinc']
    user.License=request.FILES.get('lic')
    user.email=request.POST['em']
    user.save()
    return HttpResponseRedirect(reverse('welcome'))

def welcome(request):
    if 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"bakers/welcome.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))

def reportorder(request):
    if 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        ord=OrderDetailing.objects.filter(userid=user)
        return render(request,"bakers/reportorder.html",{'all_cust':user,'order':ord})
    else:
        return HttpResponseRedirect(reverse('login'))


def reportproduct(request):
    if 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        all_prod=Product.objects.filter(user_id=user)
        return render(request,"bakers/reportproduct.html",{'all_cust':user,'allprod':all_prod})
    else:
        return HttpResponseRedirect(reverse('login'))

def onselect(request):
    if 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        
        selection=request.POST['viewby']
        nm=request.POST['search']
        if selection=="Category":
            cat=Category.objects.get(category_name=nm)
            all_prod=Product.objects.filter(user_id=user,category_id=cat)
            if cat!="":    
                return render(request,"bakers/reportproduct.html",{'all_cust':user,'allprod':all_prod})
        # elif selection=="Decoration":
        #     deco=Decoration.objects.get(decoration_name=nm)
        #     all_prod=Product.objects.filter(user_id=user,decoration_id=deco)    
        #     return render(request,"bakers/reportproduct.html",{'all_cust':user,'allprod':all_prod})
        elif selection=="Theme":
            thm=Theme.objects.get(theme_name=nm)
            all_prod=Product.objects.filter(user_id=user,theme_id=thm)    
            return render(request,"bakers/reportproduct.html",{'all_cust':user,'allprod':all_prod})
        elif selection=="Flavor":
            flvr=Flavour.objects.get(flavour_name=nm)
            all_prod=Product.objects.filter(user_id=user,flavor_id=flvr)    
            return render(request,"bakers/reportproduct.html",{'all_cust':user,'allprod':all_prod})
    else:
        return HttpResponseRedirect(reverse('login'))


def onc(request):
    if 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        all_prod=Product.objects.filter(user_id=user)
        selectio=request.POST.get('exportto')
        print("------------------------------------",selectio)
        if selectio=="Select":
            alrt="First select type of file to which you want to export!!"
            return render(request,"bakers/reportproduct.html",{'all_cust':user,'allprod':all_prod,'aler':alrt})
        elif selectio=="PDF":
            return render_to_pdf('bakers/reportproductpdf.html', {'allprod':all_prod,'all_cust':user})

        elif selectio=="Excel":
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="products.csv"'
            writer = csv.writer(response)
            for i in all_prod:
                writer.writerow([i.product_name,i.product_price,i.product_type,i.product_desc,i.category_id.category_name,i.user_id.firstname,i.theme_id.theme_name,i.flavor_id.flavour_name,i.decoration_id.decoration_name])
            return response
            # return HttpResponse(1)
    else:
        return HttpResponseRedirect(reverse('login'))