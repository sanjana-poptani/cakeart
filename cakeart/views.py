from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from random import *
from .utils import *
# Create your views here.
def loadusrpwd(request):
    return render(request,"cakeart/my-account015e.html")

def regpg(request):
    return render(request,"cakeart/my-account4437.html")

def collctdata(request):
    try:
        if request.POST['type']=='Customer':
            user_role=request.POST['type']
            fnm=request.POST['Firstname']
            lnm=request.POST['Lastname']
            dobb=request.POST['dob']
            gender=request.POST['Gender']
            con=request.POST['cont']
            add=request.POST['Address']
            pincode=request.POST['pincode']
            lic=request.FILES.get('bak_lic')
            shop=request.POST['shpnm']
            em=request.POST['email1']
            passw=request.POST['password1']
            passwd=request.POST['password2']
            user=User.objects.filter(email=em)
            if user:
                msg="Email already exists!!"
                return render(request,"cakeart/my-account4437.html",{'message':msg})
            else:
                if passw==passwd:
                    user_type = User_type.objects.get(utname=user_role)
                    Otp = randint(10000,99999)
                    new_customer=User.objects.create(utid=user_type,firstname=fnm,lastname=lnm,DOB=dobb,gender=gender,contact=con,address=add,pinc=pincode,License=lic,shopnm=shop,email=em,pwd=passwd,otp=Otp)
                    subject="CakeArt : Account Verification"
                    sendmail(subject,'mail_template',em,{'name':fnm,'otp':Otp,'link':'http://localhost:8000/enterprise/user_verify/'})
                    return HttpResponseRedirect(reverse('otp'))
                #return HttpResponseRedirect(reverse('acc'))
                else:
                    msg="Password and ConfirmPassword doesn't match!!"
                    return render(request,"cakeart/my-account4437.html",{'message':msg})
        elif request.POST['type']=='Vendor':
            user_role=request.POST['type']
            fnm=request.POST['Firstname']
            lnm=request.POST['Lastname']
            dobb=request.POST['dob']
            gender=request.POST['Gender']
            con=request.POST['cont']
            add=request.POST['Address']
            pincode=request.POST['pincode']
            lic=request.FILES.get('bak_lic')
            shop=request.POST['shpnm']
            em=request.POST['email1']
            passw=request.POST['password1']
            passwd=request.POST['password2']
            user=User.objects.filter(email=em)
            if user:
                msg="Email already exists!!"
                return render(request,"cakeart/my-account4437.html",{'message':msg})
            else:
                if passw==passwd:
                    user_type = User_type.objects.get(utname=user_role)
                    #user_type=User_type.objects.create(utname=user_role)
                    Otp= randint(10000,99999)
                    new_customer=User.objects.create(utid=user_type,firstname=fnm,lastname=lnm,DOB=dobb,gender=gender,contact=con,address=add,pinc=pincode,License=lic,shopnm=shop,email=em,pwd=passwd,otp=Otp)
                    subject="CakeArt : Account Verification"
                    sendmail(subject,'mail_template',em,{'name':fnm,'otp':Otp,'link':'http://localhost:8000/enterprise/user_verify/'})
                    return HttpResponseRedirect(reverse('otp'))
                 #   return HttpResponseRedirect(reverse('acc'))
                else:
                    msg="Password and ConfirmPassword doesn't match!!"
                    return render(request,"cakeart/my-account4437.html",{'message':msg})
        elif request.POST['type']=='Baker':
            user_role=request.POST['type']
            fnm=request.POST['Firstname']
            lnm=request.POST['Lastname']
            dobb=request.POST['dob']
            gender=request.POST['Gender']
            con=request.POST['cont']
            add=request.POST['Address']
            pincode=request.POST['pincode']
            lic=request.FILES.get('bak_lic')
            shop=request.POST['shpnm']
            em=request.POST['email1']
            passw=request.POST['password1']
            passwd=request.POST['password2']
            user=User.objects.filter(email=em)
            if user:
                msg="Email already exists!!"
                return render(request,"cakeart/my-account4437.html",{'message':msg})
            else:
                if passw==passwd:
                    user_type = User_type.objects.get(utname=user_role)
                    #user_type=User_type.objects.create(utname=user_role)
                    Otp=randint(10000,99999)
                    new_customer=User.objects.create(utid=user_type,firstname=fnm,lastname=lnm,DOB=dobb,gender=gender,contact=con,address=add,pinc=pincode,License=lic,shopnm=shop,email=em,pwd=passwd,otp=Otp)
                    subject="CakeArt : Account Verification"
                    sendmail(subject,'mail_template',em,{'name':fnm,'otp':Otp,'link':'http://localhost:8000/enterprise/user_verify/'})
                    return HttpResponseRedirect(reverse('otp'))
                #    return HttpResponseRedirect(reverse('acc'))
                else:
                    msg="Password and ConfirmPassword doesn't match!!"
                    return render(request,"cakeart/my-account4437.html",{'message':msg})
        else:
            return HttpResponse("In Else")
    except User.DoesNotExist:
        message="This user does not exists"
        return render(request,"cakeart/my-account4437.html",{'message':message})


