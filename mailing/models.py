from django.db import models

from users.models import CustomUser

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
    CREATED = 'Создана'
    LAUNCHED = 'Запущена'
    COMPLETED = 'Завершена'
    STATUS_MAILING = [
        (CREATED, 'Создана'),
        (LAUNCHED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    date_and_time_of_first_sending = models.DateTimeField(auto_now_add=True,
                                                          verbose_name="дата и время первой отправки")
    date_and_time_of_sending_end = models.DateTimeField(verbose_name="дата и время окончания отправки")
    status = models.CharField(max_length=100, choices=STATUS_MAILING, default=CREATED, verbose_name="статус")
    message = models.ForeignKey(
        'Message',
        on_delete=models.SET_NULL,
        related_name="mailing",
        verbose_name="сообщение",
        **NULLBLE
    )
    recipients = models.ManyToManyField('Mailing_recipient', verbose_name="получатель", related_name='mailings',
                                        **NULLBLE)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        related_name="mailings",
        verbose_name="создатель",
        **NULLBLE
    )

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
        ordering = ["status", "date_and_time_of_first_sending", "date_and_time_of_sending_end"]  # Сортировка
        db_table = 'Mailing'  # Название таблици

class Mailing_attempt(models.Model):
    SUCCESSFUL = 'Успешно'
    NOT_SUCCESSFUL = 'Не успешно'

    STATUS_MAILING = [
        (SUCCESSFUL, 'Успешно'),
        (NOT_SUCCESSFUL, 'Не успешно'),
    ]
    date_and_time_of_sending = models.DateTimeField(auto_now_add=True, verbose_name="дата и время отправки")
    status = models.CharField(max_length=100, choices=STATUS_MAILING, default=NOT_SUCCESSFUL, verbose_name="статус")
    mail_server_response = models.TextField(verbose_name="ответ почтового сервера", **NULLBLE)
    message = models.ForeignKey('Mailing', on_delete=models.SET_NULL, related_name="mailing_attempt", verbose_name="рассылка",**NULLBLE)

    class Meta:
        verbose_name = "попытка_рассылки"
        verbose_name_plural = "попытки_рассылки"
        ordering = ["status", "date_and_time_of_sending"]  # Сортировка
        db_table = 'Mailing_attempt'
        permissions = [
            ("can_disable_mailing", "Возможность отключения рассылки"),
        ]

    def __str__(self):
        return f"Попытка рассылки {self.id} - {self.status}"