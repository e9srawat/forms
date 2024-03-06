from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("add_book", views.AddBook.as_view(), name="add_book"),
    path("add_car", views.AddCar.as_view(), name="add_car"),
    path("add_song", views.AddSong.as_view(), name="add_song"),
    path("add_movie", views.AddMovie.as_view(), name="add_movie"),
    path("add_job", views.AddJob.as_view(), name="add_job"),
    path("add_category", views.AddCategory.as_view(), name="add_category"),
    path("add_product", views.AddProduct.as_view(), name="add_product"),
    path("add_project", views.AddProject.as_view(), name="add_project"),
    path("add_task", views.AddTask.as_view(), name="add_task"),
    path("add_postcategory", views.AddPostCategory.as_view(), name="add_postcategory"),
    path("add_post", views.AddPost.as_view(), name="add_post"),
    path("add_student", views.AddStudent.as_view(), name="add_student"),
    path("add_course", views.AddCourse.as_view(), name="add_course"),
    path("add_enrollment", views.AddEnrollment.as_view(), name="add_enrollment"),
    path("success", views.Success.as_view(), name="success"),
]