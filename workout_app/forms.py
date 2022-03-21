from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# サインアップのフォーム(貴重になりそうな個人情報は取らない仕様)
class SignUpForm(UserCreationForm):

    date_of_birth = forms.DateField(label="誕生日", widget=forms.SelectDateWidget(years=[x for x in range(1970, 2030)]))

    class Meta:
        model = User
        fields = ("username","password1","password2","date_of_birth","heights","weights")

    def save(self, commit=True):
        # commit=Falseだと、DBに保存されない
        # デフォルトのabstractUserにないフィールドのみここに記載
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.date_of_birth = self.cleaned_data["date_of_birth"]
        user.heights = self.cleaned_data["heights"]
        user.weights = self.cleaned_data["weights"]
        

        user.is_active = False

        if commit:
            user.save()

        return user
