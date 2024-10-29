from aplication.core.models import *
from aplication.attention.models import *
from django.db.models import Q
from django.db.models import Sum,Avg,Max,Min,Count
from django.db.models import F

# Crear un registro de TipoSangre con el método create
tipo1 = TipoSangre.objects.create(tipo="A+", descripcion="Tipo A positivo")
# Equivalete al metodo create, pero en lenguaje sql
   #INSERT INTO "core_tiposangre" ("tipo", "descripcion")
   #VALUES ('A+', 'Tipo A positivo') RETURNING "core_tiposangre"."id"
   
# Crea un registro de TipoSangre con el método save
tipo2 = TipoSangre(tipo="B-", descripcion="Tipo B negativo")
tipo2.save() # Y luego con save() lo guarda el registro en la base de datos
# Equivalente al metodo save, pero en lenguaje sql
   #INSERT INTO "core_tiposangre" ("tipo", "descripcion")
   #VALUES ('B-', 'Tipo B negativo') RETURNING "core_tiposangre"."id"

# Inserta un registro de TipoSangre con el método bulk_create
tipos_sangre = [
    TipoSangre(tipo="B+", descripcion="Tipo B positivo"),
    TipoSangre(tipo="B-", descripcion="Tipo B negativo"),
]
TipoSangre.objects.bulk_create(tipos_sangre)
# Equivalente al metodo bulk_create,en lenguaje sql
   #INSERT INTO "core_tiposangre" ("tipo", "descripcion")
   #VALUES ('B+', 'Tipo B positivo'), ('B-', 'Tipo B negativo') RETURNING "core_tiposangre"."id"

# Consulta todos los registros de TipoSangre con todos sus campos
tipos_sangre = TipoSangre.objects.all()
# Muestra los registros de TipoSangre
for tipo in tipos_sangre:
    print(f"Tipo: {tipo.tipo}, Descripción: {tipo.descripcion}")
# Equivalente al metodo all, pero en lenguaje sql
    #SELECT "core_tiposangre"."id", "core_tiposangre"."tipo", "core_tiposangre"."descripcion"

# Consulta un registro de TipoSangre con el tipo "O+,A,AB+""
tipo_O_pos = TipoSangre.objects.get(tipo="O+")
tipo_A = TipoSangre.objects.get(tipo="A")
tipo_ab_pos = TipoSangre.objects.get(tipo="AB+")
# Equivalente al metodo get, pero en lenguaje sql
    #SELECT "core_tiposangre"."id", "core_tiposangre"."tipo", "core_tiposangre"."descripcion"
    #FROM "core_tiposangre" WHERE "core_tiposangre"."tipo" = 'O+' LIMIT 21
    #SELECT "core_tiposangre"."id", "core_tiposangre"."tipo", "core_tiposangre"."descripcion"
    #FROM "core_tiposangre" WHERE "core_tiposangre"."tipo" = 'A' LIMIT 21
    #SELECT "core_tiposangre"."id", "core_tiposangre"."tipo", "core_tiposangre"."descripcion"
    #FROM "core_tiposangre" WHERE "core_tiposangre"."tipo" = 'AB+' LIMIT 21

# Crear un registro de paciente con el método bulk_create
pacientes = [
    Paciente(
        nombres="Juan",
        apellidos="Pérez",
        cedula="1234567890",
        fecha_nacimiento="1980-01-15",
        telefono="0998765432",
        email="juan.perez@example.com",
        sexo="M",
        estado_civil="C",
        direccion="Calle Falsa 123",
        latitud=-0.123456,
        longitud=-78.123456,
        tipo_sangre= tipo_O_pos,
        alergias="Ninguna",
        enfermedades_cronicas="Hipertensión",
        medicacion_actual="Losartán",
        cirugias_previas="Apendicectomía",
        antecedentes_personales="Diabetes en tratamiento",
        antecedentes_familiares="Corazón en la familia"
    ),
    Paciente(
        nombres="María",
        apellidos="Gómez",
        cedula="0987654321",
        fecha_nacimiento="1990-05-20",
        telefono="0991234567",
        email="maria.gomez@example.com",
        sexo="F",
        estado_civil="S",
        direccion="Av. Libertad 456",
        latitud=-0.654321,
        longitud=-78.654321,
        tipo_sangre=tipo_A,
        alergias="Penicilina",
        enfermedades_cronicas="Asma",
        medicacion_actual="Salbutamol",
        cirugias_previas="Ninguna",
        antecedentes_personales="No fuma",
        antecedentes_familiares="Madre con cáncer"
    ),
    Paciente(
        nombres="Carlos",
        apellidos="Ramírez",
        cedula="1357924680",
        fecha_nacimiento="1975-09-30",
        telefono="0987654321",
        email="carlos.ramirez@example.com",
        sexo="M",
        estado_civil="C",
        direccion="Calle 10 de Agosto 789",
        latitud=-0.321654,
        longitud=-78.321654,
        tipo_sangre=tipo_ab_pos,
        alergias="Ninguna",
        enfermedades_cronicas="Ninguna",
        medicacion_actual="Ninguna",
        cirugias_previas="Ninguna",
        antecedentes_personales="No antecedentes relevantes",
        antecedentes_familiares="Padre con hipertensión"
    ),
]
Paciente.objects.bulk_create(pacientes)
# Equivalente al metodo bulk_create, pero en lenguaje sql
    # INSERT INTO "core_paciente" (
    #     "nombres", "apellidos", "cedula", "fecha_nacimiento", "telefono", "email", "sexo", "estado_civil", "direccion", "latitud", "longitud", "tipo_sangre_id", "alergias", "enfermedades_cronicas", "medicacion_actual", "cirugias_previas", "antecedentes_personales", "antecedentes_familiares"
    # ) VALUES
    #     ('Juan', 'Pérez', '1234567890', '1980-01-15', '0998765432', 'juan.perez@example.com', 'M', 'C', 'Calle Falsa 123', -0.123456, -78.123456, 'tipo_O_pos', 'Ninguna', 'Hipertensión', 'Losartán', 'Apendicectomía', 'Diabetes en tratamiento', 'Corazón en la familia'),
    #     ('María', 'Gómez', '0987654321', '1990-05-20', '0991234567', 'maria.gomez@example.com', 'F', 'S', 'Av. Libertad 456', -0.654321, -78.654321, 'tipo_A', 'Penicilina', 'Asma', 'Salbutamol', 'Ninguna', 'No fuma', 'Madre con cáncer'),
    #     ('Carlos', 'Ramírez', '1357924680', '1975-09-30', '0987654321', 'carlos.ramirez@example.com', 'M', 'C', 'Calle 10 de Agosto 789', -0.321654, -78.321654, 'tipo_ab_pos', 'Ninguna', 'Ninguna', 'Ninguna', 'No antecedentes relevantes', 'Padre con hipertensión');

# Presenta todos los pacientes con sus campos utilizando el método all
pacientes=Paciente.objects.all()
for paciente in pacientes:
    print(f"--- Paciente ---")
    print(f"Nombres: {paciente.nombres}")
    print(f"Apellidos: {paciente.apellidos}")
    print(f"Cédula: {paciente.cedula}")
    print(f"Fecha de Nacimiento: {paciente.fecha_nacimiento}")
    print(f"Teléfono: {paciente.telefono}")
    print(f"Email: {paciente.email}")
    print(f"Sexo: {paciente.sexo}")
    print(f"Estado Civil: {paciente.estado_civil}")
    print(f"Dirección: {paciente.direccion}")
    print(f"Latitud: {paciente.latitud}")
    print(f"Longitud: {paciente.longitud}")
    print(f"Tipo de Sangre: {paciente.tipo_sangre.tipo if paciente.tipo_sangre else 'No especificado'}")
    print(f"Alergias: {paciente.alergias if paciente.alergias else 'Ninguna'}")
    print(f"Enfermedades Crónicas: {paciente.enfermedades_cronicas if paciente.enfermedades_cronicas else 'Ninguna'}")
    print(f"Medicación Actual: {paciente.medicacion_actual if paciente.medicacion_actual else 'Ninguna'}")
    print(f"Cirugías Previas: {paciente.cirugias_previas if paciente.cirugias_previas else 'Ninguna'}")
    print(f"Antecedentes Personales: {paciente.antecedentes_personales if paciente.antecedentes_personales else 'Ninguno'}")
    print(f"Antecedentes Familiares: {paciente.antecedentes_familiares if paciente.antecedentes_familiares else 'Ninguno'}")
    print("-----------------------------")
