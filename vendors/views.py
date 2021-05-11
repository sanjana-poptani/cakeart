from django.shortcuts import render,HttpResponseRedirect,reverse, HttpResponse, redirect
from cakeart.models import *
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
import logging,traceback
import vendors.constants as constants
import vendors.config as config
import datetime
import hashlib    
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .checksum import generate_checksum, verify_checksum


# Create your views here.

def loadtbl(request):
    if request.session['email']=="sanjanapoptani54@gmail.com" and request.session['firstname']=="sanjana":
        frstnm=request.session['firstname']
        usrtyp=User_type.objects.get(utname="Vendor")
        vendors=User.objects.filter(utid=usrtyp)
        return render(request,"vendors/tbl_bootstrap.html",{'profile':frstnm,'email':"sanjanapoptani54@gmail.com",'vndr':vendors})
    elif 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"vendors/tbl_bootstrap.html",{'all_cust':user,'email':"sanjanapoptani54@gmail.com"})
    else:
        return HttpResponseRedirect(reverse('login'))


def loadtbl2(request):
    usr=User.objects.all()
    return render(request,"vendors/table2.html",{'profile':usr})


def loadtbl3(request):
    cat=Category.objects.all()
    print("\n\n===== Image URL",settings.MEDIA_URL,"\n\n")
    return render(request,"vendors/table3.html",{'profile':cat})


def loadtbl4(request):
    cat=Package.objects.all()
    return render(request,"vendors/table4.html",{'profile':cat})

def EditPage(request,pk):
    user=User.objects.get(pk=pk)
    return render(request,"vendors/edit.html",{'reguser':user})

def delPage(request,pk):
    user=User.objects.get(pk=pk)
    user.delete()
    return HttpResponseRedirect(reverse('table'))

def deletePage(request,pk):
    user=User.objects.get(pk=pk)
    user.delete()
    return HttpResponseRedirect(reverse('table'))

def EditUser(request,pk):
    user=User.objects.get(pk=pk)
    user.firstname=request.POST['firstname']
    user.lastname=request.POST['lastname']
    user.email=request.POST['email']
    user.License=request.POST.get('License')
    user.save()
    if user.utid_id == 2:
        return HttpResponseRedirect(reverse('table'))
    else:
        return HttpResponseRedirect(reverse('table2'))

def EditCategory(request,pk):
    user=Category.objects.get(pk=pk)
    return render(request,"vendors/editcat.html",{'reguser':user})

def delCategory(request,pk):
    print("=============1====================")
    user=Category.objects.get(pk=pk)
    print("user")
    user.delete()
    return HttpResponseRedirect(reverse('table3'))

def editcat(request,pk):
    cat=Category.objects.get(pk=pk)
    cat.category_name=request.POST['categoryname']
    cat.save()
    return HttpResponseRedirect(reverse('table3'))

def addcat(request):
    return render(request,'vendors/addcat.html')

def AddCategory(request):
    category_name=request.POST['name']
    category_img=request.FILES.get('categoryimg')
    print("\n\n====== Image ===",category_img)
    if category_img:
        cat=Category.objects.create(category_name=category_name,category_img=category_img)
    return HttpResponseRedirect(reverse('table3'))

def EditPackage(request,pk):
    pack=Package.objects.get(pk=pk)
    return render(request,'vendors/editpack.html',{'reguser':pack})

def delPackage(request,pk):
    user=Package.objects.get(pk=pk)
    user.delete()
    return HttpResponseRedirect(reverse('table4'))

def EditPack(request,pk):
    user=Package.objects.get(pk=pk)
    user.package_name=request.POST['package_name']
    user.package_price=request.POST['package_price']
    user.package_validity=request.POST['package_validity']
    user.package_discount=request.POST['package_discount']
    user.save()
    return HttpResponseRedirect(reverse('table4'))

def AddPack(request):
    return render(request,"vendors/addpack.html")

def AddPackage(request):
    pn=request.POST['package_name']
    pp=request.POST['package_price']
    pv=request.POST['package_validity']
    pd=request.POST['package_discount']
    pde=request.POST['package_description']
    pack=Package.objects.create(package_name=pn,package_price=pp,package_validity=pv,package_description=pde)
    return HttpResponseRedirect(reverse('table4'))

def showprod(request):
    if 'email' in request.session:
        all_prod=Product.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"vendors/showproduct.html",{'all_cust':user,'allprod':all_prod})
    else:
        return HttpResponseRedirect(reverse('login'))

