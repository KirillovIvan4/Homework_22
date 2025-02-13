from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from mailing.models import Mailing_recipient, Message, Mailing

class Mailing_recipientCreateView(LoginRequiredMixin, CreateView):
    model = Mailing_recipient
    fields = ['email', 'full_name', 'comment']
    #template_name = 'Mailing_recipient_form.html'
    success_url = reverse_lazy('mailing:mailing_recipient_list')

class Mailing_recipientListView(ListView):
    model = Mailing_recipient
    #template_name = 'Mailing_recipient_list.html'
    context_object_name = 'mailing_recipient'

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

class MessageListView(ListView):
    model = Message
    #template_name = 'Message_list.html'
    context_object_name = 'message'

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

class MailingListView(ListView):
    model = Mailing
    #template_name = 'Mailing_list.html'
    context_object_name = 'mailing'

    def get_queryset(self):
        return Mailing.objects.filter(status='launched')

class MailingDetailView(DetailView):
    model = Mailing
    #template_name = 'Mailing_detail.html'
    context_object_name = 'mailing'

class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ['date_and_time_of_sending_end', 'status', 'message', 'recipients']
    success_url = reverse_lazy('mailing:mailing_list')

class MailingDeleteView(DeleteView):
    model = Mailing
    #template_name = 'Mailing_confirm_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')