# Equivalente al metodo all, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente"

# Consulta un paciente con el tipo de sangre "O+" utilizando el método filter
pacientes_o_plus = Paciente.objects.filter(tipo_sangre__tipo="O+")
print(pacientes_o_plus)
# Equivalente al metodo filter, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" = 'O+'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consulta un paciente con el tipo de sangre "A"  utilizando el exact
pacientes_a = Paciente.objects.filter(tipo_sangre__tipo__exact="A")
print(pacientes_a)
# Equivalente al metodo exact, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" = 'A'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consulta un paciente con el tipo de sangre "AB" utilizando el iexact
pacientes_ab = Paciente.objects.filter(tipo_sangre__tipo__iexact="AB")
print(pacientes_ab)
# Equivalente al metodo iexact, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" ILIKE 'AB'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consulta un paciente con el tipo de sangre que contenga "B" utilizando el contains
pacientes_b = Paciente.objects.filter(tipo_sangre__tipo__contains="B")
print(pacientes_b)
# Equivalente al metodo contains, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" LIKE '%B%'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consulta un paciente con el tipo de sangre que contenga "O" utilizando el icontains
pacientes_o = Paciente.objects.filter(tipo_sangre__tipo__icontains="O")
print(pacientes_o)
# Equivalente al metodo icontains, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" ILIKE '%O%'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consulta un paciente con el tipo de sangre que empiece con "A" utilizando el startswith
pacientes_a = Paciente.objects.filter(tipo_sangre__tipo__startswith="A")
print(pacientes_a)
# Equivalente al metodo startswith, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" LIKE 'A%'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21  
    
# Consulta un paciente con el tipo de sangre que empiece con "O" utilizando el istartswith
pacientes_o = Paciente.objects.filter(tipo_sangre__tipo__istartswith="O")
print(pacientes_o)
# Equivalente al metodo istartswith, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" ILIKE 'O%'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consulta un paciente con el tipo de sangre que termine con "A" utilizando el endswith
pacientes_a = Paciente.objects.filter(tipo_sangre__tipo__endswith="A")
print(pacientes_a)
# Equivalente al metodo endswith, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" LIKE '%A'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21
    
# Consulta un paciente con el tipo de sangre que termine con "O" utilizando el iendswith
pacientes_o = Paciente.objects.filter(tipo_sangre__tipo__iendswith="O")
print(pacientes_o)
# Equivalente al metodo iendswith, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" ILIKE '%O'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21
    
# Consulta un paciente con el tipo de sangre que contenga "O" utilizando el regex
pacientes_o = Paciente.objects.filter(tipo_sangre__tipo__regex=r'^[O]')
print(pacientes_o)
# Equivalente al metodo regex, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" ~ '^[O]'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consulta un paciente con el tipo de sangre que contenga "O" sin distinguir mayúsculas/minúsculas utilizando el iregex
pacientes_o = Paciente.objects.filter(tipo_sangre__tipo__iregex=r'^[o]')
print(pacientes_o)
# Equivalente al metodo iregex, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")  
    #WHERE "core_tiposangre"."tipo" ~* '^[o]'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21
    
# Consulta pacientes que contengan 'O' en el tipo de sangre. Ejemplo icontains
pacientes_con_o = Paciente.objects.filter(tipo_sangre__tipo__icontains="O")
print(pacientes_con_o)
# Equivalente al metodo icontains, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_tiposangre"."tipo" ILIKE '%O%'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consulta pacientes cuyos nombres empiecen con una "y" o "w" sin importar mayúsculas/minúsculas
pacientes_con_yw = Paciente.objects.filter(nombres__iregex=r'^[yw]')
print(pacientes_con_yw)
# Equivalente al metodo iregex, pero en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente"
    #WHERE "core_paciente"."nombres" ~* '^[yw]'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Funciones con fecha del Orm
