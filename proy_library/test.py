from libreria.models import Libro, Autor, AutorCapitulo, Editorial, LibroCronica
from django.db.models import Min, Max, Avg, Count, Sum
from django.db.models.functions import Left
from django.db.models.functions import Substr
from django.db.models import F, Q

editorial = Editorial.objects.create(nombre='Editorial 1')

# Incercion basica de datos en la tabla Libro
libro = Libro.objects.create(
    isbn='1234567890123',
    titulo='Ciencia para Todos',
    paginas=100,
    fecha_publicacion='2021-01-01',
    imagen='http://imagen.com',
    desc_corta='Descripcion corta',
    estatus='A',
    categoria='Educación',
    editorial=editorial
)

# 1. Crea 5 autores y relaciónalos con el libro “Ciencia para Todos” usando bulk_create.
libro = Libro.objects.get(titulo='Ciencia para Todos')

autores = [
    Autor(nombre='yent'),
    Autor(nombre='luis'),
    Autor(nombre='gaby'),
    Autor(nombre='carlos'),
    Autor(nombre='miguel')
]

Autor.objects.bulk_create(autores)

for autor in autores:
    AutorCapitulo.objects.create(autor=autor, libro=libro)

# 2. Encuentra todos los autores cuyos nombres contengan la letra "e" y que hayan escrito un libro en la categoría "Educación".
autores = AutorCapitulo.objects.filter(
    autor_nombre_icontains='e',
    libro__categoria='Educación'
).values('autor__nombre')
print(autores)

# 3. Busca libros publicados entre los años 2018 y 2022, con más de 300 páginas, y que no pertenezcan a la categoría "Historia".
libros = Libro.objects.filter(fecha_publicacion__range=['2018-01-01', '2022-12-31'],
    paginas__gt=300
).exclude(categoria='Historia').values('titulo')
print(libros)

# 4. Dado el libro “Cuentos Cortos”, muestra todos sus autores.
autores = AutorCapitulo.objects.filter(libro_titulo='Cuentos Cortos').values('autor_nombre')
print(autores)

# 5. Decrementa el número de páginas en 25 para todos los libros con más de 200 páginas y cuyo autor sea “Luis”.
libros = Libro.objects.filter(paginas_gt=200,autorcapituloautor_nombre='Luis').update(paginas=F('paginas') - 25)