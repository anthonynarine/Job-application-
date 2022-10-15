
from django.urls import URLPattern
from django.urls import path
from app.views import hello, job_detail


urlpatterns = [
    path("", hello),
    path("job/1",job_detail),
]