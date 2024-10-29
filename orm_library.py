from library.models import Libro, Autor, AutorCapitulo, Editorial, LibroCronica
from django.db.models import Min, Max, Avg, Count, Sum
from django.db.models.functions import Left
from django.db.models.functions import Substr
from django.db.models import F, Q

# sentencias orm 
# Incercion basica de datos en la tabla Autor
Autor.objects.create(nombre='Autor desde el orm')

# Incercion basica de datos en la tabla Autor con el metodo save
autor = Autor.objects.create(nombre='Gabril Garcia Marquez')
autor.save()

# Incercion basica de datos en la tabla Autor con el metodo bulk_create

autores = [
    Autor(nombre='Autor 1M'),
    Autor(nombre='Autor 2M'),
    Autor(nombre='Autor 3M')
]

Autor.objects.bulk_create(autores)

# Consulta basica de datos en la tabla Autor con el metodo all
autores = Autor.objects.all()
for autor in autores:
    print(autor.nombre)

# Incercion basica de datos en la tabla Editorial con el metodo create
Editorial.objects.create(nombre='Editorial 1')

#obtener la editorial creada con el metodo get
editorial = Editorial.objects.get(nombre='Editorial 1')

# Incercion basica de datos en la tabla Libro
libro = Libro.objects.create(
    isbn='1234567890123',
    titulo='Cien años de soledad',
    paginas=100,
    fecha_publicacion='2021-01-01',
    imagen='http://imagen.com',
    desc_corta='Descripcion corta',
    estatus='A',
    categoria='Categoria 1',
    editorial=editorial
)

# Incercion basica de datos en la tabla Libro con el metodo bulk_create

libros = [
    Libro(
        isbn='1644567890123',
        titulo='El amor en los tiempos del colera',
        paginas=100,
        fecha_publicacion='2021-01-01',
        imagen='http://imagen.com',
        desc_corta='Descripcion corta',
        estatus='A',
        categoria='Categoria 1',
        editorial=editorial
    ),
    Libro(
        isbn='1634567890125',
        titulo='El alquimista',
        paginas=100,
        fecha_publicacion='2021-01-01',
        imagen='http://imagen.com',
        desc_corta='Descripcion corta',
        estatus='A',
        categoria='Categoria 1',
        editorial=editorial
    )
]

Libro.objects.bulk_create(libros)

# Obtener un libro con el metodo get
libro = Libro.objects.get(isbn='1234567890123')
print(libro)

#Obtener el primer libro con el metodo first
libro = Libro.objects.first()
print(libro)

#Obtener el ultimo libro con el metodo last
libro = Libro.objects.last()
print(libro)

# Obtener los primeros 2 libros 
libros = Libro.objects.all()[:2]    
print(libros)


# Consultas por coincidencia
# Obtener los libros con el isbn que empieza con 16 con el metodo startswith
libros = Libro.objects.filter(isbn__startswith='16')
print(libros)

# Consultas mayor que con el metodo gt(>)
# Obtener los libros con mas de 200 paginas con el metodo gt
libros = Libro.objects.filter(paginas__gt=200)
print(libros)

# Consultas con not in con el metodo exclude 
# consultar los libros que tenga mas de 200 paginas y que no su isbn no sea 1234567890123
libros = Libro.objects.filter(paginas__gt=200).exclude(isbn='1234567890123')
print(libros)

# Consultas mayor o igual que con el metodo gte(>=)
# Consultar los libros que tengan 200 o mas paginas
libros = Libro.objects.filter(paginas__gte=200).values('titulo','paginas')
print(libros)

# Consulta menor que con el metodo lt(<)
# Consultar los libros que tengan menos de 200 paginas
libros = Libro.objects.filter(paginas__lt=200).values('titulo','paginas')
print(libros)

# Consulta menor o igual que con el metodo lte(<=)
# Consultar los libros que tengan 200 o menos paginas
libros = Libro.objects.filter(paginas__lte=200).values('titulo','paginas')
print(libros)

# Consultas con count
# Contar los libros que tengan menos de 200 paginas
libros = Libro.objects.filter(paginas__lt=200).count()
print(libros)

# Consulta con or forma larga 
# Consultar los libros con 200 o 300 paginas
libros1 = Libro.objects.filter(paginas=200)
libros2 = Libro.objects.filter(paginas=300)
consulta = (libros1 | libros2).values('titulo','paginas')
print(consulta)

# Consuta por fecha con el metodo year 
# Consultar los libros que se publicaron en el 2021
libros = Libro.objects.filter(fecha_publicacion__year=2021).values('titulo','fecha_publicacion')
print(libros)

# Filtrando con expreciones regulares con el metodo regex (pag 26)
# Consultar cuyo isb comience con 19 seguido de 8 digitos
libros = Libro.objects.filter(isbn__regex=r'^19\d{8}$').values('isbn')
print(libros)

