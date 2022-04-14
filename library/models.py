from django.db import models


# Create your models here.
class Category(models.Model):
    CATEGORY_NAME_CHOICES = [
        ("Literature", 'Literature'),
        ("Children", 'Children'),
        ("Computing", 'Computing'),
        ("Entertainment", 'Entertainment'),
        ("Fiction", 'Fiction'),
        ("Personel Development", 'Personel Development'),
        ("History", 'History'),
        ("Romance", 'Romance'),
        ("Religion", 'Religion'),
    ]
    name = models.CharField(
        max_length=100, choices=CATEGORY_NAME_CHOICES, default='Literature')

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='books')
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    total_pages = models.IntegerField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.title} by {self.author} ({self.category}) ({self.published_date})'
