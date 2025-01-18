from django.db import models

# Create your models here.
NULLBLE = {"blank": True, "null": True}

class Mailing_recipient(models.Model):
    email = models.EmailField(unique=True, verbose_name="электронная почта")
    full_name = models.CharField(max_length=100, verbose_name="Ф.И.О.")
    comment = models.TextField(verbose_name="комментарий")

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "получатель рассылки"
        verbose_name_plural = "получатели рассылок"
        ordering = ["email", "full_name"]  # Сортировка
        db_table = 'Mailing_recipient'  # Название таблици


class Message(models.Model):
    subject_letter = models.CharField(max_length=100, verbose_name="тема письма")
    body_letter = models.TextField(verbose_name="тело письма")

    def __str__(self):
        return f"{self.subject_letter}"

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
        ordering = ["subject_letter"]  # Сортировка
        db_table = 'Message'  # Название таблици


class Mailing(models.Model):
    CREATED = 'created'
    LAUNCHED = 'launched'
    COMPLETED = 'completed'
    STATUS_MAILING = [
        (CREATED, 'Создана'),
        (LAUNCHED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    date_and_time_of_first_sending = models.DateTimeField(auto_now_add=True, verbose_name="дата и время первой отправки")
    date_and_time_of_sending_end = models.DateTimeField(verbose_name="дата и время окончания отправки")
    status = models.CharField(max_length=100, choices=STATUS_MAILING, default=CREATED, verbose_name="статус")
    message = models.ForeignKey(
        'Message',
        on_delete=models.SET_NULL,
        related_name="mailing",
        verbose_name="сообщение",
        **NULLBLE
    )
    recipients =  models.ManyToManyField('Mailing_recipient',blank=True, verbose_name="получатель",**NULLBLE)