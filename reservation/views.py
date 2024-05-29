
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView

from reservation.models import Service, Stylist, Reservation
from reservation.models import Service, AboutUs, Contact, Review

from reservation.forms import ServiceForm, ServiceUpdateForm, ReservationUpdateForm, ReservationForm

from reservation.forms import StylistForm, StylistUpdateForm
from reservation.forms import ServiceForm, ServiceUpdateForm, ReviewForm, ReviewUpdateForm


class ServiceCreateView(CreateView):
    template_name = 'service/create_service.html'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services_list')

    def form_valid(self, form):
        if form.is_valid():
            new_service = form.save(commit=False)
            new_service.name = new_service.name.title()
            new_service.save()
        return redirect('services_list')


class ServicesListView(ListView):
    template_name = 'service/services_list.html'
    model = Service
    context_object_name = 'all_services'


class ServiceUpdateView(UpdateView):
    template_name = "service/update_service.html"
    model = Service
    form_class = ServiceUpdateForm
    success_url = reverse_lazy('services_list')


class ServiceDeleteView(DeleteView):
    template_name = "service/delete_service.html"
    model = Service
    success_url = reverse_lazy('services_list')


class AboutUsTemplateView(TemplateView):
    template_name = 'about/about_us.html'
    model = AboutUs
    success_url = reverse_lazy('about_us')


class ContactTemplateView(TemplateView):
    template_name = 'contact/contact_us.html'
    model = Contact
    success_url = reverse_lazy('contact')

class StylistCreateView(CreateView):
    template_name = 'stylist/create_stylist.html'
    model = Stylist
    form_class = StylistForm
    success_url = reverse_lazy('stylist_list')


class StylistListView(ListView):
    template_name = 'stylist/stylist_list.html'
    model = Stylist
    context_object_name = 'all_stylists'


class StylistUpdateView(UpdateView):
    template_name = "stylist/update_stylist.html"
    model = Stylist
    form_class = StylistUpdateForm
    success_url = reverse_lazy('stylist_list')


class StylistDeleteView(DeleteView):
    template_name = "stylist/delete_stylist.html"
    model = Stylist
    success_url = reverse_lazy('stylist_list')

class ReviewCreateView(CreateView):
    template_name = 'review/create_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews_list')

class ReservationCreateView(CreateView):
    template_name = "reservation/create_reservation.html"
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservation_list')

class ReviewListView(ListView):
    template_name = 'review/review_list.html'
    model = Review
    context_object_name = 'reviews_list'

class ReservationListView(ListView):
    template_name = 'reservation/reservation_list.html'
    model = Reservation
    context_object_name = 'all_reservations'


class ReservationUpdateView(UpdateView):
    template_name = "reservation/update_reservation.html"
    model = Reservation
    form_class = ReservationUpdateForm
    success_url = reverse_lazy('reservation_list')


class ReservationDeleteView(DeleteView):
    template_name = "reservation/delete_reservation.html"
    model = Reservation
    success_url = reverse_lazy('reservation_list')

class ReviewUpdateView(UpdateView):
    template_name = 'review/update_review.html'
    model = Review
    form_class = ReviewUpdateForm
    success_url = reverse_lazy('reviews_list')
