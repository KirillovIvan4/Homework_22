from django.contrib import admin
from mailing.models import Mailing_recipient, Message, Mailing, Mailing_attempt


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
    filter_horizontal = ('recipients',)

@admin.register(Mailing_attempt)
class Mailing_attemptgAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'message',)
    list_filter = ('message', 'status',)
    search_fields = ('message', 'status',)