# Consulta con union con el metodo union 
# Consultar el nombre de los autores que contengan hill con las editoriales que contengan hill
autores = Autor.objects.filter(nombre__icontains='hill').values('nombre')
editoriales = Editorial.objects.filter(nombre__icontains='hill').values('nombre')
union = autores.union(editoriales)
print(union)

# Consulta con con el metodo order_by 
# Obtener el cuarto libro con mas paginas
libro = Libro.objects.values("isbn","paginas").order_by("-paginas")[3]
print(libro)

#Obtener el cuarto y quinto libro con mas paginas
libros = Libro.objects.values("isbn","paginas").order_by("-paginas")[3:5]
print(libros)

# Consulta por indice 
libro = Libro.objects.filter(paginas__gt=200).explain()
print(libro)

# Consultas de agregacion y agrupacion
# con las funciones Min, Max, Avg, Count, Sum
# Consulta con la funcion Min
# Consultar el numero minimo de paginas de los libros con la funcion Min
libro = Libro.objects.filter(paginas__gt=0).aggregate(Min('paginas'))
print(libro)

# Consultar el numero maximo de paginas de los libros con la funcion Max
libro = Libro.objects.filter(paginas__gt=0).aggregate(Max('paginas'))
print(libro)

# Consultar el numero promedio de paginas de los libros con la funcion Avg
libro = Libro.objects.filter(paginas__gt=0).aggregate(Avg('paginas'))
print(libro)

# Consultar el numero total de paginas de los libros de python con la funcion Sum
libro = Libro.objects.filter(categoria__icontains='python').aggregate(Sum('paginas'))
print(libro)

# Consultar el numero de libros con la funcion Count
libro = Libro.objects.filter(paginas__gt=0).aggregate(Count('paginas'))
print(libro)

# Consulta con group by y annotate
# Consultar los libros son de python por categoria y contar cuantos libro de cada categoria hay
libros = Libro.objects.filter(categoria__contains
 ='python').values('categoria').annotate(
 NumeroLibros=Count('*')) 
 
print(libros)

# Consulta los libros que son de python por categoria y contar cuantos libro hay
libro = Libro.objects.filter(categoria__icontains='python').values('categoria'
 ,'editorial__nombre').annotate(NumeroLibros=Count('*'))  
print(libro)

# Consultas Having(filtrar agrupaciones)
# Filtrar los libros por fecha de publicación y filtrar solo las que tengan más de 2 libros en esa fecha
Consulta_fechas = Libro.objects.values('fecha_publicacion').annotate(cant_fec_pub=Count('fecha_publicacion')).filter(cant_fec_pub__gte=2).values_list('fecha_publicacion', flat=True)
print(Consulta_fechas)

# Para obtener el detalle de los libros que se publicaron en esas fechas
Detalle_libros = Libro.objects.filter(fecha_publicacion__in=Consulta_fechas).values('isbn', 'fecha_publicacion')
print(Detalle_libros)

# Consultas con Distinct
# El metodo distinct se utiliza para eliminar los registros duplicados de una consulta
# Consultar las categorias de los libros sin repetir
libros = Libro.objects.values('categoria').distinct()
print(libros)

# Consultas usando Substr
# Anotamos cada libro con una descripción resumida que toma los primeros 15 caracteres de 'desc_corta'
libro = Libro.objects.annotate(
    desc_resumida=Substr('desc_corta', 1, 15)
).values('isbn', 'desc_resumida')

# Imprimimos el resultado de la consulta
print(libro)

# Este filtro encuentra libros cuyo título es exactamente igual a los primeros 50 caracteres de su descripción corta
libros = Libro.objects.filter(titulo__exact=F('desc_corta')[:50])
print(libros)

# Consultas con Q
#  Consultar los libros de categoria python o que tengan mas de 100 paginas
libro = Libro.objects.filter( 
(Q(categoria__contains='python') |  
Q(categoria__contains='java') |  
Q(categoria__contains='net')) &  
~Q(paginas=100))
print(libro) 

#Consultas con left join
# Consultar los libros con sus autores
libros = Libro.objects.values('titulo','isbn','libros_autores__nombre')
print(libros)

#Consultar libros de python con sus editoriales
libros = Libro.objects.filter(categoria__icontains='python').values('titulo','categoria','editorial__nombre')
print(libros)

# ahora utilizamos el metodo select_related
libros = Libro.objects.filter(categoria__icontains='python').select_related('editorial').values('titulo','categoria','editorial__nombre')
print(libros)

# consultar 2 autores con sus libros 
autores = Autor.objects.all().values('nombre','libro__titulo')
print(autores)

#consulta con prefetch_related  
autores = Autor.objects.all().prefetch_related('libro').values('nombre','libro__titulo')
print(autores)

# listar cada uno de sus libros, pero ahora debemos mostrar el nombre de la editorial por cada uno de los libros 
# con el metodo prefetch_related
autores = Autor.objects.all().prefetch_related('libro__editorial').values('nombre','libro__titulo','libro__editorial__nombre')
print(autores)


