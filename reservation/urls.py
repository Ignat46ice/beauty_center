from django.urls import path

from reservation import views

urlpatterns = [
    path('create-service/', views.ServiceCreateView.as_view(), name='create_service'),
    path('services-list/', views.ServicesListView.as_view(), name='services_list'),
    path('update-service/<int:pk>/', views.ServiceUpdateView.as_view(), name='update_service'),
    path('delete-service/<int:pk>/', views.ServiceDeleteView.as_view(), name='delete_service'),

    path('create-stylist/', views.StylistCreateView.as_view(), name='create_stylist'),
    path('stylist-list/', views.StylistListView.as_view(), name='stylist_list'),
    path('update-stylist/<int:pk>/', views.StylistUpdateView.as_view(), name='update_stylist'),
    path('delete-stylist/<int:pk>/', views.StylistDeleteView.as_view(), name='delete_stylist'),

    path('create-reservation/', views.ReservationCreateView.as_view(), name='create_reservation'),
    path('reservation-list/', views.ReservationListView.as_view(), name='reservation_list'),
    path('update-reservation/<int:pk>/', views.ReservationUpdateView.as_view(), name='update_reservation'),
    path('delete-reservation/<int:pk>/', views.ReservationDeleteView.as_view(), name='delete_reservation'),



    path('about-us/', views.AboutUsTemplateView.as_view(), name='about_us'),

    path('contact_us/', views.ContactTemplateView.as_view(), name='contact_us'),

    path('create-review/', views.ReviewCreateView.as_view(), name='create_review'),
    path('reviews_list/', views.ReviewListView.as_view(), name='reviews_list'),
    path('update-review/', views.ReviewUpdateView.as_view(), name='update_review'),
]