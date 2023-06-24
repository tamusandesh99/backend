
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReactView.as_view(), name="blah"),
    path('creators/', ReactView.as_view(), name="blah"),
    path('creators/<int:pk>/', ReactDetailView.as_view(), name="creator-id"),
    path('creator/search/', ReactView.as_view(), name='creator-search'),
    path('creators/login/', ReactLoginView.as_view(), name="creator-login"),
]
