from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages

from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing_recipient, Message, Mailing, Mailing_attempt
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail

class Mailing_recipientCreateView(LoginRequiredMixin, CreateView):
    model = Mailing_recipient
    fields = ['email', 'full_name', 'comment']
    #template_name = 'Mailing_recipient_form.html'
    success_url = reverse_lazy('mailing:mailing_recipient_list')

@method_decorator(cache_page(60 * 15), name='dispatch')
class Mailing_recipientListView(ListView):
    model = Mailing_recipient
    #template_name = 'Mailing_recipient_list.html'
    context_object_name = 'mailing_recipient'

@method_decorator(cache_page(60 * 15), name='dispatch')
class Mailing_recipientDetailView(DetailView):
    model = Mailing_recipient
    #template_name = 'Mailing_recipient_detail.html'
    context_object_name = 'mailing_recipient'



class Mailing_recipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing_recipient
    fields = ['email', 'full_name', 'comment']
    success_url = reverse_lazy('mailing:mailing_recipient_list')


class Mailing_recipientDeleteView(DeleteView):
    model = Mailing_recipient
    #template_name = 'Mailing_recipient_confirm_delete.html'
    success_url = reverse_lazy('mailing:mailing_recipient_list')
    
    
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['subject_letter', 'body_letter']
    #template_name = 'Message_form.html'
    success_url = reverse_lazy('mailing:message_list')

@method_decorator(cache_page(60 * 15), name='dispatch')
class MessageListView(ListView):
    model = Message
    #template_name = 'Message_list.html'
    context_object_name = 'message'

@method_decorator(cache_page(60 * 15), name='dispatch')
class MessageDetailView(DetailView):
    model = Message
    #template_name = 'Message_detail.html'
    context_object_name = 'message'

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ['subject_letter', 'body_letter']
    success_url = reverse_lazy('mailing:message_list')

class MessageDeleteView(DeleteView):
    model = Message
    #template_name = 'Message_confirm_delete.html'
    success_url = reverse_lazy('mailing:message_list')
    
class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    fields = ['date_and_time_of_sending_end', 'status', 'message', 'recipients']
    #template_name = 'Mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingListView(ListView):
    model = Mailing
    #template_name = 'Mailing_list.html'
    context_object_name = 'mailing'

    def get_queryset(self):
        return Mailing.objects.filter(status='launched')

@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingDetailView(DetailView):
    model = Mailing
    context_object_name = 'mailing'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        subject_letter = request.POST.get("subject_letter")
        body_letter = request.POST.get("body_letter")
        recipients = [recipient.email for recipient in self.object.recipients.all()]

        # Логика отправки писем и создания попыток
        for recipient in recipients:
            try:
                # Отправка письма
                send_mail(
                    subject_letter,
                    body_letter,
                    EMAIL_HOST_USER,  # Отправитель
                    [recipient],  # Получатель
                    fail_silently=False,
                )

                # Создание записи об успешной попытке
                Mailing_attempt.objects.create(
                    status=Mailing_attempt.SUCCESSFUL,
                    mail_server_response="Письмо успешно отправлено",
                    message=self.object,
                )

            except Exception as e:
                # Создание записи о неудачной попытке
                Mailing_attempt.objects.create(
                    status=Mailing_attempt.NOT_SUCCESSFUL,
                    mail_server_response=str(e),
                    message=self.object,
                )

        messages.success(request, "Рассылка завершена. Проверьте попытки отправки.")
        return redirect('mailing:mailing_list')
        # recipients = request.POST.getlist("recipient")
        # send_mail(
        #     subject_letter,
        #     body_letter,
        #     'kirillov.ivankirillov1993@yandex.ru',
        #     #email_list,
        #     recipients,
        #     fail_silently=False,
        # )
        # Mailing_attempt.objects.create(
        #     status=Mailing_attempt.SUCCESSFUL,
        #     mail_server_response="Письмо успешно отправлено",
        #     message=self.object,
        # )
        # return redirect('mailing:mailing_list')

class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ['date_and_time_of_sending_end', 'status', 'message', 'recipients']
    success_url = reverse_lazy('mailing:mailing_list')

class MailingDeleteView(DeleteView):
    model = Mailing
    #template_name = 'Mailing_confirm_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')
