from django.shortcuts import render,redirect
from models import User
from django.views.generic.edit import CreateView,UpdateView
from .forms import CustomSignupForm


class SignUp(CreateView):
    model = User
    form_class = CustomSignupForm
    success_url = '/accounts/confirm-email'
    template_name = 'registration/signup.html'



class ConfirmUser(UpdateView):
    model =  User
    context_object_name = 'confirm_user'
    template_name = 'registration/account_inactive.html'
    def post(self,request, *args, **kwargs):
        if 'code' in request.post:
            user = User.objects.filter(code = request.POST('code'))
            if user.exists():
                user.update(is_active = True)
                user.update(code = None)

            else:
                return  render(self.request, template_name='wrong_code.html')
            return redirect('accounts/login')

