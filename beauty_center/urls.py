from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from userextend.forms import AuthenticationNewForm
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("", include("reservation.urls")),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path("", include("django.contrib.auth.urls")),
    path("", include("userextend.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

