"""
views.py
"""

from django.views.generic import CreateView, TemplateView
from . import forms
from . import models
from rest_framework import generics, permissions
from . import serializers
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

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


###  API  ###
class BookListView(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    lookup_field = 'slug'
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class CarList(generics.ListCreateAPIView):
    """
    API view for listing and creating Car objects.
    """

    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Car object.
    """

    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class SongList(generics.ListCreateAPIView):
    """
    API view for listing and creating Song objects.
    """

    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Song object.
    """

    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class MovieList(generics.ListCreateAPIView):
    """
    API view for listing and creating Movie objects.
    """

    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    API view for retrieving, updating, and deleting a Movie object.
    """

    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class JobPostingList(generics.ListCreateAPIView):
    """
    API view for listing and creating JobPosting objects.
    """

    queryset = models.JobPosting.objects.all()
    serializer_class = serializers.JobPostingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class JobPostingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a JobPosting object.
    """

    queryset = models.JobPosting.objects.all()
    serializer_class = serializers.JobPostingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductList(generics.ListCreateAPIView):
    """API view for listing and creating Product objects."""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Product object.
    """

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class TaskList(generics.ListCreateAPIView):
    """API view for listing and creating Task objects."""

    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Task object.
    """

    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class PostList(generics.ListCreateAPIView):
    """
    API view for listing and creating Post objects.
    """

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Post object.
    """

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class PostCategoryList(generics.ListCreateAPIView):
    """
    API view for listing and creating PostCategory objects.
    """

    queryset = models.PostCategory.objects.all()
    serializer_class = serializers.PostCategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class PostCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a postcategory object.
    """

    queryset = models.PostCategory.objects.all()
    serializer_class = serializers.PostCategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CategoryList(generics.ListCreateAPIView):
    """
    API view for listing and creating Category objects.
    """

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Category object.
    """

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProjectList(generics.ListCreateAPIView):
    """
    API view for listing and creating Project objects.
    """

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Project object.
    """

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class StudentList(generics.ListCreateAPIView):
    """
    API view for listing and creating Student objects.
    """

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Student object.
    """

    queryset = models.Student.objects.all()
    serializer_class = serializers.CarSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CourseList(generics.ListCreateAPIView):
    """
    API view for listing and creating Course objects.
    """

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Course object.
    """

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class EnrollmentListView(generics.ListCreateAPIView):
    queryset = models.Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    
class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]