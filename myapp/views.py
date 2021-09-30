from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import post,profile
# Create your views here.
def login_page(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user     =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request,'index.html')

def Home(request):
    if request.user.is_authenticated:
        user = request.user
        name =user.first_name +' '+user.last_name
        pro = profile.objects.get(user=user)
        pos = post.objects.filter(user=user)
        context = {'name':name,'pro':pro,'pos':pos}
        return render(request,'home.html',context)
    else:
        return redirect('login')

def Profile(request):
        if request.user.is_authenticated:
            pro = profile.objects.get(user=request.user)
            return render(request,'profile.html',{"pro":pro})
        else:
            return redirect('login')
def Logout(request):

    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

def register(request):
            if request.method=='POST':
                username = request.POST['username']
                password1 = request.POST['password1']
                password2= request.POST['password2']
                if password1==password2:
                    user = User.objects.create(username=username)
                    user.set_password(password2)
                    user.save()
                    return redirect('login')
                else:
                    return redirect('login')
            else:
                return redirect('login')

def creat_post (request):
    if request.method=='POST':
        content = request.POST['content']
        p = post.objects.create(user=request.user,post=content)
        p.save()
        return redirect('home')

def update_profile(request):
    if request.method == 'POST':
        status=request.POST['status']
        loc = request.POST['location']

        p = profile.objects.get(user=request.user)
        p.status=status
        p.location=loc
        p.save()
        return redirect ('home')
            
