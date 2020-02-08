from django import forms
from django.contrib.auth.models import User
from main_app.models import StudentUserInfo, LabUserInfo, HODUserInfo, OtherUserInfo, BTPUserInfo

class StudentUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class StudentsInfoForm(forms.ModelForm):
    class Meta():
        model = StudentUserInfo
        fields = ('department','rollnumber',)


class LabUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class LabInfoForm(forms.ModelForm):
    class Meta():
        model = LabUserInfo
        fields = ('department',)


class HODUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class HODInfoForm(forms.ModelForm):
    class Meta():
        model = HODUserInfo
        fields = ('department',)

class BTPUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class BTPInfoForm(forms.ModelForm):
    class Meta():
        model = BTPUserInfo
        fields = ('department',)

class OtherUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class OtherInfoForm(forms.ModelForm):
    class Meta():
        model = OtherUserInfo
        fields = ()