def addtocart(request):
    print("\n\n----------------------------\n\n")
    pid=request.GET['pid']
    price=request.GET['price']
    prd=Product.objects.get(pk=pid)
    print("\n\n-------------------",pid,price,prd,"----------------------\n\n")
    user=User.objects.get(pk=request.session['id'])
    print("====USER===",user)
    cartli=Cart.objects.all()

    print("CARTLI===",cartli)
    for i in cartli:
        print("I====",i)
        if prd==i.prodid:
            print("PRD===",prd,i.prodid)
            return HttpResponse("Error")
        
    pro=Cart.objects.create(prodid=prd,userid=user)
    print("Pro====",pro)
    return HttpResponse(1)
    # return HttpResponseRedirect(reverse("cartlist"))

def cartlist(request):
    if 'email' in request.session:
        cart=Cart.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"vendors/cartlist.html",{'all_cust':user,'allprod':cart})
    else:
        return HttpResponseRedirect(reverse('login'))

# def cartlistcalc(request):
#     Cart.objects.all()
#     return 1

def deletecartobj(request,pk):
    # pro=Cart.objects.get(pk=pk)
    pro=Cart.objects.get(pk=pk)
    pro.delete()
    return HttpResponseRedirect(reverse("cartlist"))

def checkout(request):
    if 'email' in request.session:
        try:
            print("\n\n===========1=============")
            usr=User.objects.get(id=request.session['id'])
            print("===========2=============",Cart)
            cartobj=Cart.objects.filter(userid=usr)
            print("===========3=============",cartobj)
            print("\n\n GET===",request.GET,cartobj)
            pid=request.GET.get('pid')
            qty=request.GET.get('qty')
            nm=request.GET.get('nm')
            print("Pid--------------->",pid)
            print("Qty--------------->",qty)
            print("CARTOBJ-====",cartobj)
            proobj=Product.objects.get(pk=pid)
            for obj in cartobj:
                if obj.prodid == proobj:
                    print(obj)
                    print(obj.prodid)
                    print(proobj)
                    print("\n Before Quantity==",obj.qnty)
                    obj.qnty = int(qty)
                    print("\n After Quantity==",obj.qnty)
                    print("\n Before rowtotal==",obj.rowtotal)
                    obj.rowtotal=int(qty)*proobj.product_price
                    print("\n After rowtotal==",obj.rowtotal)
                    print("Name--------------->",nm)
                    obj.cnm=nm
                    obj.save()          
            print("##################Reached#########################")
            return HttpResponse(1)
            # return HttpResponseRedirect(reverse("viewcart"))
        except Exception as e1:
            print("Exception Caught Checkout------------------>",e1)
        
    else:
        return HttpResponseRedirect(reverse('login'))


def viewcart(request):
    if 'email' in request.session:
        cartl=Cart.objects.all()
        tax=0
        finaltotal=0
        for i in cartl:
            finaltotal+=i.rowtotal
        tax=finaltotal * 5 / 100
        grandfinal=finaltotal+tax
        usr=User.objects.get(firstname=request.session['firstname'])
        return render(request,"vendors/viewlist.html",{'all_cust':usr,'cartl':cartl,'finaltotal':finaltotal,'tax':tax,'grandfinal':grandfinal})
    else:
        return HttpResponseRedirect(reverse('login')) 

def addpro(request):
    if 'email' in request.session:
        all_cat=Category.objects.all()
        all_thm=Theme.objects.all()
        all_shps=Shape.objects.all()
        all_flvr=Flavour.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"vendors/addpro.html",{'all_cust':user,'msg':all_cat,'thm':all_thm,'shp':all_shps,'flvr':all_flvr})
    else:
        return HttpResponseRedirect(reverse('login'))

