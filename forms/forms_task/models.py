"""
models.py
"""

from django.db import models


# Create your models here.
class Book(models.Model):
    """
    book model
    """

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)


class Car(models.Model):
    """
    car model
    """

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    transmission = models.CharField(
        max_length=10, choices=(("automatic", "Automatic"), ("manual", "Manual"))
    )


class Song(models.Model):
    """
    song model
    """

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    genres = (
        ("pop", "Pop"),
        ("rock", "Rock"),
        ("hip hop", "Hip Hop"),
        ("electronic", "Electronic"),
    )
    genre = models.CharField(max_length=10, choices=genres)
    duration = models.FloatField()


class Movie(models.Model):
    """
    movie model
    """

    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    release_year = models.IntegerField()
    choice = (
        ("g", "G"),
        ("h", "H"),
        ("i", "I"),
        ("j", "J"),
        ("k", "K"),
        ("l", "L"),
        ("m", "M"),
        ("n", "N"),
        ("o", "O"),
        ("p", "P"),
        ("q", "Q"),
        ("r", "R"),
    )
    rating = models.CharField(max_length=10, choices=choice)


class JobPosting(models.Model):
    """
    job model
    """

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(
        max_length=10,
        choices=(("ft", "Full-time"), ("pt", "Part-time"), ("c", "Contract")),
    )


class Category(models.Model):
    """
    category model
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class PostCategory(models.Model):
    """
    category model
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    product model
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Project(models.Model):
    """
    project model
    """

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    task model
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Post(models.Model):
    """
    post model
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Student(models.Model):
    """
    student model
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    course model
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    """
    enrollment model
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
