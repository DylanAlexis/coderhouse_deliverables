Clases:
	Curso:
		•id
		•Título
		•Duración
	Profesor:
		•id
		•Nombre
		•Apellido
		•Edad
		•eMail
		•Curso (Curso.id = foreign key)
	Alumno:
		•id
		•Nombre
		•Apellido
		•Edad
		•eMail
		•Profesor (Profesor.id = foreign key)
		•Curso (Curso.id = foreign key)

Al ingresar se depliega el template de inicio.
En la barra de navegación se encuentran 4 botones, I. el primero de etiqueta "CODERHOUSE" en la esquina superior izquierda lleva a al principio de la página en caso de estar en el
index, o al propio template index en caso de estar en otro template. II. En la esquina superior derecha se encuentran los botones hacia las clases Cusos, profesores y
alumnos.
En el header se localizan 2 botones, uno de etiqueta "Registrarse" que abre el template "updateForm" que ingresa nuevos datos a la tabla "alumnos" de la base de datos,
el segundo de etiqueta "Buscar curso" abre el template "readForm" que buscar los datos coincidentes con la palabre clave agregada al formulario en la tabla "Curso"
de la base de datos.
Al registrarse un nuevo alumno, los campos asociados a foreign keys, curso y profesor, se llenarán por defecto con las id's correspondientes al valor "none" en la base
de datos.

Cuenta admin:
Usuario: coder
Contraseña: 123coder 