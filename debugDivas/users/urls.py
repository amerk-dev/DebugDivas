from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SportTypeViewSet, LocationViewSet, RegisterView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sport-types', SportTypeViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='api-register'),
    path('auth/', include('dj_rest_auth.urls')),
]
