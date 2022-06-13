from cProfile import label
from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from category.models import Category
from datetime import date
# from bootstrap_datepicker_plus import DatePickerInput

class DateSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        days = [(day, day) for day in range(1, 32)]
        months = [(month, month) for month in range(1, 13)]
        years = [(year, year) for year in range(1900, 2021)]
        widgets = [
            forms.Select(attrs=attrs, choices=days),
            forms.Select(attrs=attrs, choices=months),
            forms.Select(attrs=attrs, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            year, month, day = value.split('-')
            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}-{}-{}'.format(year, month, day)

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('this email is already in use')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('this username is already in use')
        return username

    def clean_password_confirm(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password_confirm')

        if ((pass1 and pass2) and (pass1 != pass2)):
            forms.ValidationError("Password don't match")
        return pass2

class PersonalProfileForm(forms.ModelForm):
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        empty_label=None,
        required=True,
        to_field_name='id',
        label='Region',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = ProfilePersonal
        fields = ['account_type', 'title', 'gender', 'first_name', 'last_name',
                  'phone_number', 'date_of_birth', 'country', 'region', 'town', 'address', 'level_of_education', 'profile_pic', 'whatsapp_number', 'show_whatsapp_number', 'online_lesson']

        widgets = {
            'date_of_birth': DatePickerInput(),

        }

        labels = {
            'whatsapp_number': 'Whatsapp',
        }
class PersonalProfilePic(forms.ModelForm):
    class Meta:
        model = ProfilePersonal
        fields = ('id', 'profile_pic',)

class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields = ['language', 'bio', 'category',
                  'subcategory', 'subject', 'charge', 'amount']
        widgets = {
            "bio": forms.Textarea(attrs={
                'name': 'bio',
                'placeholder': 'Tell others about yourself',
                'class': 'form-control',
                'rows': 8,
                'cols': 20,
                'required': False
            }),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('category', 'subcategory', 'subject', 'charge', 'amount', )

class AddExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('work_post', 'position', 'description',
                  'start_date', 'end_date', 'current_job')
        widgets = {
            'start_date': DatePickerInput(),
            'end_date': DatePickerInput()

        }

class AddQualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ('school', 'certificate', 'start_year',
                  'end_year', 'still_studying')

class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ('document_type', 'number', 'photo_back', 'photo_front')

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ('day', 'hour')

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = ('facebook', 'instagram', 'linkedin', 'website', 'youtube')

class UpgradeForm(forms.ModelForm):
    class Meta:
        model = Upgrade
        fields = ('payment_method', 'phone_number')

        widgets = {
            "phone_number": forms.TextInput(attrs={
                'class': 'form-control',
                'id': "phone",
                'required': True,
                'value': "237",
                'min': 15,
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 15:
            raise forms.ValidationError('this email is already in use')
        return phone

class AddScheduleForm(forms.ModelForm):
    class Meta:
        model = OnlineLesson
        fields = ('start', 'end', 'mode', 'amount')
        widgets = {
            'start': DateTimePickerInput(
                attrs={
                    'name': 'start'
                }),
            'end': DateTimePickerInput(
                attrs={
                    'name': 'end'
                }
            ),
        }

class ConfirmScheduleForm(forms.ModelForm):
    class Meta:
        model = OnlineLesson
        fields = ('is_confirm',)