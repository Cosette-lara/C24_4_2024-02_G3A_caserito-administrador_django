from rest_framework.routers import DefaultRouter
from api_Caserito import views

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuario')
router.register(r'restaurantes', views.RestauranteViewSet, basename='restaurante')
router.register(r'calificaciones', views.CalificacionViewSet, basename='calificacion')
router.register(r'comentarios', views.ComentarioViewSet, basename='comentario')
router.register(r'detalles', views.DetalleViewSet, basename='detalle')
router.register(r'favoritos', views.FavoritoViewSet, basename='favorito')
router.register(r'roles', views.RolViewSet, basename='rol')
router.register(r'usuario_roles', views.UsuarioRolViewSet, basename='usuario_rol')

urlpatterns = router.urls
