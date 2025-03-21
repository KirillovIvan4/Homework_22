from django import forms


class MailingForm(forms.Form):
    date_and_time_of_first_sending = models.DateTimeField(auto_now_add=True,
                                                          verbose_name="дата и время первой отправки")
    date_and_time_of_sending_end = models.DateTimeField(verbose_name="дата и время окончания отправки")
    status = models.CharField(max_length=100, choices=STATUS_MAILING, default=CREATED, verbose_name="статус")
