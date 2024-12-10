from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Usuario, Calificacion
from .serializers import UsuarioSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import (
    Usuario,
    Restaurante,
    Calificacion,
    Comentario,
    Detalle,
    Favorito,
    Menu,
    Rol,
    UsuarioRol
)
from .serializers import (
    UsuarioSerializer,
    RestauranteSerializer,
    CalificacionSerializer,
    ComentarioSerializer,
    DetalleSerializer,
    FavoritoSerializer,
    MenuSerializer,
    RolSerializer,
    UsuarioRolSerializer
)

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RestauranteViewSet(ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class CalificacionViewSet(ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class DetalleViewSet(ModelViewSet):
    queryset = Detalle.objects.all()
    serializer_class = DetalleSerializer

class FavoritoViewSet(ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class RolViewSet(ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioRolViewSet(viewsets.ModelViewSet):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Calificacion.objects.filter(fk_usuario=instance.pk_usuario).delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['is_superuser'] = user.is_superuser
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer