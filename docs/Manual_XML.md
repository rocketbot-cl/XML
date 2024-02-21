



# XML
  
Open XML files to get data.  

*Read this in other languages: [English](Manual_XML.md), [Português](Manual_XML.pr.md), [Español](Manual_XML.es.md)*
  
![banner](imgs/Banner_XML.png o jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Load XML File
  
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

### Dictionary to XML File
  
Convert a python dictionary into a XML file
|Parameters|Description|example|
| --- | --- | --- |
|Dictionary||dictionary|
|XML file path||C:/Users/usuario/Desktop/archivo.xml|
|Encoding||latin-1|
|Assign result to variable||Variable|
