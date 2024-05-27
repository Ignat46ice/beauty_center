
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from reservation.models import Service, Stylist

from reservation.forms import ServiceForm, ServiceUpdateForm

from reservation.forms import StylistForm, StylistUpdateForm


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
