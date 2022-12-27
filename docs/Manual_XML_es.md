



# XML
  
Open XML files to get data.  
  
![banner](imgs/Banner_XML.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Carga archivo XML
  
Carga datos de un archivo XML en memoria
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo XML||C:/Users/usuario/Desktop/archivo.xml|
|XML como texto||<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type='text/xsl'?> 
<Users>
	<User>
	<Name>User 1</Name>
	<Surname>Test</Surname>
	<Country>USA</Country>
	<Company>Acme</Company>
	</User>
</Users>|
|Codificación||latin-1|
|Asignar resultado a variable||Variable|
|ID Sesión||Default|

### Insertar Nodo
  
Inserta un nodo en el XML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión||Default|
|Expresión Xpath||//|
|Nombre de Nodo||Nombre|
|Dato del Nodo||data|
|Si existe el nodo|Seleccione la acción a realizar si el nodo ya existe||
|Ubicación de la inserción|Seleccione la ubicación donde se realizara la inserción||
|Nombre de un nodo hijo||nodo (Opcional)|
|Namespaces (opcional)||{'namespace': 'http://.example.com'}|
|Asignar resultado a variable||Variable|

### Obtener Nodo
  
Obtiene informacion de un nodo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión||Default|
|Múltiples nodos?||False|
|Expresión Xpath||//|
|Atributo (Opcional)||attr|
|Namespaces (opcional)||{'namespace': 'http://.example.com'}|
|Asignar resultado a variable||Variable|

### Modificar Nodo
  
Modificar un nodo en el XML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión||Default|
|Expresión Xpath||//|
|Nuevo Valor||Valor|
|Atributo(s)||Disable=True, other_attribute="attributeOk"|
|Namespaces (opcional)||{'namespace': 'http://.example.com'}|
|Asignar resultado a variable||Variable|

### Borrar Nodo
  
Borra un Nodo a partir de un XPath
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión||Default|
|Expresión Xpath||//|
|Namespaces (opcional)||{'namespace': 'http://.example.com'}|
|Asignar resultado a variable||Variable|

### Guarda archivo XML
  
Guarda datos en un archivo XML
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo XML||C:/Users/usuario/Desktop/archivo.xml|
|Asignar resultado a variable||Variable|
|ID Sesión||Default|

### Termina sesión XML
  
Quita una sesión de XML y libera memoria
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Sesión||Default|
