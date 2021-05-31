
from django.conf import settings
from django.conf.urls.static import static
from leads.views import SignupView, landing_page, LandingPageView
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetCompleteView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LandingPageView.as_view() , name="landing-page"),
    path("leads/", include("leads.urls", namespace="leads")),
    path("agents/", include("agents.urls", namespace="agents")),
    path("signup/", SignupView.as_view(), name="signup"),
    path("reset-password/", PasswordResetView.as_view() , name="reset-password"),
    path("password-reset-done/", PasswordResetDoneView.as_view() , name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(),name="password_reset_confirm" ),
    path("reset-password-complete/", PasswordResetCompleteView.as_view() , name="password_reset_complete"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
