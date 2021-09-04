from django import forms
from django.contrib.auth.models import User
from .models import *

from category.models import Category
from datetime import date


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
	class Meta:
		model = ProfilePersonal
		fields = ['account_type','title', 'gender','first_name', 'last_name', 
        'phone_number','country', 'region','city','date_of_birth', 'address_1', 'address_2', 'level_of_education', 'profile_pic']
		
		widgets = {
			'date_of_birth': DateSelectorWidget(attrs = {
				'class': 'form-control'
			})
		}
            # "account_type": forms.CharField(attrs= { 
			# 	'name' : 'account_type',
			# 	'class': 'form-control',
			# 	'id': 'floatingInput',
			# 	'required' : True
			# }), 
        #     "title": forms.CharField(attrs= { 
		# 		'name' : 'title',
		# 		'class': 'form-control',
		# 		'id': 'floatingInput',
		# 		'required' : True
		# 	}), 
        #     "gender": forms.CharField(attrs= { 
		# 		'name' : 'account_type',
		# 		'class': 'form-control',
		# 		'id': 'floatingInput',
		# 		'required' : True
		# 	}),      
        #     "level_of_education": forms.CharField(attrs= { 
		# 		'name' : 'level_of_education',
		# 		'class': 'form-control',
		# 		'id': 'floatingInput',
		# 		'required' : True
		# 	}),    
        #     "first_name": forms.TextInput(attrs= { 
		# 		'name' : 'firstName',
		# 		'class': 'form-control',
		# 		'id': 'floatingInput',
		# 		'required' : True
		# 	}),
		# 	"last_name": forms.TextInput(attrs= { 
		# 		'name' : 'LastName',
		# 		'class': 'form-control',
		# 		'id': 'floatingInput',
		# 		'required': True
		# 	}),
        #     "quater": forms.TextInput(attrs= { 
		# 		'name' : 'quater',
		# 		'class': 'form-control',
		# 		'id': 'floatingInput',
		# 		'required': True
		# 	}),
		# 	"email": forms.EmailInput(attrs= { 
		# 		'name' : 'email',
		# 		'class': 'form-control',
		# 		'id': 'email',
		# 		'required' : True
		# 	}),
		# 	"phone_number": forms.NumberInput(attrs= { 
		# 		'name' : 'phoneNumber',
		# 		'class': 'form-control',
		# 		'id': 'floatingInput',
		# 		'required' : True
		# 	}),
		# 	"date_of_birth": forms.DateField(attrs= { 
		# 		'name' : 'date_of_birth',
		# 		'class': 'form-control',
		# 		'id': 'floatingInput',
		# 		'required' : True
		# 	}),

		# 	"profile_pic": forms.ImageField(attrs= { 
		# 		'name' : 'profile_pic',
		# 		'class': 'form-control',
		# 		'id': 'floatingInput',
		# 		'required' : True
		# 	}),
        #      "country": forms.CharField(attrs= { 
		# 		'name' : 'country',
		# 		'class': 'form-control select-picker',
		# 		'required' : True
		# 	}), 
        #     "region": forms.CharField(attrs= { 
		# 		'name' : 'region',
		# 		'class': 'form-control select-picker',
		# 		'required' : True
		# 	}), 
        #     "division": forms.CharField(attrs= { 
		# 		'name' : 'division',
		# 		'class': 'form-control select-picker',
		# 		'required' : True
		# 	}), 
        #     "city": forms.CharField(attrs= { 
		# 		'name' : 'city',
		# 		'class': 'form-control select-picker',
		# 		'required' : True
		# 	}),       

		# }

class  ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields = ['language', 'bio', 'experience']
        widgets = { 
            "bio": forms.Textarea(attrs= { 
				'name' : 'bio',
				'class': 'form-control',
                'rows': 8,
                'columns': 8,
				'required' : True
			}), 
            "experience": forms.Textarea(attrs= { 
				'name' : 'experience',
				'class': 'form-control',
                'rows': 8,
                'columns': 8,
				'required' : True
			}), 
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    # widgets = {
	# 		"username": forms.TextInput(attrs= { 
	# 			'name' : 'username',
	# 			'class': 'form-control',
	# 			'id' : "floatingInput",
	# 			'required' : True,
    #             'placeholder':"name@example.com"
	# 		}),
			# "password": forms.PasswordInput(attrs= { 
			# 	'name' : 'password',
			# 	'class': 'form-control',
			# 	'id': 'floatingPassword',
            #     'placeholder':"name@example.com"
			# 	'required': True,
			# }),


class AddSubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = ('category','subcategory','subject','level','charge', 'amount')

class AddExperienceForm(forms.ModelForm):
	class Meta:
		model = Experience
		fields = ('work_post','position','start_date','end_date')

class AddQualificationForm(forms.ModelForm):
	class Meta:
		model = Qualification
		fields = ('school','certificate','start_year','end_year')

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
		fields = ('facebook','instagram','linkedin', 'website', 'youtube')