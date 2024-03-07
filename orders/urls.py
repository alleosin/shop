from django.urls import path

from orders import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_("create/"), views.order_create, name="order_create"),
    path(r"^admin/order/(?P<order_id>\d+)/$", views.admin_order_detail, name="admin_order_detail"),
]