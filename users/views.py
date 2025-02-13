from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.views import View




class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('online_store:product_list')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        login(self.request, user)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'kirillov.ivankirillov1993@yandex.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

    # def post(self, request, *args, **kwargs):
    #     form_data = request.POST  # Для form-data
    #     json_data = request.body  # Для raw JSON-данных
    #     print("Form Data:", form_data)
    #     print("JSON Data:", json_data)


