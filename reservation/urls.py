from django.urls import path

from reservation import views

urlpatterns = [
    path('create-service/', views.ServiceCreateView.as_view(), name='create_service'),
    path('services-list/', views.ServicesListView.as_view(), name='services_list'),
    path('update-service/<int:pk>/', views.ServiceUpdateView.as_view(), name='update_service'),
    path('delete-service/<int:pk>/', views.ServiceDeleteView.as_view(), name='delete_service'),

]
