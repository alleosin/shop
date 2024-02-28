from django.urls import path

from coupons import views

urlpatterns = [
    path("apply/", views.coupon_apply, name="apply"),
]