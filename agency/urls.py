from django.urls import path

from agency.views import (
    index,
)


urlpatterns = [
    path("", index, name="index"),

]
