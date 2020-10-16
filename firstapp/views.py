from django.shortcuts import render
from django.core.files.storage import FileSystemStorage 
from .forms import BookForm
from django.shortcuts import redirect
from . models import Book
from .filters import BookFilters
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='loginPage')
def book_list(request):
    books=Book.objects.all()
    return render(request,'book_list.html',{'books':books})

def filter_view(request):
    if request.method=='POST':
        name=request.POST['search']
        books=Book.objects.all()
        books=Book.objects.filter(title=name)
    return render(request,'book_list.html',{'books':books})

@login_required(login_url='loginPage')
def delete_book(request,pk):
    if request.method=='POST':
        book=Book.objects.get(pk=pk)
        book.delete()
        return redirect('book_list')

class BookListView(ListView):
    model=Book
    template_name='filter_list.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['filter']=BookFilters(self.request.GET,queryset=self.get_queryset()) 
        return context   