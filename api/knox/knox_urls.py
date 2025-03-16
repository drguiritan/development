from django.urls import path
from knox.views import LogoutAllView
from .knox_views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
    path('logout-all/', LogoutAllView.as_view(), name='knox_logout_all'),  # Logs out all sessions
]
