from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,  name='home'),
    path('event/', views.PostList.as_view(), name='news_page'),
    path('login/', views.login, name="login"),
    path('event/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]



