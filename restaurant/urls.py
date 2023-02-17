from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.BookingViewSet.as_view({'get': 'list',
                                                   'post': 'create'})),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]