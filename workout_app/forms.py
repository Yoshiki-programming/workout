from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.forms.models import inlineformset_factory
from django.forms.widgets import Select

from workout_app.models import Workout, WorkoutDetail
User = get_user_model()

# サインアップのフォーム(貴重になりそうな個人情報は取らない、メールアドレス認証はしない仕様)
class SignUpForm(UserCreationForm):
    # date_of_birth = forms.DateField(label="誕生日", widget=forms.SelectDateWidget(years=[x for x in range(1970, 2030)]))
    success_url = reverse_lazy('login') 
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "heights", "weights")

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password1')
    #     user = authenticate(username=username, password=password)
    #     login(self.request, user)
    #     return response

class WorkoutForm(forms.ModelForm):
    success_url = reverse_lazy('workout_app:logined') 
    class Meta:
        model = Workout
        fields = ("part_of_body", "workout", "memo")

class WorkoutDetailForm(forms.ModelForm):
    success_url = reverse_lazy('workout_app:logined') 
    class Meta:
        model = WorkoutDetail
        fields = ("workout","weight", "reps", "date", "memo")

    def __init__(self, *args, **kwargs):
        super(WorkoutDetailForm, self).__init__(*args, **kwargs)

        self.fields['workout'].choices = lambda: [('', '-- 商品 --')] + [
            (item.id, '円') for item in Workout.objects.order_by('user')
            ]

        choices_number = [('', '-- 個数 --')] + [(str(i), str(i)) for i in range(1, 10)]
        self.fields['reps'].widget = Select(choices=choices_number)

WorkoutDetailFormSet = inlineformset_factory(
    parent_model=Workout,
    model=WorkoutDetail,
    form=WorkoutDetailForm,
    extra=1,
    min_num=1,
    validate_min=True,
)
