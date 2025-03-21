from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing_recipient, Message, Mailing, Mailing_attempt


class Mailing_recipientCreateView(LoginRequiredMixin, CreateView):
    model = Mailing_recipient
    fields = ['email', 'full_name', 'comment']
    #template_name = 'Mailing_recipient_form.html'
    success_url = reverse_lazy('mailing:mailing_recipient_list')

    def dispatch(self, request, *args, **kwargs):
        # Проверка прав доступа
        if not (request.user.is_superuser or request.user.groups.filter(name='Пользователи').exists()):
            raise PermissionDenied("У вас нет прав для редактирования публикации.")
        return super().dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        # Проверка прав доступа
        if not (request.user.is_superuser or request.user.groups.filter(name='Пользователи').exists()):
            raise PermissionDenied("У вас нет прав для редактирования получателей.")
        return super().dispatch(request, *args, **kwargs)


class Mailing_recipientDeleteView(DeleteView):
    model = Mailing_recipient
    #template_name = 'Mailing_recipient_confirm_delete.html'
    success_url = reverse_lazy('mailing:mailing_recipient_list')

    def dispatch(self, request, *args, **kwargs):
        # Проверка прав доступа
        if not (request.user.is_superuser or request.user.groups.filter(name='Пользователи').exists()):
            raise PermissionDenied("У вас нет прав для редактирования публикации.")
        return super().dispatch(request, *args, **kwargs)


    
    
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['subject_letter', 'body_letter']
    #template_name = 'Message_form.html'
    success_url = reverse_lazy('mailing:message_list')

    def dispatch(self, request, *args, **kwargs):
        # Проверка прав доступа
        if not (request.user.is_superuser or request.user.groups.filter(name='Пользователи').exists()):
            raise PermissionDenied("У вас нет прав для редактирования публикации.")
        return super().dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        # Проверка прав доступа
        if not (request.user.is_superuser or request.user.groups.filter(name='Пользователи').exists()):
            raise PermissionDenied("У вас нет прав для редактирования публикации.")
        return super().dispatch(request, *args, **kwargs)



class MessageDeleteView(DeleteView):
    model = Message
    #template_name = 'Message_confirm_delete.html'
    success_url = reverse_lazy('mailing:message_list')

    def dispatch(self, request, *args, **kwargs):
        # Проверка прав доступа
        if not (request.user.is_superuser or request.user.groups.filter(name='Пользователи').exists()):
            raise PermissionDenied("У вас нет прав для редактирования публикации.")
        return super().dispatch(request, *args, **kwargs)


    
class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    fields = ['date_and_time_of_sending_end', 'status', 'message', 'recipients']
    #template_name = 'Mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def dispatch(self, request, *args, **kwargs):
        # Проверка прав доступа
        if not (request.user.is_superuser or request.user.groups.filter(name='Пользователи').exists()):
            raise PermissionDenied("У вас нет прав для редактирования публикации.")
        return super().dispatch(request, *args, **kwargs)

@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    #template_name = 'Mailing_list.html'
    context_object_name = 'mailing'




    def get_queryset(self):
        """
        Фильтруем данные в зависимости от группы пользователя.
        """
        if self.request.user.is_superuser or self.request.user.groups.filter(name="Менеджеры").exists():
            # Суперпользователь и менеджеры видят все рассылки
            return Mailing.objects.all()
        elif self.request.user.groups.filter(name="Пользователи").exists():
            # Пользователи видят только свои рассылки
            return Mailing.objects.filter(user=self.request.user)
        else:
            # Если пользователь не входит ни в одну из групп, запрещаем доступ
            raise PermissionDenied("У вас нет прав для просмотра этого списка.")

    def get_context_data(self, **kwargs):
        """
        Добавляем статистику в контекст.
        """
        context = super().get_context_data(**kwargs)

        if self.request.user.is_superuser or self.request.user.groups.filter(name="Менеджеры").exists():# Статистика по рассылкам
            context['total_mailings'] = Mailing.objects.count()
            context['active_mailings'] = Mailing.objects.filter(status='Запущена').count()
            context['unique_recipients'] = Mailing_recipient.objects.distinct().count()

            # Статистика по попыткам
            successful_attempts = Mailing_attempt.objects.filter(status=Mailing_attempt.SUCCESSFUL).count()
            failed_attempts = Mailing_attempt.objects.filter(status=Mailing_attempt.NOT_SUCCESSFUL).count()
            total_attempts = Mailing_attempt.objects.count()

        elif self.request.user.groups.filter(name="Пользователи").exists():
            context['total_mailings'] = Mailing.objects.filter(user=self.request.user).count()
            context['active_mailings'] = Mailing.objects.filter(status='Запущена',user=self.request.user).count()
            context['unique_recipients'] = Mailing_recipient.objects.distinct().count()

            # Статистика по попыткам
            successful_attempts = Mailing_attempt.objects.filter(status=Mailing_attempt.SUCCESSFUL).count()
            failed_attempts = Mailing_attempt.objects.filter(status=Mailing_attempt.NOT_SUCCESSFUL).count()
            total_attempts = Mailing_attempt.objects.count()

        context.update({
            'successful_attempts': successful_attempts,
            'failed_attempts': failed_attempts,
            'total_attempts': total_attempts,
        })

        return context

@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingDetailView(DetailView):
    model = Mailing
    context_object_name = 'mailing'


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        subject_letter = request.POST.get("subject_letter")
        body_letter = request.POST.get("body_letter")
        recipients = [recipient.email for recipient in self.object.recipients.all()]
        for recipient in recipients:
            try:
                send_mail(
                    subject_letter,
                    body_letter,
                    EMAIL_HOST_USER,
                    [recipient],
                    fail_silently=False,
                )
                Mailing_attempt.objects.create(
                    status=Mailing_attempt.SUCCESSFUL,
                    mail_server_response="Письмо успешно отправлено",
                    message=self.object,
                )
            except Exception as e:
                Mailing_attempt.objects.create(
                    status=Mailing_attempt.NOT_SUCCESSFUL,
                    mail_server_response=str(e),
                    message=self.object,
                )
        messages.success(request, "Рассылка завершена. Проверьте попытки отправки.")
        return redirect('mailing:mailing_list')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ['date_and_time_of_sending_end', 'status', 'message', 'recipients']
    success_url = reverse_lazy('mailing:mailing_list')

    def dispatch(self, request, *args, **kwargs):
        # Проверка прав доступа
        if not (request.user.is_superuser or request.user.groups.filter(name='Пользователи').exists()):
            raise PermissionDenied("У вас нет прав для редактирования публикации.")
        return super().dispatch(request, *args, **kwargs)


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')

    def dispatch(self, request, *args, **kwargs):
        # Проверка прав доступа
        if not (request.user.is_superuser or request.user.groups.filter(name='Пользователи').exists()):
            raise PermissionDenied("У вас нет прав для редактирования публикации.")
        return super().dispatch(request, *args, **kwargs)


def block_mailing(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    mailing.is_active = {mailing.is_active: False, not mailing.is_active: True}[True]
    mailing.save()
    return redirect(reverse("mailing:mailing_list"))