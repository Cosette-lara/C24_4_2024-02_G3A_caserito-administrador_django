from django.contrib import admin
from .models import Usuario, Restaurante, Calificacion, Comentario, Detalle, Favorito

admin.site.register(Usuario)
admin.site.register(Restaurante)
admin.site.register(Calificacion)
admin.site.register(Comentario)
admin.site.register(Detalle)
admin.site.register(Favorito)