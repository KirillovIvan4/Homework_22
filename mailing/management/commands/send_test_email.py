from django.core.management.base import BaseCommand
from django.core.mail import send_mail

from mailing.models import Message, Mailing, Mailing_recipient, Mailing_attempt


class Command(BaseCommand):
    help = 'Отправляет письмо'
    #  получаю список с id рассылок
    id_mailings = Mailing.objects.values_list('id', flat=True)
    #  итерируемся по списку и выводим данные о рассылках для дальнейшего выбора той рассылки которую надо отправить
    for id_mailing in id_mailings:
        mailing = Mailing.objects.get(id=id_mailing)
        print("id рассылки -", mailing.id)
        print("Тема письма -", mailing.message.subject_letter, "\n")
        print("Тело письма -",mailing.message.body_letter[:9],"..." , "\n")


    mailing_id = input("Введите id рассылки которую хотите отправить ")

    def handle(self, *args, **kwargs):
        email_list = []
        empty_list = []
        mailing_id = self.mailing_id
        try:
            mailing = Mailing.objects.get(pk=mailing_id)
            subject_letter = mailing.message.subject_letter
            body_letter = mailing.message.body_letter
            # Получаем всех получателей для этой рассылки
            recipients = mailing.recipients.all()
            print(len(recipients))

            if recipients:
            # заполняем список с почтой получателей
                for recipient in recipients:
                    print("recipient")
                    email_list.append(recipient.email)
            else:
                self.stdout.write(self.style.WARNING('Нет получателей для этой рассылки'))
            send_mail(
                subject_letter,
                body_letter,
                'kirillov.ivankirillov1993@yandex.ru',
                email_list,
                fail_silently=False,
            )
            Mailing_attempt.objects.create(
                status=Mailing_attempt.SUCCESSFUL,
                mail_server_response="Письмо успешно отправлено",
                message=self.object,
            )
            self.stdout.write(self.style.SUCCESS('Письмо отправлено!'))
        except Mailing.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Рассылки с ID {mailing_id} не найдено.'))
