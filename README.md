<a name="br1"></a> 

**UNIVERSIDAD AUTÓNOMA DE CHIHUAHUA**

CÓMPUTO PARALELO Y

DISTRIBUIDO

**Proyecto 2a. Evaluación**

**Nombres**:

331206 - Miguel Ángel Abundis Medina

353198 - Diego Alejandro Martínez González

348411 - Ramón Reyna García

**Profesor**: De Lira Montes Jose Saul



<a name="br2"></a> 

**Link Repositorio Github:**

[**https://github.com/DiegoMTZGlz/proy2CPD**](https://github.com/DiegoMTZGlz/proy2CPD)

**Scripts:**

Para empezar tenemos dos contenedores, ambos con la base de datos de ORACLE, los

cuales están dentro de una red de docker llamada oracle\_net

El primer script a ejecutar fue el de la base de datos OE, el cual tal cual es corrido en la

base de datos del servidor A

luego creamos un datalink hacia el server B

luego fragmentamos la tabla de customers creando otra tabla que contenga solo los de

región A y B

creamos la vista para mostrar todos los customers tanto del servidor A como del B



<a name="br3"></a> 

al igual que en el servidor A en el B ejecutamos el script OE pero con la diferencia que la

única operación extra es crear su fragment con los customers de región C y D

A partir de ahora todos los script son creados en el servidor A, de los cuales empezamos

con la capa de transparencia:

Creamos los triggers los cuales al ejecutarse una operación en el servidor A se replicará en

el servidor B a excepción de la tabla de customers



<a name="br4"></a> 



<a name="br5"></a> 

Después tenemos el script que crea los procedimientos almacenados, que es básicamente

el CRUD para cada tabla que tenemos exceptuando customers:



<a name="br6"></a> 

etc.



<a name="br7"></a> 

Para seguir con el CRUD de customers qué es un poco diferente ya que contiene

condicionales para saber si se almacenará un usuario en el servidor A o B, así como su

edición:

así sucesivamente con todas las operaciones CRUD



<a name="br8"></a> 

**Funcionamiento:**

tenemos una ventana la cual contiene varias opciones, en ellas tenemos las 4 tablas al

superior y debajo sus operaciones crud correspondientes

en el apartado de BUSCAR tenemos toda la lista de registros de la tabla en la base de

datos



<a name="br9"></a> 

para ACTUALIZAR tenemos un campo de ID el cual ingresamos un id a modificar y en el

botón buscar nos llenará los otros campos con la información de ese id

por último para eliminar tenemos solo el campo de ID, con el cuál buscará el usuario



<a name="br10"></a> 

Al querer eliminar nos saldrá un recuadro con los datos del campo a eliminar, de no ser así

saltará la leyenda de registro no encontrado

Las mismas operaciones son similares para las otras tablas solo cambiando algunos inputs

Todos los campos han sido validados con sus correspondientes tipo de datos y longitud