# year: fecha__year=2024  o # (fecha__year__in=[2022, 2023, 2024]
pacientes_2024 = Paciente.objects.filter(fecha_nacimiento__year=2024).values('apellidos','fecha_nacimiento')
print(pacientes_2024)
# Equivalente al metodo year, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE EXTRACT('year' FROM "core_paciente"."fecha_nacimiento") = 2024
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consulta pacientes en octubre de 2024
pacientes_oct_2024 = Paciente.objects.filter(fecha_nacimiento__year=2024, fecha_nacimiento__month=10).values('apellidos','fecha_nacimiento')
print(pacientes_oct_2024)
# Equivalente al metodo month, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE EXTRACT('year' FROM "core_paciente"."fecha_nacimiento") = 2024
    #AND EXTRACT('month' FROM "core_paciente"."fecha_nacimiento") = 10
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consultar pacientes que nacieron el 15 de cualquier mes
pacientes_15 = Paciente.objects.filter(fecha_nacimiento__day=15).values('apellidos','fecha_nacimiento')
print(pacientes_15)
# Equivalente al metodo day, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"   
    #WHERE EXTRACT('day' FROM "core_paciente"."fecha_nacimiento") = 15
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21
    
# Consultar pacientes que nacieron en domingo
pacientes_domingo = Paciente.objects.filter(fecha_nacimiento__week_day=1).values('apellidos','fecha_nacimiento')
print(pacientes_domingo)
# Equivalente al metodo week_day, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE EXTRACT('dow' FROM "core_paciente"."fecha_nacimiento") = 0
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21
    
# Consultar pacientes que nacieron en el segundo trimestre
pacientes_trimestre_2 = Paciente.objects.filter(fecha_nacimiento__quarter=2).values('apellidos','fecha_nacimiento')
print(pacientes_trimestre_2)
# Equivalente al metodo quarter, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE EXTRACT('quarter' FROM "core_paciente"."fecha_nacimiento") = 2
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21
    
# Consultar pacientes comprobando si la fecha de nacimiento es NULL
pacientes_sin_fecha = Paciente.objects.filter(fecha_nacimiento__isnull=True).values('apellidos','fecha_nacimiento')
print(pacientes_sin_fecha)
# Equivalente al metodo isnull, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE "core_paciente"."fecha_nacimiento" IS NULL
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21
    
# Consultas con gt (mayor que), lt (menor que), gte (mayor o igual que) y lte (menor o igual que) o el rango
# Consultar pacientes nacidos después de 1980 utilizando el operador gt (mayor que)
pacientes_nacidos_despues_1980 = Paciente.objects.filter(fecha_nacimiento__year__gt=1980).values('apellidos', 'fecha_nacimiento')
print(pacientes_nacidos_despues_1980)
# Equivalente al metodo gt, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE EXTRACT('year' FROM "core_paciente"."fecha_nacimiento") > 1980
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consultar pacientes nacidos antes de 1980 utilizando el operador lt (menor que)
pacientes_nacidos_antes_1980 = Paciente.objects.filter(fecha_nacimiento__year__lt=1980).values('apellidos', 'fecha_nacimiento')
print(pacientes_nacidos_antes_1980)
# Equivalente al metodo lt, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE EXTRACT('year' FROM "core_paciente"."fecha_nacimiento") < 1980
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21
    
# Consultar pacientes nacidos en 1980 o después utilizando el operador gte (mayor o igual que)
pacientes_nacidos_1980_o_despues = Paciente.objects.filter(fecha_nacimiento__year__gte=1980).values('apellidos', 'fecha_nacimiento')
print(pacientes_nacidos_1980_o_despues)
# Equivalente al metodo gte, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE EXTRACT('year' FROM "core_paciente"."fecha_nacimiento") >= 1980
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consultar pacientes nacidos en 1980 o antes utilizando el operador lte (menor o igual que)
pacientes_nacidos_1980_o_antes = Paciente.objects.filter(fecha_nacimiento__year__lte=1980).values('apellidos', 'fecha_nacimiento')
print(pacientes_nacidos_1980_o_antes)   
# Equivalente al metodo lte, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE EXTRACT('year' FROM "core_paciente"."fecha_nacimiento") <= 1980
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consultar pacientes nacidos entre 1975 y 1989 utilizando el operador range
pacientes_nacidos_1975_1989 = Paciente.objects.filter(fecha_nacimiento__year__range=[1975, 1989]).values('apellidos', 'fecha_nacimiento')
print(pacientes_nacidos_1975_1989)
# Equivalente al metodo range, pero en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento"
    #FROM "core_paciente"
    #WHERE EXTRACT('year' FROM "core_paciente"."fecha_nacimiento") BETWEEN 1975 AND 1989
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consultar pacientes los nombre y las descripciones de los tipos de sangre de los pacientes con tipo de sangre "AB+" 
pacientes_ab = Paciente.objects.filter(tipo_sangre__tipo="AB+").values('nombres', 'apellidos', 'tipo_sangre__descripcion')
print(pacientes_ab)
# Equivalente al metodo values, pero en lenguaje sql
    #SELECT "core_paciente"."nombres", "core_paciente"."apellidos", "core_tiposangre"."descripcion"

# Consultar los tipos de sangre "AB+" y los nombres de los pacientes asociados
tipos_sangre_ab = TipoSangre.objects.filter(tipo="AB+").values('descripcion', 'tipos_sangre__nombres', 'tipos_sangre__apellidos')
print(tipos_sangre_ab)
# Equivalente al metodo values, pero en lenguaje sql
    #SELECT "core_tiposangre"."descripcion", "core_paciente"."nombres", "core_paciente"."apellidos"
    #FROM "core_tiposangre" LEFT OUTER JOIN "core_paciente" ON ("core_tiposangre"."id" = "core_paciente"."tipo_sangre_id")
    #WHERE "core_tiposangre"."tipo" = 'AB+'

# Consulta inversa de un paciente con tipo de sangre "AB+"
# Obtener el tipo de sangre "AB+"
tipo_sangre_ab = TipoSangre.objects.get(tipo="AB+")
# Obtener todos los pacientes que tienen este tipo de sangre
pacientes_con_ab = tipo_sangre_ab.tipos_sangre.all().values('nombres', 'apellidos')
print(pacientes_con_ab)
# Equivalente al metodo all, pero en lenguaje sql
    #SELECT "core_paciente"."nombres", "core_paciente"."apellidos" 
    #FROM "core_paciente"
    #WHERE "core_paciente"."tipo_sangre_id" = 4
    
# Consulta orm con and(AND), or(OR) 
# Consultar pacientes que nacieron en 1980 y tienen tipo de sangre "O+" utilizando el operador AND
pacientes_1980_o_plus = Paciente.objects.filter(fecha_nacimiento__year=1980, tipo_sangre__tipo="O+").values('apellidos', 'fecha_nacimiento', 'tipo_sangre__descripcion')
print(pacientes_1980_o_plus)
# Equivalente en lenguaje sql
    #SELECT "core_paciente"."apellidos", "core_paciente"."fecha_nacimiento", "core_tiposangre"."descripcion"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")   
    #WHERE EXTRACT('year' FROM "core_paciente"."fecha_nacimiento") = 1980
    #AND "core_tiposangre"."tipo" = 'O+'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