def otp_load(request):
    return render(request,"cakeart/otp.html")

def loadindex(request):
    #return render(request,"cakeart/index.html")
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"cakeart/index.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))

def loadblogpg(request):
    return render(request,"cakeart/blog.html")

def loadrecipe(request):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"cakeart/recipes.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))

def loadbshop(request):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"cakeart/shop.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))

def forgtpwd(request):
    return render(request,"cakeart/my-account798d.html")

def blog2(request):
    return render(request,"cakeart/blog9b5f.html")

def recipe2(request):
    return render(request,"cakeart/recipesbd13.html")

def show(request):
    all_users=User.objects.all()
    return render(request,"cakeart/success.html",{'key1':all_users})

def showdata(request):
    return render(request,"cakeart/success.html")



def contact(request):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        feedbacks=Feedback.objects.all()
        return render(request,"cakeart/contact.html",{'all_cust':user,'fdbk':feedbacks})
    else:
        return HttpResponseRedirect(reverse('login'))

def loadabt(request):
    return render(request,"cakeart/about-us.html")

def LoginUser(request):
    try:
        if request.POST['role']=="customer":
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.get(email=email)
            if user:
                if user.pwd==password:
                    request.session['email'] = user.email
                    request.session['firstname'] = user.firstname
                    request.session['id']=user.id
                    return HttpResponseRedirect(reverse("index"))
                else:
                    msg = "Password is incorrect"
                    return render(request,"cakeart/my-account015e.html",{'msg':msg})
            else:
                msg = "User doesnot exist"
                return render(request,"cakeart/my-account015e.html",{'msg':msg})
        elif request.POST['role']=="Admin":
            email=request.POST['email']
            password=request.POST['password']
            if email=="sanjanapoptani54@gmail.com" and password=="admin":
                request.session['email'] = "sanjanapoptani54@gmail.com"
                request.session['firstname'] = "sanjana"
                return HttpResponseRedirect(reverse("table"))
            else:
                msg="Login failed!!"
                return render(request,"cakeart/my-account015e.html",{'msg':msg})
        elif request.POST['role']=="Vendor":
            email=request.POST['email']
            password=request.POST['password']
            user=User.objects.get(email=email)
            if user:
                if user.pwd==password:
                    request.session['email'] = user.email
                    request.session['firstname'] = user.firstname
                    request.session['id']=user.id
                    return HttpResponseRedirect(reverse("showproduct11"))
                else:
                    msg = "Password is incorrect"
                    return render(request,"cakeart/my-account015e.html",{'msg':msg})
            else:
                msg = "User doesnot exist"
                return render(request,"cakeart/my-account015e.html",{'msg':msg})
    
        elif request.POST['role']=="Baker":
            email=request.POST['email']
            password=request.POST['password']
            user=User.objects.get(email=email)
            if user:
                if user.pwd==password:
                    request.session['email'] = user.email
                    request.session['firstname'] = user.firstname
                    request.session['id']=user.id
                    return HttpResponseRedirect(reverse("welcome"))
                else:
                    msg = "Password is incorrect"
                    return render(request,"cakeart/my-account015e.html",{'msg':msg})
            else:
                msg = "User doesnot exist"
                return render(request,"cakeart/my-account015e.html",{'msg':msg})
    except:
        msg="No such user"
        return render(request,"cakeart/my-account015e.html",{'mesg':msg})


def membership(request):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"cakeart/membership.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))

def loadvisitorindex(request):
    print("Index Called")
    return render(request,"cakeart/visitorindex.html")

