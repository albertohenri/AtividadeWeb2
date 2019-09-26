from django.conf.urls import url

from .views import BookCreate, BookDestroy, BookGet, BookList, BookUpdate

urlpatterns = [
    url(r'books/$', BookList.as_view()),
    url(r'books/(?P<pk>\d+)/$', BookDestroy.as_view()),
    url(r'books/add/$', BookCreate.as_view()),
    url(r'books/get/(?P<pk>\d+)/$', BookGet.as_view()),
    url(r'books/edit/(?P<pk>\d+)/$', BookUpdate.as_view()),
]
