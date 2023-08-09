from lxml import etree

arquivo = "biblioteca.xml"

parser = etree.XMLParser(dtd_validation=True)

try: 
   etree.parse(arquivo, parser)
   print("Documento válido")
except Exception as error:
   print("Documento inválido")
   print(error)