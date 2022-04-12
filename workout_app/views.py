from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignUpForm, UserUpdateForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url
User = get_user_model()
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('workout_app:login')
    template_name = 'registration/signup.html'

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin, DetailView):
    model = User
    template_name = 'user_detail.html'

class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_update_form.html'
    def get_success_url(self):
        return resolve_url('workout_app:user_detail', pk=self.kwargs['pk'])
    