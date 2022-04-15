from django.urls import path
from rest_framework import routers

from .views import AuthorView, BookView, CategoryView, PublisherView

router = routers.DefaultRouter()
router.register('books', BookView)
router.register('categories', CategoryView)
router.register('authors', AuthorView)
router.register('publishers', PublisherView)

urlpatterns = [

]

urlpatterns += router.urls
