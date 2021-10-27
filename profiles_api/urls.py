from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')
                #(name of the url, the viewset we want to register to the url, base name for the viewset
router.register('profile',views.UserProfileViewSet)



urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
    # - '' - for the prefix of the url
    # - include(router.urls) - it generates a list for the urls that are associated with the viewset
]
