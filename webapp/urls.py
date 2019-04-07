from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from webapp.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('', MovieList)
router2 = routers.DefaultRouter()
router2.register('', GenreList)


urlpatterns = [
    path('movie/', include(router.urls)),
    path('genre/', include(router2.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
