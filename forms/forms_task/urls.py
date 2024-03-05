from django.urls import path
from . import views

urlpatterns = [
    path("add_book", views.Add_book.as_view(), name="add_book"),
    path("add_car", views.Add_Car.as_view(), name="add_car"),
    path("add_song", views.Add_Song.as_view(), name="add_song"),
    path("add_movie", views.Add_Movie.as_view(), name="add_movie"),
    path("add_job", views.Add_Job.as_view(), name="add_job"),
    path("add_product", views.Add_Product.as_view(), name="add_product"),
    path("add_task", views.Add_Task.as_view(), name="add_task"),
    path("add_post", views.Add_Post.as_view(), name="add_post"),
    path("add_enrollment", views.Add_Enrollment.as_view(), name="add_enrollment"),
    path("success", views.Success.as_view(), name="success"),
]