from django.contrib.auth.views import PasswordChangeView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdateUserForm


class SignUpUserView(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = '/users/login/'


class DisplayUserView(DetailView):
    model = User
    template_name = 'users/display_user.html'


class UpdateUserView(UpdateView):
    form_class = UpdateUserForm
    template_name = 'users/update_user.html'
    success_url = '/'

    def get_object(self):
        return self.request.user


class DeleteUserView(DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = '/'


class PasswordUserChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'users/change_password.html'
    success_url = '/'
