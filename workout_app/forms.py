from xml.parsers.expat import model
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# サインアップのフォーム(貴重になりそうな個人情報は取らない、メールアドレス認証はしない仕様)
class SignUpForm(UserCreationForm):
    # date_of_birth = forms.DateField(label="誕生日", widget=forms.SelectDateWidget(years=[x for x in range(1970, 2030)]))
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "heights", "weights")
