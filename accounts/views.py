from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method=='POST':
           username = request.POST.get('username')
           password= request.POST.get('password')
           user = authenticate(username=username,password=password)

           if user is not None:
               login(request,user)
               return redirect('index')
           else:
               messages.info(request,'username or password incorrect')
               return render(request,'login.html')
    return render(request,'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form=CreateUserForm()
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for' + user)
                return redirect('loginPage')

    context={'form':form}
    return render(request,'register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')