from django.db import models
from django.core.exceptions import ValidationError

#validador de titulo
def validar_titulo(titulo):
    if 'cobol' in titulo:
        raise ValidationError(f'{titulo} no se vende mucho')
    return titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=70)
    libro = models.ManyToManyField(
        'Libro',
        through='AutorCapitulo',
        related_name='libros_autores',
        through_fields=('autor','libro')
    )

class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=70, blank=True, validators=[validar_titulo])
    paginas = models.PositiveIntegerField()
    fecha_publicacion = models.DateField(null=True)
    imagen = models.URLField(max_length=85, null=True)
    desc_corta = models.CharField(max_length=2000)
    estatus = models.CharField(max_length=1)
    categoria = models.CharField(max_length=50)
    edicion_anterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, related_name='ediciones_posteriores')
    editorial = models.ForeignKey('Editorial', on_delete=models.PROTECT)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~models.Q(titulo='cobol'),
                name='titulo_no_permitido_chk'
            )
        ]

    def get_historial_ediciones(self):
        """
        Retorna una lista con todas las ediciones anteriores del libro
        ordenadas de la más reciente a la más antigua
        """
        historial = []
        edicion = self.edicion_anterior
        
        while edicion is not None:
            historial.append(edicion)
            edicion = edicion.edicion_anterior
            
        return historial

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"


class LibroCronica(models.Model):
    descripcion_larga = models.TextField(null=True)
    libro = models.OneToOneField(
        Libro,
        on_delete=models.CASCADE,
        primary_key=True
    )

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'libreria_editorial'

class AutorCapitulo(models.Model):
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    libro = models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True) 
    numero_capitulos = models.IntegerField(default=0)
