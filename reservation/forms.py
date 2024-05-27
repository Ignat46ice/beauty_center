from django import forms

from reservation.models import *


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a service'}),
            "duration": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the duration'}),
            "price": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the price'}),

        }

    def clean(self):
        clean_data = super().clean()
        print(clean_data)

        get_name = clean_data.get("name")
        check_name = Service.objects.filter(name=get_name)

        if check_name:
            msg = "This service already exist"
            self._errors["name"] = self.error_class([msg])


class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ("name", "duration", "price")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a service'}),
            "duration": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the duration'}),
            "price": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the price'}),


        }


class StylistForm(forms.ModelForm):
    class Meta:
        model = Stylist
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a email'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter a description', 'rows': 3}),
            "services": forms.CheckboxSelectMultiple(),
        }

    def clean(self):
        clean_data = super().clean()
        print(clean_data)

        get_email = clean_data.get("email")
        check_email = Stylist.objects.filter(email=get_email)
        if check_email:
            msg = "The email was already registered. Please enter a new email"
            self._errors["email"] = self.error_class([msg])

        get_description = clean_data.get("description")
        if len(get_description) <= 5:
            msg = "Please write a more detailed description"
            self._errors["description"] = self.error_class([msg])

        return clean_data


class StylistUpdateForm(forms.ModelForm):
    class Meta:
        model = Stylist
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a email'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter a description', 'rows': 3}),
            "services": forms.CheckboxSelectMultiple(),
        }
