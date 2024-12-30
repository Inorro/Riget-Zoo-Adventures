from django.urls import path
import core.views as views

urlpatterns = [
    path('',views.index,name="index"),
    path('About',views.about,name="About"),
    path('Hotel',views.hotel,name="Hotel"),
    path('Loyalty',views.loyalty,name="Loyalty"),
    path('Tickets',views.tickets,name="Tickets"),
    path('SignOut',views.SignOut,name="SignOut"),
    path('Ticketpt1',views.ticketpt1,name="Ticketpt1"),
    path('Hotelpt1',views.hotelpt1,name="Hotelpt1"),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
]