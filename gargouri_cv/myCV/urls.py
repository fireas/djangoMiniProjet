from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.myCV_view, name='home'),
    path('contact', views.comming_soon_view, name='contact'),
    path('tupperware', views.comming_soon_view, name='tupperware'),
    path('contacttest', views.contact_test_view, name='contacttest')
]
urlpatterns += staticfiles_urlpatterns()