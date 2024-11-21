from rest_framework.routers import DefaultRouter
from .views import userViewSet
from django.urls import path, include
from .views import ClientViewSet
from .views import ProjectViewSet

router = DefaultRouter()
router.register('user', userViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'Project', ProjectViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
]
