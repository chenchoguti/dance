from rest_framework import routers
from dance.viewsets import BailarinaViewSet, TeatroViewSet, NacionalidadViewSet
router = routers.DefaultRouter()
router.register(r'bailarina', BailarinaViewSet)
router.register(r'teatro', TeatroViewSet)
router.register(r'nacionalidad',NacionalidadViewSet)