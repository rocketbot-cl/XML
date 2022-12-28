# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import sys
import os
import json
from xml.etree import ElementTree as ET

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'XML' + os.sep + 'libs' + os.sep
if not cur_path in sys.path:
    sys.path.append(cur_path)

# Imports from module libs here.
import xmltodict
# Globals declared here.
global mod_xml_sessions
# Defaults declared here.
SESSION_DEFAULT = "default"

# Initialize settings for the module here.

try:
    if not mod_xml_sessions :
        mod_xml_sessions = {SESSION_DEFAULT:{}}
except NameError:
    mod_xml_sessions = {SESSION_DEFAULT:{}}


"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

try:

    if module == "xmlsession":
 """ 
        XML Session: Open session, read xml from file or text
        """
        path = GetParams('path')
        var_ = GetParams('result')
        encoding = GetParams('encoding')
        session = GetParams('session')
        xml_ = GetParams('xml')
        
        if not session:
            session = SESSION_DEFAULT

        if not encoding:
            encoding = "latin-1"

        mod_xml_sessions[session]={'path': path}
        if path:
            with open(path, encoding=encoding) as fd:
                xml = fd.read()        
        else:
            xml = xml_
        mod_xml_sessions[session]['data'] = ET.fromstring(xml)
        try:
            mod_xml_sessions[session]['namespaces'] = dict([node for _, node in ET.iterparse(path, events=['start-ns'])])
        except:
            pass
        
        if var_:
            #Convert only if required
            doc = xmltodict.parse(xml)
            SetVar(var_, json.loads(json.dumps(doc)))

    if module == "xmlsessionend":
        """
        XML Session end: Remove from sessions a XML
        """
        session = GetParams('session')
        if not session:
            session = SESSION_DEFAULT
        if session in mod_xml_sessions:
            del mod_xml_sessions[session]
            if session == SESSION_DEFAULT:
                mod_xml_sessions[SESSION_DEFAULT] = {}
        else:
            raise Exception("The session you want to delete does not exist")
    
    if module == "xmlgetnode":
        """
        XML Get Node: get data from xml node
        """
        var_ = GetParams('result')
        attribute = GetParams('attribute')
        session = GetParams('session')
        xpath = GetParams('xpath')
        multiple = GetParams('multiple')
        namespaces_ = GetParams('namespaces')

        if namespaces_:
            namespaces_ = eval(namespaces_)
            if not isinstance(namespaces_, dict):
                raise Exception ("Namespaces must be a dictionary.")
        else:
            namespaces_ = None
        
        # Set Default session
        if not session:
            session = SESSION_DEFAULT

        if not 'data' in mod_xml_sessions[session]:
            # Remember set session
            raise Exception('The session no exists')
        root_xml = mod_xml_sessions[session]['data']
        if multiple and multiple == 'True':
            res = []
            tmp = root_xml.findall(xpath, namespaces=namespaces_)
            data_dict = {}
            if attribute:
                for item in tmp:
                    res.append(item.attrib[attribute])
            else:
                for child in tmp:
                    for little_child in child:
                        data_dict[little_child.tag] = little_child.text
                    res.append(data_dict)

        else:
            tmp = root_xml.find(xpath, namespaces=namespaces_)
            
            if not xpath:
                tmp = root_xml
            if attribute:
                res = tmp.attrib[attribute]
            else:
                res = tmp.text
        
        SetVar(var_, res)

    if module == "xmlinsertnode":
        """
        XML Insert Node: add new node to XML
        """
        var_ = GetParams('result')
        node = GetParams('node')
        value = GetParams('value')
        if_exist = GetParams('if_exist')
        specified = GetParams('specified')
        session = GetParams('session')
        xpath = GetParams('xpath')
        location = GetParams('location')
        namespaces_ = GetParams('namespaces')

        if namespaces_:
            namespaces_ = eval(namespaces_)
            if not isinstance(namespaces_, dict):
                raise Exception ("Namespaces must be a dictionary.")
        else:
            namespaces_ = None

        res = None
        location_ = 0
        
        add_ = True
        overwrite = False
        node_exist = False

        # Set Default session
        if not session:
            session = SESSION_DEFAULT

        if not 'data' in mod_xml_sessions[session]:
            # Remember set session
            raise Exception('The session no exists')
        if not node or len(node) < 1:
            # Node name undefined
            raise Exception("Node name undefined")

        if  location and len(location) > 1:
            # Default location
            if location == "beging":
                location_ = 0
            elif location == "end":
                if mod_xml_sessions[session]['data'].find(xpath, namespaces=namespaces_):
                    location_ = len(mod_xml_sessions[session]['data'].find(xpath, namespaces=namespaces_))

            elif location in ["before", "after"]:
                for i in mod_xml_sessions[session]['data'].find(xpath, namespaces=namespaces_):
                    if i.tag == specified:
                        break
                    location_ = location_ + 1
                if location == "after":                   
                    location_ = location_ + 1

        node_exist = len(mod_xml_sessions[session]['data'].findall(xpath + "/" + node, namespaces=namespaces_)) > 0
        
        if if_exist and len(if_exist) > 0:
            if if_exist == "skip":
                add_ = False
                overwrite = False
            elif if_exist == "overwrite":
                add_ = False
                overwrite = True

        item = ET.Element(node)
        if value and len(value) > 0:
            item.text = value
        
        if add_ or not node_exist:
            try:
                mod_xml_sessions[session]['data'].find(xpath, namespaces=namespaces_).insert(location_,item)
            except Exception as e:
                SetVar(var_, False)
                raise e
        if overwrite and node_exist:
            mod_xml_sessions[session]['data'].find(xpath + "/" + node, namespaces=namespaces_).text = value

        res = json.dumps(xmltodict.parse(ET.tostring(mod_xml_sessions[session]['data']).decode()))
        
        if var_:
            SetVar(var_, res)

    if module == "xmlupdatenode":
        """
        XML update Node: update node and attribs to XML
        """
        var_ = GetParams('result')        
        session = GetParams('session')
        xpath = GetParams('xpath')
        data = GetParams('data')
        attr_ = GetParams('attr')
        namespaces_ = GetParams('namespaces')

        if namespaces_:
            namespaces_ = eval(namespaces_)
            if not isinstance(namespaces_, dict):
                raise Exception ("Namespaces must be a dictionary.")
        else:
            namespaces_ = None
        
        res = None        
        
        # Set Default session
        if not session:
            session = SESSION_DEFAULT

        if not 'data' in mod_xml_sessions[session]:
            # Remember set session
            raise Exception('The session no exists')
        
        item = mod_xml_sessions[session]['data'].find(xpath, namespaces=namespaces_)
        if item != None:
            mod_xml_sessions[session]['data'].find(xpath, namespaces=namespaces_).text = data
            if attr_ and len(attr_) > 1 and "=" in attr_:
                att = attr_.split(",")
                for at in att:
                    mod_xml_sessions[session]['data'].find(xpath).attrib[at.split("=")[0]]=at.split("=")[1]  
        if var_:
            res = json.dumps(xmltodict.parse(ET.tostring(mod_xml_sessions[session]['data']).decode()))
            SetVar(var_, res)

    if module == "xmldeletenode":
        """
        XML Delete Node: Delete node  XML
        """
        var_ = GetParams('result')        
        session = GetParams('session')
        xpath = GetParams('xpath')
        namespaces_ = GetParams('namespaces')

        if namespaces_:
            namespaces_ = eval(namespaces_)
            if not isinstance(namespaces_, dict):
                raise Exception ("Namespaces must be a dictionary.")
        else:
            namespaces_ = None
        
        res = None        
        
        # Set Default session
        if not session:
            session = SESSION_DEFAULT

        if not 'data' in mod_xml_sessions[session]:
            # Remember set session
            raise Exception('The session no exists')
        
        item = mod_xml_sessions[session]['data'].find(xpath, namespaces=namespaces_)
        root = mod_xml_sessions[session]['data']
        global xml_iterator
        def xml_iterator(parents, nested, item):
            for child in reversed(parents):
                if nested:
                    if len(child) >= 1:
                        xml_iterator(child,nested, item)
                if child == item:  # Add your entire condition here
                    parents.remove(child)
                    del child
            
        xml_iterator(root,True, item)

        if var_:
            res = json.dumps(xmltodict.parse(ET.tostring(mod_xml_sessions[session]['data']).decode()))
            SetVar(var_, res)

    if module == 'xmlsave':
        path = GetParams('path')
        var_ = GetParams('result')
        session = GetParams('session')
        if not session:
            session = SESSION_DEFAULT
        
        res = True
        SetVar(var_, res)
        try:
            if not 'data' in mod_xml_sessions[session]:
                raise Exception('The session no exists')
            root_xml = mod_xml_sessions[session]['data']
            enc_ = "utf-8"
            
            namespaces = mod_xml_sessions[session].get('namespaces', None)
            if namespaces:
                for ns, url in namespaces.items():
                    ET.register_namespace(ns, url)
            
            b_xml = ET.tostring(root_xml, enc_)
            with open(path, "wb") as f: 
                f.write(b_xml)

        except Exception as e:
            res = False
            SetVar(var_, res)
            raise e


except Exception as e:
    PrintException()
    raise e
