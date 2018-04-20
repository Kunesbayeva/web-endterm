from django.conf.urls import url
from . import views
urlpatterns = [
    url ('blogs/', views.blog_list, name="blog_list"),
    url ('blogs/<int:blog_id>', views.blog_detail, name="blog_detail"),
]