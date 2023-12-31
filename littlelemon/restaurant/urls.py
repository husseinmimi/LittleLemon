from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('booking/', views.BookingView.as_view(), name='bookings'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
