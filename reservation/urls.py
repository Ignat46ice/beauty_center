from django.urls import path

from reservation import views

urlpatterns = [
    path('create-service/', views.ServiceCreateView.as_view(), name='create_service'),
    path('services-list/', views.ServicesListView.as_view(), name='services_list'),
    path('update-service/<int:pk>/', views.ServiceUpdateView.as_view(), name='update_service'),
    path('delete-service/<int:pk>/', views.ServiceDeleteView.as_view(), name='delete_service'),

    path('about-us/', views.AboutUsTemplateView.as_view(), name='about_us'),

    path('contact_us/', views.ContactTemplateView.as_view(), name='contact_us'),

    path('create-review/', views.ReviewCreateView.as_view(), name='create_review'),
    path('reviews_list/', views.ReviewListView.as_view(), name='reviews_list'),
    path('update-review/', views.ReviewUpdateView.as_view(), name='update_review'),
]