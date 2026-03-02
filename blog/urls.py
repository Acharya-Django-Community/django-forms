from django.urls import path
from .views import home , post_detail , feedback , thank_you

urlpatterns = [
    path('',home,name='home'),
    path('feedback/',feedback,name='feedback'),
    path('thank-you/',thank_you,name='thank_you'),
    path('<int:pk>/',post_detail,name='post_detail'),



]