import xml.etree.ElementTree as ET

tree = ET.parse('filmes.xml')
root = tree.getroot()

for filmes in root:
    #print(filmes)
    print(filmes.attrib['id'])
    for coisa in filmes:
        if coisa.tag == 'diretor' and coisa.text == 'Roger Allers':
            print(f' > {coisa.tag.capitalize()}:{coisa.text}')
            root.remove(filmes)
        #print(f' > {coisa.tag.capitalize()}:{coisa.text}')
    print()
tree.write('filmes.xml')