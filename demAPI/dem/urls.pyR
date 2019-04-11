
from rest_framework.urlpatterns import format_suffix_patterns
from dem import views
from django.conf.urls import url
from .views import doctorCedulaSearch, doctorNombreSearch


urlpatterns = [
    url(r'^v1/cedula/$', doctorCedulaSearch.as_view()),
    url(r'^v1/nombre/$', doctorNombreSearch.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
