from django.contrib import admin
from django.urls import path
from tracker import views  # import all views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # home page
    path('', views.calc, name='calc'),  # calculators page
]