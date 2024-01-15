from django.db import models

class RegistroU(models.Model):
    id_registroU = models.AutoField(primary_key=True, db_column='id_registro')
    nombre = models.CharField(max_length=100, db_column='nombre')
    apellidop = models.CharField(max_length=100, db_column='apellidoP')
    apellidom = models.CharField(max_length=100, db_column='apellidoM')
    email = models.CharField(max_length=150, db_column='email')
    contra = models.CharField(max_length=100, db_column='contra')
    numero_telefono = models.CharField(max_length=12, null=True, blank=True, db_column='numero_telefono')
    class Meta:
        db_table='R_usuario'
        
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, db_column='id_registro')
    nombre = models.CharField(max_length=100, db_column='nombre')
    apellidop = models.CharField(max_length=100, db_column='apellidoP')
    apellidom = models.CharField(max_length=100, db_column='apellidoM')
    email = models.CharField(max_length=150, db_column='email')
    contra = models.CharField(max_length=100, db_column='contra')
    class Meta:
        db_table='cliente'

class Encuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True, db_column='id_respuesta')
    gama = models.CharField(max_length=35, db_column='gama')
    frecuencia = models.CharField(max_length=100, db_column='frecuencia')
    met_pago = models.CharField(max_length=100, db_column='met_pago')
    dispositivo = models.CharField(max_length=100, db_column='dispositivo')
    opc_correo = models.CharField(max_length=10, db_column='opc_correo')
    serv_mensajeria = models.CharField(max_length=30, db_column='serv_mensajeria')
    opc_chatbot = models.CharField(max_length=10, db_column='opc_chatbor')
    opc_atencion_pers = models.CharField(max_length=10, db_column='opc_atencion_pers')
    tiempo_nave = models.CharField(max_length=100, db_column='tiempo_nav')
    class Meta:
        db_table='respuesta'
        
class CategoriaProducto(models.Model):
    id_categoria= models.AutoField(primary_key=True, db_column='id_categoria')
    descripcion = models.CharField(max_length=300, db_column='descripcion')
    class Meta:
        db_table = 'categoria_producto'
        
class Marca(models.Model):
    id_marca= models.AutoField(primary_key=True, db_column='id_marca')
    descripcion = models.CharField(max_length=300, db_column='descripcion')
    class Meta:
        db_table = 'marca_producto'

class UnidadMedida(models.Model):
    id_unidadMedida= models.AutoField(primary_key=True, db_column='id_unidadMedida')
    descripcion = models.CharField(max_length=300, db_column='descripcion')
    class Meta:
        db_table = 'unidad_medida'
        
class Tamaño(models.Model):
    id_tomaño= models.AutoField(primary_key=True, db_column='id_tamaño')
    descripcion = models.CharField(max_length=300, db_column='descripcion')
    class Meta:
        db_table = 'tamaño'

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, db_column='id_producto')
    nombre = models.CharField(max_length=100, db_column='nombre')
    descripcion = models.CharField(max_length=500, db_column='descripcion')
    precio = models.DecimalField(max_digits=10, decimal_places=2, db_column='precio')
    imagen = models.ImageField(upload_to='static/imagenes_productos/', db_column='imagen')
    categoria = models.CharField(max_length=100, db_column='categoria')
    marca = models.CharField(max_length=100, db_column='marca')
    unidadMedida = models.CharField(max_length=100, db_column='unidadmedida')
    tamaño = models.CharField(max_length=100, db_column='tamaño')
    class Meta:
        db_table = 'productos'

class Venta(models.Model):
    id_venta= models.AutoField(primary_key=True, db_column='id_venta')
    id_productofk = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_registroUfk = models.ForeignKey(RegistroU, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    class Meta:
        db_table = 'venta'
        
class prueba(models.Model):
    id_venta= models.AutoField(primary_key=True, db_column='id_venta')
    class Meta:
        db_table = 'prueba'