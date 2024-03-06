"""
views.py
"""

from django.views.generic import CreateView, TemplateView
from . import forms
from . import models

# Create your views here.


class Success(TemplateView):
    """
    success view
    """

    template_name = "success.html"


class Index(TemplateView):
    """
    index view
    """

    template_name = "index.html"


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

    model = models.Car
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


class AddCategory(CreateView):
    """
    category view
    """

    template_name = "add.html"
    form_class = forms.CategoryForm
    success_url = "add_product"


class AddProject(CreateView):
    """
    category view
    """

    template_name = "add.html"
    form_class = forms.ProjectForm
    success_url = "add_task"


class AddPostCategory(CreateView):
    """
    category view
    """

    template_name = "add.html"
    form_class = forms.PostCategoryForm
    success_url = "add_post"


class AddStudent(CreateView):
    """
    category view
    """

    template_name = "add.html"
    form_class = forms.StudentForm
    success_url = "add_enrollment"


class AddCourse(CreateView):
    """
    category view
    """

    template_name = "add.html"
    form_class = forms.CourseForm
    success_url = "add_enrollment"
