



# XML
  
Abre archivos XML para extrer informacion.  
  
![banner](https://raw.githubusercontent.com/rocketbot-cl/XML/master/docs/imgs/Banner_XML.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.
## Como usar este module
  
Eiusmod veniam ut nisi minim in. Do et deserunt eiusmod veniam sint aliqua nulla adipisicing laboris voluptate fugiat 
ullamco elit do. Sint amet cillum fugiat excepteur mollit voluptate reprehenderit nisi commodo sint minim.
## Descripción de los comandos

### Carga archivo XML
  
Carga datos de un archivo XML en memoria
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del XML|Seleccione el archivo XML a cargar|C:/Users/usuario/Desktop/archivo.xml|
|XML Text|Ingrese el texto del archivo XML|<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type='text/xsl'?> 
<Users>
	<User>
	<Name>User 1</Name>
	<Surname>Test</Surname>
	<Country>USA</Country>
	<Company>Acme</Company>
	</User>
</Users>|
|Codificación|Ingrese la codificación del archivo XML|latin-1|
|Asignar resultado a variable|Ingrese la variable donde se guardará el resultado|variable|
|ID Sesión|Sesión para multiples archivos|Default|

### Insertar Nodo
  
Inserta un nodo en el XML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión|Sesión para multiples archivos|Default|
|Expresión Xpath|Xpath que utilizaremos para buscar un nodo dentro del XML|//|
|Nombre de Nodo|Nombre del nodo que queremos insertar|Name|
|Dato del Nodo|Dato del nodo que queremos insertar|data|
|Si existe el nodo|Si el nodo ya existe, tendremos la opcion de insertar, pasar, sobreescribir||
|Ubicación de la inserción|Ubicación de la inserción del nodo||
|Nombre de un nodo especifico|Nombre del nodo especifico que queremos insertar|node|
|Asignar resultado a variable|Variable donde se guardará el resultado|variable|

### Obtener Nodo
  
Obtiene informacion de un nodo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión|ID de sesión para obtener el nodo|Default|
|Múltiples nodos?|¿Desea devolver un array con los nodos?||
|Expresión Xpath||//|
|Atributo (opcional)|Atributo de nodo a seleccionar|attr|
|Asignar resultado a variable|Variable donde se guardará el resultado|variable|

### Modificar Nodo
  
Modificar un nodo en el XML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión|ID de sesión para el archivo|Default|
|Expresión Xpath|Expresión xpath para el nodo|//|
|Nuevo Valor|Valor a actualizar|Dato|
|Atributo(s)|Atributos a actualizar|Disable=True, other_attribute="attributeOk"|
|Asignar resultado a variable|Variable donde se guardará el resultado|variable|

### Borrar Nodo
  
Borra un Nodo a partir de un XPath
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión|ID de la sesión|Default|
|Expresión Xpath|Expresión Xpath del nodo a eliminar|//|
|Asignar resultado a variable|Variable donde se guardará el resultado|variable|

### Guarda archivo XML
  
Guarda datos en un archivo XML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del XML|Ruta del archivo XML a guardar|C:/Users/usuario/Desktop/archivo.xml|
|Asignar resultado a variable|Variable donde se guardará el resultado|variable|
|ID Sesión|ID de sesión para multiples archivos|Default|

### Termina sesión XML
  
Quita una sesión de XML y libera memoria
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión|ID de la sesión XML|Default|
