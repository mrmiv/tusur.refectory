from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from .models import ExtUser

# class UserForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Подтверждение',
        widget=forms.PasswordInput
    )
    lastname = forms.CharField(label='Имя', required=False)
    firstname = forms.CharField(label='Фамилия', required=False)
    middlename = forms.CharField(label='Отчество', required=False)


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль и подтверждение не совпадают')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'lastname',
            'firstname', 
            'middlename',
            )


class UserChangeForm(forms.ModelForm):

    '''
    Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    '''
    # password = ReadOnlyPasswordHashField(
    #     widget=forms.PasswordInput,
    #     required=False
    # )

    # def save(self, commit=True):
    #     user = super(UserChangeForm, self).save(commit=False)
    #     password = self.cleaned_data["password"]
    #     if password:
    #         user.set_password(password)
    #     if commit:
    #         user.save()
    #     return user

    # class Meta:
    #     model = get_user_model()
    #     fields = ['email', ]

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = ExtUser
        fields = ('email', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]




class LoginForm(forms.Form):

    """Форма для входа в систему
    """
    username = forms.CharField(widget=forms.EmailInput, required=True, label='email')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='password')
