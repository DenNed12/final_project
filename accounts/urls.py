from django.urls import path
from .views import SignUp, ConfirmUser

urlpatterns = [
    #path('', ),
    path('signup/', SignUp.as_view(), name='signup'),
    path('confirm-email/', ConfirmUser.as_view(), name ='confirm_user')
    #path('profile/')

]