from django.contrib import admin
from django.urls import path
import App.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', App.views.home, name="home"),
]
