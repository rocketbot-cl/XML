



# XML
  
Open XML files to get data.  
  
![banner](imgs/Banner_XML.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Descrição do comando

### Carregar arquivo XML
  
Carregar dados de um arquivo XML na memória
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo XML||C:/Users/usuario/Desktop/archivo.xml|
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
|Codificação||latin-1|
|Atribuir resultado à variável||Variável|
|ID Sessão||Default|

### Inserir Nó
  
Inserir um nó no XML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão||Default|
|Expressão Xpath||//|
|Nome do nó||Nome|
|Dados do nó||data|
|Se o nó existir|Selecione a ação a ser executada se o nó já existir||
|Local de inserção|Selecione o local onde será feita a inserção||
|Nome de um nó filho||nó (Opcional)|
|Namespaces (opcional)||{'namespace': 'http://.example.com'}|
|Atribuir resultado à variável||Variável|

### Obter Nó
  
Obter informações de um nó
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão||Default|
|Vários nós?||False|
|Expressão Xpath||//|
|Atributo (Opcional)||attr|
|Namespaces (opcional)||{'namespace': 'http://.example.com'}|
|Atribuir resultado à variável||Variável|

### Modificar Nó
  
Modificar um nó no XML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão||Default|
|Expressão Xpath||//|
|Novo Valor||Valor|
|Atributo(s)||Disable=True, other_attribute="attributeOk"|
|Namespaces (opcional)||{'namespace': 'http://.example.com'}|
|Atribuir resultado à variável||Variável|

### Excluir Nó
  
Excluir um nó de um XPath
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão||Default|
|Expressão Xpath||//|
|Namespaces (opcional)||{'namespace': 'http://.example.com'}|
|Atribuir resultado à variável||Variável|

### Salvar arquivo XML
  
Salvar dados em um arquivo XML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo XML||C:/Users/usuario/Desktop/archivo.xml|
|Atribuir resultado à variável||Variável|
|ID Sessão||Default|

### Terminar sessão XML
  
Remove uma sessão XML e libera memória
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID Sessão||Default|
