from django.urls import path

from .import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('handle_payment_success/', views.handle_payment_success, name='handle_payment_success'),
]
