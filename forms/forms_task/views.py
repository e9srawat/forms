"""
views.py
"""
from django.views.generic import CreateView, TemplateView
from . import forms

# Create your views here.


class Success(TemplateView):
    """
    success view
    """

    template_name = "success.html"


class AddBook(CreateView):
    """
    book view
    """

    template_name = "add.html"
    form_class = forms.BookForm
    success_url = "success"


class AddCar(CreateView):
    """
    car view
    """

    template_name = "add.html"
    form_class = forms.CarForm
    success_url = "success"


class AddSong(CreateView):
    """
    song view
    """

    template_name = "add.html"
    form_class = forms.SongForm
    success_url = "success"


class AddMovie(CreateView):
    """
    success view
    """

    template_name = "add.html"
    form_class = forms.MovieForm
    success_url = "success"


class AddJob(CreateView):
    """
    job view
    """

    template_name = "add.html"
    form_class = forms.JobPostingForm
    success_url = "success"


class AddProduct(CreateView):
    """
    product view
    """

    template_name = "add.html"
    form_class = forms.ProductForm
    success_url = "success"


class AddTask(CreateView):
    """
    task view
    """

    template_name = "add.html"
    form_class = forms.TaskForm
    success_url = "success"


class AddPost(CreateView):
    """
    post view
    """

    template_name = "add.html"
    form_class = forms.PostForm
    success_url = "success"


class AddEnrollment(CreateView):
    """
    enrollment view
    """

    template_name = "add.html"
    form_class = forms.EnrollmentForm
    success_url = "success"
