from django.urls import path
from .views import SignUp

urlpatterns = [
    #path('', ),
    path('signup/', SignUp.as_view(), name='signup'),

]