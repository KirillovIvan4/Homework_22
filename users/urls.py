from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', next_page='online_store:product_list'), name='login'),
    path('logout/', LogoutView.as_view(next_page='online_store:product_list'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]