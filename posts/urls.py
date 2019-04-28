from django.urls import path, include
from posts import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
	path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]
