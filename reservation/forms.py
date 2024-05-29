from django import forms

from reservation.models import Service
from reservation.models import Review


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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        widgets = {
            'stylist': forms.Select(attrs={'class': 'form-select'}),
            'stars': forms.NumberInput(attrs={'class': ""}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter a review', 'rows': 1}),
        }


class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'description']

        widgets = {
            'stars': forms.NumberInput(attrs={'class': ""}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter a review', 'rows': 1}),
        }
