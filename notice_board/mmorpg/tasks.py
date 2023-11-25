from celery import shared_task
from django.core.mail import send_mail

from .models import Response
@shared_task()
def notification_send(response_id):
    response = Response.objects.get(pk=response_id)
    notice = response.notice
    author = notice.author

    subject = 'У вас новый отклик на ваше объявление'
    message = ('Здравствуйте {0},\n\nНа ваше объявление "{1}" поступил новый отклик. Проверьте свою страницу,'
               ' чтобы увидеть подробности.\n\nС уважением,\nКоманда сайта').format(author.name, notice.title)
    from_email = 'Nikto51@yandex.ru'
    recipient_list = [author.name.email]

    send_mail(subject, message, from_email, recipient_list)

