from django.urls import include, path
from rest_framework import routers

from api.views import TimecardViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('timecards', TimecardViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
