Clinica Mateos: Es una web realizada en Django.
Para poder correr el trabajo usar python manage.py runserver. 
Ya dentro de la web, te encontrás con la página de inicio donde se visualiza la bienvenida a la página y arriba podés ir a la página que necesites. 
Las páginas disponibles son:
Pacientes: en la página podés registrarte en nuestra base de datos o ir a la opción que está disponible para sacar un turno, la opción que elijas te estará abriendo el formulario correspondiente.
Turnos: acá podés sacar un turno o buscar el turno que ya tenías reservado mediante tu DNI.
Médicos: muestra los médicos que hay disponibles en la clínica y si sos un profesional que trabaja con nosotros y no estás en la lista, te podés agregar.
Para esto se crearon las plantillas para ingresar datos mediante herencia de la plantilla inicio. Se utilizó el método POST para poder ingresar los datos y el método GET para poder buscar la información.
Desde el panel de administración se pueden agregar o eliminar registros.