def makepayment(request):
    if 'email' in request.session:
        # user=User.objects.get(firstname=request.session['firstname'])
        data=OrderMaster.objects.all()
        # if data['id']==0:
        usr=User.objects.get(id=request.session['id'])
        shippingaddr=request.POST['shipaddr']
        totprc=request.POST['grandfinal']
        crte=OrderMaster.objects.create(userid=usr,BillingAddress=shippingaddr,TotalPrice=float(totprc))
        cart=Cart.objects.all()
        for item in cart:
            oitem=OrderDetailing.objects.create(userid=item.prodid.user_id,orderid=crte,prodid=item.prodid,qty=item.qnty,prc=item.rowtotal,cnm=item.cnm)
            pro=Products.objects.filter(user_id=item.userid)
            prod=Product.objects.filter(user_id=item.userid)
            print("-------------------------------------------",prod,"---------------------------------------",pro,"--------------------------------------")
            for i in prod: 
                for j in pro:   
                    print("------------------------",i.product_name,"-------------------------------------",j.product_name)
                    if j.product_name==i.product_name:
                        print("-----------------------",j.product_name,"--------------------------",j.qty)
                        j.qty=j.qty+item.qnty
                        j.save()
                    else:
                        pass
            pitem=Products.objects.create(product_name=item.prodid.product_name,product_price=item.prodid.product_price,product_type=item.prodid.product_type,product_desc=item.prodid.product_desc,category_id=item.prodid.category_id,user_id=item.userid,product_image=item.prodid.product_image,theme_id=item.prodid.theme_id,decoration_id=item.prodid.decoration_id,shape_id=item.prodid.shape_id,flavor_id=item.prodid.flavor_id,qty=item.qnty)
            item.delete()
        return redirect(reverse("pay"))
    else: 
        return HttpResponseRedirect(reverse('login'))

# def payment(request):   
#     data = {}
#     txnid = get_transaction_id()
#     hash_ = generate_hash(request, txnid)
#     # hash_string = get_hash_string(request, txnid)
#     # use constants file to store constant values.
#     # use test URL for testing
#     data["action"] = constants.PAYMENT_URL_LIVE
#     usr=User.objects.get(id=request.session['id'])
#     now=datetime.date.today()
#     print("----------------------------------------------Date: ", now)
#     om=OrderMaster.objects.get(userid=usr,order_dt=now)
#     print("00000000000000000000000000000000000000000000000",om,"000000000000000000000000") 
#     data["amount"] = float(constants.PAID_FEE_AMOUNT)
#     od=OrderDetailing.objects.filter(dt=om.order_dt)
#     data["productinfo"]  = constants.PAID_FEE_PRODUCT_INFO
#     data["key"] = config.KEY
#     data["name"]=od
#     data["txnid"] = txnid
#     data["hash"] = hash_
#     data["hash_string"] = hash_string
#     data["firstname"] = request.session['firstname']
#     data["email"] = request.session["email"]
#     # usr=User.objects.get(id=request.session['id'])
#     data["phone"] = usr.contact
#     data["service_provider"] = constants.SERVICE_PROVIDER
#     data["furl"] = request.build_absolute_uri(reverse("payfailure"))
#     data["surl"] = request.build_absolute_uri(reverse("paysuccess"))
    
#     data["i"]=om.TotalPrice
#     print("--------------------------------------------",data["i"])
#     pymn=Payment.objects.create(txid=txnid,userid=usr,omid=om)
#     return render(request, "vendors/payment_form.html", data)        
    
# # generate the hash
# def generate_hash(request, txnid):
#     try:
#         # get keys and SALT from dashboard once account is created.
#         # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
#         hash_string = get_hash_string(request,txnid)
#         generated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
#         return generated_hash
#     except Exception as e:
#         # log the error here.
#         logging.getLogger("error_logger").error(traceback.format_exc())
#         return None

# # create hash string using all the fields
# # def get_hash_string(request, txnid):
#     # hash_string = config.KEY+"|"+txnid+"|"+str(float(constants.PAID_FEE_AMOUNT))+"|"+constants.PAID_FEE_PRODUCT_INFO+"|"
#     # hash_string += request.session["firstname"]+"|"+request.session["email"]+"|"
#     # hash_string += "||||||||||"+config.SALT

#     # return hash_string

# # generate a random transaction Id.
# def get_transaction_id():
#     hash_object = hashlib.sha256(str(randint(0,9999)).encode("utf-8"))
#     # take approprite length
#     txnid = hash_object.hexdigest().lower()[0:32]
#     return txnid

# # no csrf token require to go to Success page. 
# # This page displays the success/confirmation message to user indicating the completion of transaction.
# @csrf_exempt
# def payment_success(request):
#     data = {}
#     return render(request, "vendors/success.html", data)

# no csrf token require to go to Failure page. This page displays the message and reason of failure.
@csrf_exempt
def payment_failure(request):
    data = {}
    usr=User.objects.get(id=request.session['id'])
    print("---------------------",usr)
    # oord=OrderMaster.objects.get(userid=usr)
    # print("---------------------",oord)
    pay=Payment.objects.filter(userid=usr)
    print("----------------------",pay)
    print(usr)
    return render(request, "vendors/success.html", data,{'all_cust':usr,'paymnt':pay})


