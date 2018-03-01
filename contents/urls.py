from django.conf.urls import url,include
from django.contrib import admin
from contents import views
from rest_framework import routers
# from .views import userProfileView,FileView

#router = routers.SimpleRouter()
#router.register(r'upload',views.userProfileViewSet)
# router.register(r'image', views.ExampleModelViewSet)
urlpatterns = [
    url(r'^adminaccounts/$',views.adminAccount),
    url(r'^patients',views.userProfileView().as_view()),
    #url(r'^upload',views.userProfileViewSet())
    #url(r'^',include(router.urls)),
]
