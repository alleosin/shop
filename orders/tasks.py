from celery import Celery
from django.core.mail import send_mail

from orders.models import Order

app = Celery("main", broker="pyamqp://guest@localhost//")


@app.task
def order_created(order_id):
    """
    A task to send an email notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                    Your order id is {}.'.format(order.first_name,
                                                 order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
