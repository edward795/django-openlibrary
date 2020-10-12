from django.shortcuts import render
from django.core.files.storage import FileSystemStorage 
from .forms import BookForm
from django.shortcuts import redirect
from . models import Book

# Create your views here.
def index(request):
    return render(request,'index.html')


def upload_book(request):
    if request.method == 'POST':
        form=BookForm(request.POST,request.FILES) 
        if form.is_valid:
            form.save() 
            return redirect('book_list')
    else:
        form=BookForm()
    return render(request,'upload.html',{'form':form})

def book_list(request):
    books=Book.objects.all()
    return render(request,'book_list.html',{'books':books})

def filter_view(request):
    if request.method=='POST':
        name=request.POST['search']
        print(name)
        books=Book.objects.all()
        books=Book.objects.filter(title=name)
    return render(request,'book_list.html',{'books':books})
               