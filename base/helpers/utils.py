import random
import base64
from django.db import connection
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from celery import shared_task
from celery.utils.log import get_task_logger
from base.pdf_render import Render
logger = get_task_logger(__name__)


def identifier_builder(table_name: str, prefix: str = None) -> str:
    with connection.cursor() as cur:
        query = f'SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1;'
        cur.execute(query)
        row = cur.fetchone()
    try:
        seq_id = str(row[0] + 1)
    except:
        seq_id = "1"
    random_suffix = random.randint(10, 99)
    if not prefix:
        return seq_id.rjust(8, '0') + str(random_suffix)
    return prefix + seq_id.rjust(8, '0') + str(random_suffix)



def send_mail_pdf(subject=None, to=None, text_content=None, pdf_content=None):
    from_email = settings.FROM_EMAIL
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to,])
    if pdf_content:
        msg.attach_alternative(pdf_content, "application/pdf")
    msg.send(fail_silently=True)
