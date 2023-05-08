from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_activation_code(email, activation_code):
    activation_url = f'http://127.0.0.1:8000/v1/api/account/activate/{activation_code}'
    message = f"""
    Thank you for signing {activation_url}
    """
    send_mail(
        'Activate your account',
        message,
        'test@test.com',
        [email, ],
        fail_silently=False
    )