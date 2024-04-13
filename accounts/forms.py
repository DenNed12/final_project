from allauth.account.forms import SignupForm
from django.core.mail import send_mail
import random
from string import hexdigits
from django.conf import settings
from board.models import Author

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm,self).save(request)
        Author.objects.create(authorUser = user)
        code = random.sample(hexdigits, k =5)
        user.code= code
        user.save()
        send_mail(
            subject= "Код подтверждения пользователя",
            message=f'{user.code}',
            from_email= settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user