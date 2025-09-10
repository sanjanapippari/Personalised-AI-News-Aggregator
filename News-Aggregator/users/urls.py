from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),   # FIXED here
    path('logout/', views.logout_view, name='logout'),
    path('liked/', views.liked_articles_view, name='liked_articles'),
path('disliked/', views.disliked_articles_view, name='disliked_articles'),

]
