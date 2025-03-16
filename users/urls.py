from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, PasswordRecoveryView, email_verification
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return (
#             str(user.pk) + str(timestamp) +
#             str(user.is_email_verified)
#         )
#
# token_generator = EmailVerificationTokenGenerator()

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', next_page='online_store:product_list'), name='login'),
    path('logout/', LogoutView.as_view(next_page='online_store:product_list'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path("email-confirm/<str:token>/", email_verification, name="email_verification"),
    path('password_recovery/',PasswordRecoveryView.as_view(), name='password_recovery'),

]