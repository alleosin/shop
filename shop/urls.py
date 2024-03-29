from django.urls import path

from shop import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path(r'^(?P<category_slug>[-\w]+)/$',
         views.product_list,
         name="product_list_by_category"),
    path(r"^(?P<id>\d+)/(?P<slug>[-\w]+)/$",
         views.product_detail,
         name="product_detail"),
]