#Consultar pacientes que nacieron en 1980 o tienen tipo de sangre "O+" utilizando el operador OR
pacientes = Paciente.objects.filter(Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"))
print(pacientes)
# Equivalente en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_paciente"."fecha_nacimiento" = 1980 OR "core_tiposangre"."tipo" = 'O+'
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21
    
#Consultar pacientes que nacieron en 1980 o tienen tipo de sangre "O+" y no tienen alergias
pacientes = Paciente.objects.filter( Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"), alergias__isnull=True) # Esta condición se aplica con AND implícito
print(pacientes)
# Equivalente en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE "core_paciente"."fecha_nacimiento" = 1980 OR "core_tiposangre"."tipo" = 'O+'
    #AND "core_paciente"."alergias" IS NULL
    # ORDER BY "core_paciente"."apellidos" ASC  
    # LIMIT 21

# Consulta orm con exclude 
# Consultar pacientes que no tienen tipo de sangre "AB+"
pacientes_no_ab_plus = Paciente.objects.exclude(tipo_sangre__tipo="AB+").values('apellidos', 'tipo_sangre__descripcion')
print(pacientes_no_ab_plus)
# Equivalente en lenguaje sql   
    #SELECT "core_paciente"."apellidos", "core_tiposangre"."descripcion"
    #FROM "core_paciente" INNER JOIN "core_tiposangre" ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
    #WHERE NOT ("core_tiposangre"."tipo" = 'AB+')
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consultar pacientes que nacieron después de 1980 y excluir aquellos con tipo de sangre "O-".
pacientes = Paciente.objects.filter(fecha_nacimiento__year__gt=1980).exclude(tipo_sangre__tipo="O-")
print(pacientes)
# Equivalente en lenguaje sql
    #SELECT "core_paciente"."id", "core_paciente"."nombres", "core_paciente"."apellidos", "core_paciente"."cedula", "core_paciente"."fecha_nacimiento", "core_paciente"."telefono", "core_paciente"."email", "core_paciente"."sexo", "core_paciente"."estado_civil", "core_paciente"."direccion", "core_paciente"."latitud", "core_paciente"."longitud", "core_paciente"."tipo_sangre_id", "core_paciente"."alergias", "core_paciente"."enfermedades_cronicas", "core_paciente"."medicacion_actual", "core_paciente"."cirugias_previas", "core_paciente"."antecedentes_personales", "core_paciente"."antecedentes_familiares"
    #FROM "core_paciente"
    #WHERE EXTRACT('year' FROM "core_paciente"."fecha_nacimiento") > 1980   
    #AND NOT ("core_paciente"."tipo_sangre_id" = 1) 
    # ORDER BY "core_paciente"."apellidos" ASC
    # LIMIT 21

# Consultar el cargo de los empleados con get y el id del cargo
cargo_1 = Cargo.objects.get(id=1)
print(cargo_1)

#Crear  empleados con el metodo Save
empleado1 = Empleado(
    nombres="Juan",
    apellidos="Pérez",
    cedula="1234567890",
    fecha_nacimiento="1990-01-01",
    cargo=cargo_1,
    sueldo=1500.00,
    direccion="Calle 1, Ciudad",
    latitud=-0.123456,
    longitud=-78.123456,
)

empleado2 = Empleado(
    nombres="María",
    apellidos="Gómez",
    cedula="0987654321",
    fecha_nacimiento="1985-05-15",
    cargo_id=2,
    sueldo=1600.00,
    direccion="Calle 2, Ciudad",
    latitud=-0.654321,
    longitud=-78.654321,
)
empleado1.save()
empleado2.save()

# Consultar empleados con values 
emps=Empleado.objects.values('nombres','sueldo')
print(emps)
# Equivalente en lenguaje sql   
    #SELECT "core_empleado"."nombres", "core_empleado"."sueldo" 
    #FROM "core_empleado"
    
# Consultar empleados con cargo "Enfermera"
# Para contar, sumar, promediar, obtener el máximo y el mínimo de los sueldos de todos los empleados
# Si hay condición dada la condición cargo_id=1
resultados = Empleado.objects.filter(cargo__descripcion__icontains="Enfermera").aggregate( 
    total_sueldo=Sum('sueldo'),
    promedio_sueldo=Avg('sueldo'),
    max_sueldo=Max('sueldo'),
    min_sueldo=Min('sueldo'),
    cantidad_enfermeras=Count('id')
)
print(resultados)
# Equivalente en lenguaje sql
    #SELECT SUM("core_empleado"."sueldo") AS "total_sueldo", AVG("core_empleado"."sueldo") AS "promedio_sueldo", MAX("core_empleado"."sueldo") AS "max_sueldo", MIN("core_empleado"."sueldo") AS "min_sueldo", COUNT("core_empleado"."id") AS "cantidad_enfermeras"
    #FROM "core_empleado" INNER JOIN "core_cargo" ON ("core_empleado"."cargo_id" = "core_cargo"."id")
    #WHERE "core_cargo"."descripcion" ILIKE '%Enfermera%' ESCAPE '\'

# Agrupar campos de una tabla
# Realizar la consulta de agregados agrupados por cargo
resultados = Empleado.objects.values('cargo__descripcion').annotate(
    total_sueldo=Sum('sueldo'),
    promedio_sueldo=Avg('sueldo'),
    max_sueldo=Max('sueldo'),
    min_sueldo=Min('sueldo'),
    cantidad_empleados=Count('id')
)
print(resultados)
# Equivalente en lenguaje sql
    #SELECT "core_cargo"."descripcion", SUM("core_empleado"."sueldo") AS "total_sueldo", AVG("core_empleado"."sueldo") AS "promedio_sueldo", MAX("core_empleado"."sueldo") AS "max_sueldo", MIN("core_empleado"."sueldo") AS "min_sueldo", COUNT("core_empleado"."id") AS "cantidad_empleados"
    #FROM "core_empleado" INNER JOIN "core_cargo" ON ("core_empleado"."cargo_id" = "core_cargo"."id")
    #GROUP BY "core_cargo"."descripcion"
    # ORDER BY "core_cargo"."descripcion" ASC
    # LIMIT 21
    
# Realizar la consulta de agregados agrupados por cargo y sueldo
resultados = Empleado.objects.values('cargo__descripcion', 'sueldo').annotate(
    cantidad_empleados=Count('id')
).order_by('cargo__descripcion', 'sueldo')  # Ordenar por cargo y sueldo
print(resultados)
# Equivalente en lenguaje sql
    #SELECT "core_cargo"."descripcion", "core_empleado"."sueldo", COUNT("core_empleado"."id") AS "cantidad_empleados"
    #FROM "core_empleado" INNER JOIN "core_cargo" ON ("core_empleado"."cargo_id" = "core_cargo"."id")
    #GROUP BY "core_cargo"."descripcion", "core_empleado"."sueldo"
    # ORDER BY "core_cargo"."descripcion" ASC, "core_empleado"."sueldo" ASC
    # LIMIT 21

# Realizar la consulta de empleados y agregar el nombre del cargo como un alias sin agrupar
resultados = Empleado.objects.annotate(
    cargo_descripcion=F('cargo__descripcion')  
)
print(resultados)
# Equivalente en lenguaje sql
    #SELECT "core_empleado"."id", "core_empleado"."nombres", "core_empleado"."apellidos", "core_empleado"."cedula", "core_empleado"."fecha_nacimiento", "core_empleado"."cargo_id", "core_empleado"."sueldo", "core_empleado"."direccion", "core_empleado"."latitud", "core_empleado"."longitud", "core_empleado"."cargo_id", "core_cargo"."descripcion" AS "cargo_descripcion"
    #FROM "core_empleado" LEFT OUTER JOIN "core_cargo" ON ("core_empleado"."cargo_id" = "core_cargo"."id")
    # LIMIT 21

# Actualizar los sueldos en un 10% para los empleados cuyo cargo sea "Enfermera"
Empleado.objects.filter(cargo__descripcion__icontains="Enfermera").update(sueldo=F('sueldo') * 1.10)
cargo = Cargo.objects.get(id=3) # Se obtiene el cargo con id 3
cargo.descripcion = "Financiero" # Se actualiza la descripción del cargo
cargo.save() # Se guarda el cambio
# Equivalente en lenguaje sql
    #UPDATE "core_empleado" SET "sueldo" = ("core_empleado"."sueldo" * 1.10)
    #WHERE "core_empleado"."cargo_id" IN (SELECT U0."id" FROM "core_cargo" U0 WHERE U0."descripcion" ILIKE '%Enfermera%' ESCAPE '\')
    
# Eliminar los tipos de sangre cuya descripcion contenido contenga "positivo"
tipos_eliminados = TipoSangre.objects.filter(descripcion__iendswith="positivo").delete()
cargo = Cargo.objects.get(id=3)
cargo.delete()
# Equivalente en lenguaje sql
    #DELETE FROM "core_tiposangre" WHERE "core_tiposangre"."descripcion" ILIKE '%positivo%'
    #DELETE FROM "core_cargo" WHERE "core_cargo"."id" = 3
