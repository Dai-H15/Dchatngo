from django.urls import path, include
from main import views as mainViews


urlpatterns = [
    path("", mainViews.index, )
]
