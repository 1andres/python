from django.conf.urls.defaults import patterns, url
from django.conf.urls import include
from rest_framework import routers
from celulares.apps.webservices.ws_productos.views import *
router = routers.DefaultRouter()
router.register(r'celular', celular_viewset)
router.register(r'marca', marca_viewset)
router.register(r'color', color_viewset)
router.register(r'conectividad', conectividad_viewset)



urlpatterns = patterns('celulares.apps.webservices.ws_productos.views',
		url(r'^ws/productos/$','ws_productos_view',name = 'ws_productos_url'),
		url(r'^api/', include(router.urls)),
		url(r'^api-auth/', include('rest_framework.urls', namespace= 'rest_framework')),
	)