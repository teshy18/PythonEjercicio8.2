import json


## se define la clase
class auto:

  def __init__(self, nombre, marca, tipo, color):
    self.nombre = nombre
    self.marca = marca
    self.tipo = tipo
    self.color = color

  def __str__(self):
    return 'nombre: ' + self.nombre + ', marca: ' + self.marca + ', tipo: ' + self.tipo + ', color: ' + self.color


##main
if __name__ == '__main__':
  ##se crea un objeto
  focus = auto('focus', 'ford', 'sedan', 'azul')

  ##print(focus) >> nombe: focus, marca: ford.......

  ##se crea un json don el objeto
  a1 = json.dumps(focus.__dict__, separators=(',', ':'), indent=2)

  ##se guarda el objeto en un archivo.json
  file = open('archivo.json', 'w')
  file.write(a1)
  file.close()

  ##se abre el archivo nuevamente y se carga el objeto
  file = open('archivo.json', 'r+')
  a2 = json.load(file)
  file.close()

  print(a2)