def forgotPassword(request):
    email = request.POST['email']
    try:
        user = User.objects.get(email=email)
        if user:
            if user.email == email:
                Otp = randint(10000, 99999)
                user.otp = Otp
                user.save()
                email_subject = "This is your new OTP"
                # link = "https://localhost:8000/example?email="+email+"&otp="+otp+"&random="+random
                sendmail(email_subject, 'mail_template', email, {'otp': Otp,'link':"https://localhost:8000/enterprise/password-recovery"})
                return HttpResponseRedirect(reverse('otp2'))
            else:
                message = 'This email does not match'
                return render(request, "cakeart/my-account798d.html", {'message': message})
        else:
            message = 'This email is not available'
            return render(request, "cakeart/my-account798d.html", {'message': message})
    except:
        message = 'Email not found'
        return render(request, "cakeart/my-account798d.html", {'message': message})

def loadprofile(request,pk):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        usr=User.objects.get(pk=pk)
        return render(request,"cakeart/myprofile.html",{'all_cust':user,'profile':usr})
    else:
        return HttpResponseRedirect(reverse('login'))
    
def updtprofile(request,pk):
    user=User.objects.get(pk=pk)
    user.firstname=request.POST['firstname']
    user.lastname=request.POST['lastname']
    user.DOB=request.POST['dob']
    user.gender=request.POST['Gender']
    user.contact=request.POST['cont']
    user.address=request.POST['Address']
    user.pinc=request.POST['pincode']
    user.email=request.POST['email1']
    user.save()
    msg="Your data changed successfully!!"
    return HttpResponseRedirect(reverse('index'),{'msg':msg})

def changepasswd(request):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        id=request.session['id']
        user=User.objects.get(id=id)
        old_password=user.pwd
        current = request.POST['current']
        new_password = request.POST['new_password']
        confirm = request.POST['confirm']
        if old_password == current and new_password == confirm:
            user.password = confirm
            user.save()
            message = "Your Password has been changed successfully:)"
            return render(request, "cakeart/pwdchnge.html",{'msg':message,'all_cust':user})
        else:
            error_msg = "Incorrect Password , Try Again  !!"
            return render(request, "cakeart/chngepwd.html", {'error_msg': error_msg}) 
    else:
        return HttpResponseRedirect(reverse('login'))
     

def loadchngepwd(request):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"cakeart/chngepwd.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))

def chngedpwd(request):
    return render(request,"cakeart/pwdchnge.html")

def logout(request):
    del request.session['email']
    del request.session['firstname']
    del request.session['id']
    return HttpResponseRedirect(reverse('login'))

def otp_load2(request):
    return render(request,"cakeart/otp2.html")

def ResetPassword(request):
    otp = request.POST['otp']
    checkotp=User.objects.filter(otp=otp)
    if checkotp:
        newPassword = request.POST['new']
        confirmPassword = request.POST['confirm']
        email = request.POST['email1']
        try:
            user = User.objects.get(email=email)
            if confirmPassword == newPassword and str(user.otp) == otp:
                user.password = newPassword
                user.save()
                return HttpResponseRedirect(reverse('login'))
            else:
                message = "Password and confirm password doesn't match"
                return render(request, "cakeart/otp2.html", {'message': message})
        except:
            message = "Invalid request"
            return render(request, "cakeart/otp2.html", {'message': message})
    else:
        message="Incorrect Otp!!"
        return render(request,"cakerart/otp2.html",{'message':message})
    
def profileupdt(request,pk):
    if 'email' in request.session:
        usr=User.objects.get(pk=pk)
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"cakeart/editprofile.html",{'all_cust':user,'profile':usr})
    else:
        return HttpResponseRedirect(reverse('login'))

def loadcart(request):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"cakeart/cart.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))

def feedback_report(request):
    try:
        #print("\n\nBool=====",'email' in request.session)
        #print("Get===",request.session.get('email'))
        if 'email' in request.session:
            abt=request.POST['about']
            feedbck=request.POST['Message']
            email=request.session['email']
            usr=User.objects.get(email=email)
            Feedback.objects.create(feedback_abt=abt,feedback_text=feedbck,to_vb=usr)
            #print("==================1==============\n\n")
            return HttpResponseRedirect(reverse('fdbk'))        
    except Exception as e:
        print("\n\nError====",e,"\n\n")
        err="Some error occurred!!"
        return render(request,"cakeart/contact.html",{'error':err})

        
def feedback_reply(request):
    if 'email' in request.session:
        all_cust = User.objects.all()
        user=User.objects.get(firstname=request.session['firstname'])
        return render(request,"cakeart/feedbackreplay.html",{'all_cust':user})
    else:
        return HttpResponseRedirect(reverse('login'))