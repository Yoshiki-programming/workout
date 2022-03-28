from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from .forms import SignUpForm, WorkoutDetailForm, WorkoutForm, WorkoutDetailFormSet
from django.urls import reverse_lazy
from rest_framework import generics
from .models import WorkoutDetail
from .serializers import WorkoutDetailSerializer
from django.shortcuts import redirect
User = get_user_model()
# Create your views here.


class FormsetMixin(object):
    object = None

    def get(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formset_class(self):
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.object.get_absolute_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))



class MyPageView(generics.ListAPIView):
    template_name = 'mypage.html'
    serializer_class = WorkoutDetailSerializer
    # queryset = WorkoutDetail.objects.all()
    def get_queryset(self):
        self.user = self.request.user
        return WorkoutDetail.objects.filter(workout__user=self.user)

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('workout_app:mypage')
    template_name = 'registration/signup.html'

class WorkoutCreateView(CreateView):
    form_class = WorkoutDetailForm
    template_name = 'workout_create.html'
    formset_class = WorkoutDetailFormSet

    def get_context_data(self, **kwargs):
        ctx = super(WorkoutCreateView, self).get_context_data(**kwargs)
        if self.request.method == "POST":
            ctx["formset"] = WorkoutDetailFormSet(self.request.POST, self.request.FILES)
        else:
            ctx["formset"] = WorkoutDetailFormSet()
        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        formset = ctx["formset"]
        if formset.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()

            # FormSet の内容を保存
            formset.instance = self.object
            formset.save()

            return redirect(self.get_redirect_url())
        else:
            ctx["form"] = form
            return self.render_to_response(ctx)

