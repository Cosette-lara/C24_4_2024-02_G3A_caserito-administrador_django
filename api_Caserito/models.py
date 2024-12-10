from django.db import models

class Usuario(models.Model):
    pk_usuario = models.BigAutoField(primary_key=True)
    usuario = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=200)
    direccion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Restaurante(models.Model):
    pk_restaurante = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    hora_apertura = models.TimeField(blank=True, null=True)
    hora_cierre = models.TimeField(blank=True, null=True)
    img = models.URLField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    ubicacion = models.TextField()
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='fk_usuario'
    )

    class Meta:
        managed = False
        db_table = 'restaurante'

class Calificacion(models.Model):
    pk_calificacion = models.BigAutoField(primary_key=True)
    calificacion = models.IntegerField()
    fk_restaurante = models.ForeignKey(
        Restaurante,
        on_delete=models.CASCADE,
        db_column='fk_restaurante'
    )
    fk_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='fk_usuario' 
    )

    class Meta:
        managed = False
        db_table = 'calificacion'


class Comentario(models.Model):
    pk_comentario = models.BigAutoField(primary_key=True)
    comentario = models.CharField(max_length=200)
    fk_restaurante = models.ForeignKey(
        'Restaurante', on_delete=models.CASCADE, db_column='fk_restaurante'
    )
    fk_usuario = models.ForeignKey(
        'Usuario', on_delete=models.CASCADE, db_column='fk_usuario'  
    )

    class Meta:
        managed = False
        db_table = 'comentario'

class Detalle(models.Model):
    pk_detalle = models.BigAutoField(primary_key=True)
    informacion = models.CharField(max_length=255)
    detalles_tipo = models.CharField(max_length=50, choices=[
        ('EMAIL', 'Email'),
        ('FACEBOOK', 'Facebook'),
        ('NUMERO', 'Número'),
        ('WHATSAPP', 'WhatsApp')
    ], blank=True, null=True)
    fk_restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'detalle'


class Favorito(models.Model):
    pk_favorito = models.BigAutoField(primary_key=True)
    fk_restaurante = models.ForeignKey(
        'Restaurante', on_delete=models.CASCADE, db_column='fk_restaurante'
    )
    fk_usuario = models.ForeignKey(
        'Usuario', on_delete=models.CASCADE, db_column='fk_usuario' 
    )

    class Meta:
        managed = False
        db_table = 'favorito'

class Menu(models.Model):
    pk_menu = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=1500)
    img = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    precio = models.BigIntegerField()
    fk_restaurante = models.ForeignKey(
        Restaurante,
        on_delete=models.CASCADE,
        db_column='fk_restaurante' 
    )

    class Meta:
        managed = False
        db_table = 'menu'


class Rol(models.Model):
    pk_rol = models.BigAutoField(primary_key=True)
    role_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'


class UsuarioRol(models.Model):
    pk_usuario = models.ForeignKey(
        'Usuario',
        on_delete=models.CASCADE,
        db_column='pk_usuario'  
    )
    pk_rol = models.ForeignKey(
        'Rol',
        on_delete=models.CASCADE,
        db_column='pk_rol'  
    )

    class Meta:
        managed = False
        db_table = 'usuario_rol'




