



# XML
  
Abra arquivos XML para obter dados.  

*Read this in other languages: [English](Manual_XML.md), [Português](Manual_XML.pr.md), [Español](Manual_XML.es.md)*
  
![banner](imgs/Banner_XML.png o jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


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

### Dicionário para arquivo XML
  
Converta um dicionário python em um arquivo XML
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dicionário||dictionary|
|Caminho do arquivo XML||C:/Users/usuario/Desktop/archivo.xml|
|Codificação||latin-1|
|Atribuir resultado à variável||Variável|
