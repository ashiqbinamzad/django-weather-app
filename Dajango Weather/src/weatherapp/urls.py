from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_veiw, name="home")
]
