import django_filters
from django import forms
from reservation.models import *


class ReviewFilter(django_filters.FilterSet):
    stylist = django_filters.ChoiceFilter(choices=[(stylist.id, stylist) for stylist in Stylist.objects.all()],
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    stars = django_filters.NumberFilter(label='Stars', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the number of stars'}))

    class Meta:
        model = Review
        fields = ['stylist', 'stars']
