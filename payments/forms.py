from django import forms
from .models import Payment
# creating a form


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payment_method', 'phone_number')

        widgets = {
            "phone_number": forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': "phone",
                'required': True,
                'min': 9,
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 15:
            raise forms.ValidationError('this email is already in use')
        return phone