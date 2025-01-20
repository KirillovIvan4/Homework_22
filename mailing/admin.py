from django.contrib import admin
from mailing.models import Mailing_recipient, Message, Mailing


@admin.register(Mailing_recipient)
class Mailing_recipientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'full_name',)
    list_filter = ('email', 'full_name',)
    search_fields = ('email', 'full_name',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject_letter',)
    list_filter = ('subject_letter',)
    search_fields = ('subject_letter',)

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'message', 'status',)
    list_filter = ('message', 'status', 'recipients',)
    search_fields = ('message', 'status', 'recipients',)
