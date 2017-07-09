from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^plot/$', TemplateView.as_view(template_name="plot.html")),
]
