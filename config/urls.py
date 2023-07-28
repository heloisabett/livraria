"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from usuario.router import router as usuario_router
from uploader.router import router as uploader_router

from livraria.views import AutorViewSet,CategoriaViewSet, EditoraViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"autores", AutorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"livros", LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/media/", include(uploader_router.urls)),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
