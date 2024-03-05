from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from django.views.generic import CreateView ,TemplateView

# Create your views here.


# def index(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             return HttpResponse("/thanks/")
#     else:
#         form = BookForm()

#     return render(request, "add_book.html", {"form": form})

class Success(TemplateView):
    template_name = "success.html"

class Add_book(CreateView):
    template_name = "add.html"
    form_class = forms.BookForm
    success_url = 'success'
    
class Add_Car(CreateView):
    template_name = "add.html"
    form_class = forms.CarForm
    success_url = 'success'
    
class Add_Song(CreateView):
    template_name = "add.html"
    form_class = forms.SongForm
    success_url = 'success'
    
class Add_Movie(CreateView):
    template_name = "add.html"
    form_class = forms.MovieForm
    success_url = 'success'

class Add_Job(CreateView):
    template_name = "add.html"
    form_class = forms.JobPostingForm
    success_url = 'success'
    
class Add_Product(CreateView):
    template_name = "add.html"
    form_class = forms.ProductForm
    success_url = 'success'

class Add_Task(CreateView):
    template_name = "add.html"
    form_class = forms.TaskForm
    success_url = 'success'
    
class Add_Post(CreateView):
    template_name = "add.html"
    form_class = forms.PostForm
    success_url = 'success'

class Add_Enrollment(CreateView):
    template_name = "add.html"
    form_class = forms.EnrollmentForm
    success_url = 'success'