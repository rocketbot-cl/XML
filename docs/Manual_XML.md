



# XML
  
Abre archivos XML para extrer informacion.  
  
![banner](imgs/Banner_XML.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Load XML Fil
  
Load data from an XML file into memory
|Parameters|Description|example|
| --- | --- | --- |
|XML file path||C:/Users/usuario/Desktop/archivo.xml|
|XML as text||<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type='text/xsl'?> 
<Users>
	<User>
	<Name>User 1</Name>
	<Surname>Test</Surname>
	<Country>USA</Country>
	<Company>Acme</Company>
	</User>
</Users>|
|Encoding||latin-1|
|Assign result to variable||Variable|
|Session ID||Default|

### Insert Node
  
Insert node on XML
|Parameters|Description|example|
| --- | --- | --- |
|Session ID||Default|
|Xpath expression||//|
|Node name||Name|
|Nodo data||data|
|If node name present then|Select the action to perform if the node already exists||
|Insertion location|Select the location where the insertion will be made||
|Specified child node name||node (Optional)|
|Namespaces (optional)||{'namespace': 'http://.example.com'}|
|Assign result to variable||Variable|

### Get Node
  
Obtain node data
|Parameters|Description|example|
| --- | --- | --- |
|Session ID||Default|
|Multiple nodes?||False|
|Xpath expression||//|
|Attribute (Optional)||attr|
|Namespaces (optional)||{'namespace': 'http://.example.com'}|
|Assign result to variable||Variable|

### Update Node
  
Update node on XML
|Parameters|Description|example|
| --- | --- | --- |
|Session ID||Default|
|Xpath expression||//|
|New Value||Value|
|Attribute(s)||Disable=True, other_attribute="attributeOk"|
|Namespaces (optional)||{'namespace': 'http://.example.com'}|
|Assign result to variable||Variable|

### Delete Node
  
Delete node by XPath
|Parameters|Description|example|
| --- | --- | --- |
|Session ID||Default|
|Xpath expression||//|
|Namespaces (optional)||{'namespace': 'http://.example.com'}|
|Assign result to variable||Variable|

### Save XML File
  
Save XML File
|Parameters|Description|example|
| --- | --- | --- |
|XML file path||C:/Users/usuario/Desktop/archivo.xml|
|Assign result to variable||Variable|
|Session ID||Default|

### End XML Session
  
Remove an xml session from memory
|Parameters|Description|example|
| --- | --- | --- |
|Session ID||Default|
