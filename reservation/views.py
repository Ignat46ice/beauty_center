from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView

from reservation.filters import ReviewFilter
from reservation.models import Stylist, Reservation, StylistService
from reservation.models import Service, AboutUs, Contact, Review

from reservation.forms import ReservationForm, StylistServiceForm, StylistServiceUpdateForm

from reservation.forms import StylistForm, StylistUpdateForm
from reservation.forms import ServiceForm, ServiceUpdateForm, ReviewForm, ReviewUpdateForm


class ServiceCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'service/create_service.html'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services_list')
    permission_required = "service.add_service"

    def form_valid(self, form):
        if form.is_valid():
            new_service = form.save(commit=False)
            new_service.name = new_service.name.title()
            new_service.save()
        return redirect('services_list')


class ServicesListView(ListView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'service/services_list.html'
    model = Service
    context_object_name = 'all_services'
    permission_required = "service.view_services_list"


class ServiceUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "service/update_service.html"
    model = Service
    form_class = ServiceUpdateForm
    success_url = reverse_lazy('services_list')
    permission_required = "service.change_service"


class ServiceDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "service/delete_service.html"
    model = Service
    success_url = reverse_lazy('services_list')
    permission_required = "service.delete_service"


class AboutUsTemplateView(TemplateView):
    template_name = 'about/about_us.html'
    model = AboutUs
    success_url = reverse_lazy('about_us')


class ContactTemplateView(TemplateView):
    template_name = 'contact/contact_us.html'
    model = Contact
    success_url = reverse_lazy('contact')


class StylistCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'stylist/create_stylist.html'
    model = Stylist
    form_class = StylistForm
    success_url = reverse_lazy('stylist_service')
    permission_required = "stylist.add_stylist"


class StylistListView(ListView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'stylist/stylist_list.html'
    model = Stylist
    context_object_name = 'all_stylists'
    permission_required = "stylist.view_stylist_list"


class StylistUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "stylist/update_stylist.html"
    model = Stylist
    form_class = StylistUpdateForm
    success_url = reverse_lazy('stylist_list')
    permission_required = "stylist.change_stylist"


class StylistDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "stylist/delete_stylist.html"
    model = Stylist
    success_url = reverse_lazy('stylist_list')
    permission_required = "stylist.delete_stylist"


class ReservationCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "reservation/create_reservation.html"
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservation_list')
    permission_required = "reservation.add_reservation"

    def form_valid(self, form):
        if form.is_valid():
            datetime_from = form.cleaned_data['datetime_from']
            stylist_service = form.cleaned_data['stylist_service']
            duration = stylist_service.service.duration
            datetime_to = datetime_from + duration

            reservations_intersecting = Reservation.objects.filter(
                Q(stylist_service__stylist=stylist_service.stylist) &
                (
                        Q(datetime_from__gte=datetime_from, datetime_from__lte=datetime_to) |
                        Q(datetime_to__gte=datetime_from, datetime_to__lte=datetime_to) |
                        Q(datetime_from__lt=datetime_from, datetime_to__gt=datetime_to)
                )
            ).count()
            if reservations_intersecting > 0:
                raise ValidationError("Your reservation conflicts with another reservation")
            reservation = form.save(commit=False)
            reservation.datetime_to = datetime_to
            reservation.user = self.request.user
            reservation.save()
            return redirect(self.success_url)
        return super(ReservationCreateView, self).form_valid(form)


class ReservationListView(ListView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'reservation/reservation_list.html'
    model = Reservation
    context_object_name = 'all_reservations'
    permission_required = "reservation.view_reservation_list"


class ReservationUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "reservation/update_reservation.html"
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservation_list')
    permission_required = "reservation.change_reservation"


class ReservationDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "reservation/delete_reservation.html"
    model = Reservation
    success_url = reverse_lazy('reservation_list')
    permission_required = "reservation.delete_reservation"


class ReviewCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'review/create_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews_list')
    permission_required = "review.add_view"

    def form_valid(self, form):
        if form.is_valid():
            review = form.save(commit=False)
            review.user = self.request.user
            review.save()
            return redirect(self.success_url)
        return super().form_valid(form)


class ReviewListView(ListView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'review/reviews_list.html'
    model = Review
    context_object_name = 'all_reviews'
    permission_required = "review.view_reviews_list"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        now = datetime.now()
        data['current_time'] = now
        data["review"] = Review.objects.all()
        review = Review.objects.all()
        my_filter = ReviewFilter(self.request.GET, queryset=review)
        data['all_reviews'] = my_filter.qs
        data['filter_form'] = my_filter.form

        return data


class ReviewUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'review/update_review.html'
    model = Review
    form_class = ReviewUpdateForm
    success_url = reverse_lazy('reviews_list')
    permission_required = "review.change_review"


class ReviewDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "review/delete_review.html"
    model = Review
    success_url = reverse_lazy('reviews_list')
    permission_required = "review.delete_review"


class StylistServiceCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "stylist/stylist_service.html"
    model = StylistService
    form_class = StylistServiceForm
    success_url = reverse_lazy('stylist_list')
    context_object_name = 'service_stylist'
    permission_required = "stylist.add_stylist_service"


class StylistServiceListView(ListView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'stylist/stylist_service_list.html'
    model = StylistService
    context_object_name = 'all_stylist_services'
    permission_required = "stylist.view_stylist_service_list"


class StylistServiceUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = 'stylist/update_stylist_service.html'
    model = StylistService
    form_class = StylistServiceUpdateForm
    success_url = reverse_lazy('stylist_service_list')
    permission_required = "stylist.change_stylist_service"


class StylistServiceDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin, ):
    template_name = "stylist/delete_stylist_service.html"
    model = StylistService
    success_url = reverse_lazy('stylist_service_list')
    permission_required = "stylist.delete_stylist_service"
