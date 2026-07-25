from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserDetails
import re

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        pasw=request.POST['pasw']
        cpasw=request.POST['cpasw']
        try:
            userExists=User.objects.get(username=uname)
            messages.error(request,'Username Already Exists')
            return redirect(register)
        except:
            if(pasw==cpasw):
                pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
                if(re.match(pattern,pasw)):
                    User.objects.create_user(
                        first_name=fname,
                        last_name=lname,
                        username=uname,
                        password=pasw,
                        email=email
                    )
                    return redirect(login_)
                else:
                    messages.error(request,'Provide Strong Password')
                    return redirect(register)
    return render(request,'register.html')


def login_(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        uname=request.POST['uname']
        pasw=request.POST['pasw']
        user=authenticate(username=uname,password=pasw)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Enter Correct Credentials')
            return redirect(login_)
    return render(request,'login_.html')


@login_required(login_url=login_)
def logout_(request):
    logout(request)
    messages.success(request,'Logout Successfull')
    return redirect(login_)


@login_required(login_url=login_)
def resetPasw(request):
    if request.method=='POST':
        if 'oldpasw' in request.POST:
            oldpasw=request.POST['oldpasw']
            user=authenticate(username=request.user,password=oldpasw)
            if user:
                return render(request,'resetPasw.html',{'new':True})
            else:
                messages.error(request,'Password Wrong')
                return redirect(resetPasw)
        if 'newpasw' in request.POST:
            newpasw=request.POST['newpasw']
            cnewpasw=request.POST['cnewpasw']
            pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
            if newpasw==cnewpasw:
                user=User.objects.get(username=request.user)
                if re.match(pattern,newpasw):
                    if user.check_password(newpasw):
                        messages.error(request,'Same password is used')
                        return redirect(resetPasw)
                    else:
                        user.set_password(newpasw)
                        user.save()
                        update_session_auth_hash(request,user)
                        messages.success(request,'Password Changed Successfully')
                        return redirect(profile)
                else:
                    messages.error(request,'Use Strong Password')
                    return redirect(resetPasw)
            else:
                messages.error(request,'Confirm Password Mismatched')
                return redirect(resetPasw)
    return render(request,'resetPasw.html')



def forgetPasw(request):
    if request.method=='POST':
        if 'uname' in request.POST:
            uname=request.POST['uname']
            try:
                user=User.objects.get(username=uname)
                if user:
                    request.session['fp_user']=user.username
                    return render(request,'forgetPasw.html',{'new':True})
                else:
                    messages.error(request,'Username Not Found')
                    return redirect(forgetPasw)
            except:
                messages.error(request,'Username Not Found')
                return redirect(forgetPasw)
        if 'newpasw' in request.POST:
            newpasw=request.POST['newpasw']
            cnewpasw=request.POST['cnewpasw']
            pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
            if newpasw==cnewpasw:
                user=request.session.get('fp_user')
                if re.match(pattern,newpasw):
                    try:
                        isUser=User.objects.get(username=user)
                        if isUser.check_password(newpasw):
                            isUser.set_password(newpasw)
                            isUser.save()
                            messages.success(request,'Password is Changed')
                            return redirect(login_)
                        else:
                            messages.error(request,'Same password is Used')
                            return redirect(forgetPasw)
                    except:
                        messages.error(request,'Username Not Found')
                        return redirect(forgetPasw)
                else:
                    messages.error(request,'Use Strong Password')
                    return redirect(forgetPasw)
            else:
                messages.error(request,'Password is Mismatched')
                return redirect(forgetPasw)
    return render(request,'forgetPasw.html')



@login_required(login_url=login_)
def profile(request):
    try:
        data=UserDetails.objects.get(userId=request.user)
    except:
        return render(request,'profile.html',{'incomplete':True})
    return render(request,'profile.html',{'data':data,'incomplete':False})


@login_required(login_url=login_)
def updateProfile(request):
    try:
        user_data=UserDetails.objects.get(userId=request.user)
    except:
        user_data=User.objects.get(username=request.user)
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        pincode=request.POST['pincode']
        try:
            ud=UserDetails.objects.get(userId=request.user)
            pic=request.FILES['pic'] if 'pic' in request.FILES else ud.pic
            u=User.objects.get(username=request.user)
            u.first_name=fname
            u.last_name=lname
            u.email=email
            u.save()
            ud.phone=phone
            ud.address=address
            ud.pincode=pincode
            ud.pic=pic
            ud.save()
            return redirect(profile)
        except:
            pic=request.FILES['pic'] if 'pic' in request.FILES else 'default.jpg'
            u=User.objects.get(username=request.user)
            u.first_name=fname
            u.last_name=lname
            u.email=email
            u.save()
            UserDetails.objects.create(
                userId=request.user,phone=phone,address=address,pincode=pincode,pic=pic
            )
            return redirect(profile)
    return render(request,'updateProfile.html',{'data':user_data})


@login_required(login_url=login_)
def completeProfile(request):
    if request.method=='POST':
        phone=request.POST['phone']
        address=request.POST['address']
        pincode=request.POST['pincode']
        pic=request.FILES['pic'] if 'pic' in request.FILES else 'user.png'
        UserDetails.objects.create(
            userId=request.user,
            phone=phone,
            address=address,
            pincode=pincode,
            pic=pic
        )
        messages.success(request,'Profile details Completed')
        return render(request,'profile.html',{'incomplete':False})
    return render(request,'completeProfile.html')


@login_required(login_url=login_)
def deleteProfile(request):
    User.objects.get(username=request.user).delete()
    return redirect(login_)

