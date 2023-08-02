from lxml import etree

raiz = etree.Element("bookstore")


book = etree.SubElement(raiz, "book")

title = etree.SubElement(book, "title")

title.text = "ola"

with open("livros.xml", "wb") as file:
   file.write(etree.tostring(raiz, pretty_print=True))



print(etree.tostring(raiz, pretty_print=True))