def pdf_view(request):
    nm=request.POST['link']
    print("\n\n C:\\Users\DELL\Desktop\\final jango\cakeart"+nm)
    with open('C:/Users/DELL/Desktop/final jango/cakeart'+nm, 'rb') as pdf:
        print("\n\nPDF===",pdf)
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=License.pdf'
        return response
    pdf.closed


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
    qnty=request.POST['qty']
    flr=Flavour.objects.get(flavour_name=flavor)
    cate=Category.objects.get(category_name=category)
    themes=Theme.objects.get(theme_name=theme)
    em=User.objects.get(firstname=usr)
    dec=Decoration.objects.create(decoration_name=proddec)
    shp=Shape.objects.get(shape_name=shape)
    prod=Products.objects.create(product_name=prodnm,product_price=prodprc,product_type=prodtype,product_desc=proddesc,category_id=cate,user_id=em,product_image=prodimg,theme_id=themes,decoration_id=dec,shape_id=shp,flavor_id=flr,qty=qnty)
    return HttpResponseRedirect(reverse('editprolist'))


def showprodlist(request):
    if 'email' in request.session:
        user=User.objects.get(firstname=request.session['firstname'])
        usr=User.objects.get(id=request.session['id'])
        all_prod=Products.objects.filter(user_id=usr)
        return render(request,"vendors/editprotbl.html",{'all_cust':user,'allprod':all_prod})
    else:
        return HttpResponseRedirect(reverse('login'))


def initiate_payment(request):
    print("----------Inside View--------------")
    # if 'email' in request.session:
    #     user=User.objects.get(firstname=request.session['firstname'])
    #     username = user.email
    #     password = user.pwd
    #     usr = User.objects.get(email=username)
    #     print("---------------------",usr,"------------------------")
    #     now=datetime.date.today()
    #     print("----------------------------------------------Date: ", now)
    #     om=OrderMaster.objects.get(userid=usr,order_dt=now)
    #     print("----------------------Obj:",om,"-----------------------")
    #     amount=om.TotalPrice
    #     return render(request, 'paytm/pay.html',{'all_cust':user,'username':username,'password':password,'amount':amount})
    try:
        user=User.objects.get(firstname=request.session['firstname'])
        username = user.email
        password = user.pwd
        usr = User.objects.get(email=username)
        print("---------------------",usr,"------------------------")
        now=datetime.date.today()
        print("----------------------------------------------Date: ", now)
        om=OrderMaster.objects.get(userid=usr,order_dt=now)
        print("----------------------Obj:",om,"-----------------------")
        amount=om.TotalPrice
        print("-----------------------",amount,"---------------------------")
        print("----------------------------",usr,"-------------------------")
        if usr:
            transaction = Transaction.objects.create(made_by=usr, amount=amount)
            transaction.save()
            merchant_key = settings.PAYTM_SECRET_KEY
            params = (
                ('MID', settings.PAYTM_MERCHANT_ID),
                ('ORDER_ID', str(transaction.order_id)),
                ('CUST_ID', str(transaction.made_by.email)),
                ('TXN_AMOUNT', str(transaction.amount)),
                ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
                ('WEBSITE', settings.PAYTM_WEBSITE),
                    # ('EMAIL', request.user.email),
                    # ('MOBILE_N0', '9911223388'),
                ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
                ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
                    # ('PAYMENT_MODE_ONLY', 'NO'),
            )
            paytm_params = dict(params)
            checksum = generate_checksum(paytm_params, merchant_key)
            transaction.checksum = checksum
            transaction.save()
            paytm_params['CHECKSUMHASH'] = checksum
            paytm_params['all_cust']=user        
            print('SENT: ', checksum)
            return render(request, 'paytm/redirect.html', context=paytm_params)
        else:
            print("----------------------------------Problem occurred-----------------------")
            return render(request,'paytm/pay.html')
    except Exception as pe:
        print("===============================Paytm error---------->",pe)
        return render(request, 'paytm/pay.html', context={'error': 'Wrong Account Details or amount'})
    else:
        return HttpResponseRedirect(reverse("login"))
    


@csrf_exempt
def callback(request):
    if 'email' in request.session:
        received_data = dict(request.POST)
        print("-------------------------",received_data)
        paytm_params = {}

        paytm_checksum = received_data['CHECKSUMHASH'][0]
        print("-----------------------------",paytm_checksum)
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        user=User.objects.get(email=request.session['email'])
        received_data['all_cust'] = user
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
            return render(request, 'paytm/callback.html', context=received_data)
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'paytm/callback.html', context=received_data)