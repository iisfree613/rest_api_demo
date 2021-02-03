from django.conf.urls import url, include

from .views import add_book, show_book


urlpatterns = [
    url(r'add_book$', add_book),
    url(r'show_book$', show_book),
]