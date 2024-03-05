"""
forms.py
"""

from django import forms
from .models import Book, Car, Song, Movie, JobPosting, Product, Task, Post, Enrollment


class BookForm(forms.ModelForm):
    """
    book form
    """

    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
            "author": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 50,
                }
            ),
            "publication_date": forms.DateInput(
                attrs={
                    "style": "width: 200px;",
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "isbn": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 13,
                    "minlength": 13,
                }
            ),
        }


class CarForm(forms.ModelForm):
    """
    car form
    """

    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "make": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 50,
                }
            ),
            "model": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 50,
                }
            ),
            "year": forms.NumberInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
            "transmission": forms.RadioSelect(),
        }


class SongForm(forms.ModelForm):
    """
    song form
    """

    class Meta:
        model = Song
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
            "artist": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 50,
                }
            ),
            "genre": forms.Select(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
            "duration": forms.NumberInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
        }


class MovieForm(forms.ModelForm):
    """
    movie form
    """

    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
            "director": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 50,
                }
            ),
            "rating": forms.Select(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
            "release_year": forms.NumberInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
        }


class JobPostingForm(forms.ModelForm):
    """
    job form
    """

    class Meta:
        model = JobPosting
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
            "company": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
            "employment_type": forms.Select(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
        }


class ProductForm(forms.ModelForm):
    """
    product form
    """

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
            "category": forms.Select(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
        }


class TaskForm(forms.ModelForm):
    """
    task form
    """

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
            "project": forms.Select(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
        }


class PostForm(forms.ModelForm):
    """
    post form
    """

    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
            "category": forms.Select(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
        }


class EnrollmentForm(forms.ModelForm):
    """
    enrollment form
    """

    class Meta:
        model = Enrollment
        fields = "__all__"
        widgets = {
            "student": forms.Select(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 100,
                }
            ),
            "course": forms.Select(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                }
            ),
            "grade": forms.TextInput(
                attrs={
                    "style": "width: 200px;",
                    "class": "form-control",
                    "maxlength": 2,
                }
            ),
        }
