from django.urls import path
from . import views
from mailing.views import MailingCreateView, MailingUpdateView, MailingDeleteView, MailingListView, MailingDetailView
from mailing.views import Mailing_recipientCreateView, Mailing_recipientUpdateView, Mailing_recipientDeleteView, Mailing_recipientListView, Mailing_recipientDetailView
from mailing.views import MessageCreateView, MessageUpdateView, MessageDeleteView, MessageListView, MessageDetailView

app_name = 'mailing'

urlpatterns = [
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/new/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    path('mailing_recipient/', Mailing_recipientListView.as_view(), name='mailing_recipient_list'),
    path('mailing_recipient/<int:pk>/', Mailing_recipientDetailView.as_view(), name='mailing_recipient_detail'),
    path('mailing_recipient/new/', Mailing_recipientCreateView.as_view(), name='mailing_recipient_create'),
    path('mailing_recipient/<int:pk>/edit/', Mailing_recipientUpdateView.as_view(), name='mailing_recipient_edit'),
    path('mailing_recipient/<int:pk>/delete/', Mailing_recipientDeleteView.as_view(), name='mailing_recipient_delete'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/new/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_edit'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]