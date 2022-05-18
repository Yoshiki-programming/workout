from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
User = get_user_model()
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('workout_app:top')
    template_name = 'registration/signup.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class MypageView(TemplateView):
    template_name = "index.html"