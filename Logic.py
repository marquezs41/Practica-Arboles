import math

class Paciente:
    def __init__(self, id_paciente, genero, nombre, edad, triaje):
        self.id_paciente:int = id_paciente
        self.genero:str = genero
        self.nombre:str = nombre
        self.edad:int = edad
        self.triaje:int = triaje
        self.llegada:int = None 
    
    def __repr__(self):
        return f'Paciente({self.id_paciente}, {self.nombre}, {self.edad}, Triaje {self.triaje}, Llegada {self.llegada})'
    
    
class Node:

  def __init__(self, paciente:Paciente):
    self.paciente = paciente
    self.leftchild = None
    self.rightchild = None
    
class min_heap:
  
  def __init__(self):
    self.cola:Paciente = []
    self.orden = 0
  
  def print_recursivo(self, nodo):
    nivel = nodo
    hijoIzq = (nodo*2) + 1
    hijoDer = (nodo*2) + 2
    prefix = ''
    
    if nodo > 1:
      nivel = (math.floor(math.log2(nodo -1)))+1
    
    for i in range(nivel):
      prefix = prefix + '|--'
        
    print(prefix + str(self.cola[nodo]))
    
    if hijoIzq < len(self.cola):
      self.print_recursivo(hijoIzq)
      
    if hijoDer < len(self.cola):
      self.print_recursivo(hijoDer)
    
  def print_Tree(self):
    for i in range(len(self.cola)-1):
      print(self.cola[i])
  
  def consulta_Triaje(self, triaje):
    print("Pacientes con triaje " + str(triaje))
    for i in range(len(self.cola)-1):
      if self.cola[i].triaje == triaje:
        print(self.cola[i])
  
  
  def intercambiar(self, posicion1, posicion2):
    paciente = self.cola[posicion1]
    self.cola[posicion1] = self.cola[posicion2]
    self.cola[posicion2] = paciente
        
  def minHeap(self, posicion):
    padre = (posicion -1)//2
    
    if self.cola[padre].triaje > self.cola[posicion].triaje or (self.cola[padre].triaje == self.cola[posicion].triaje and self.cola[padre].llegada > self.cola[posicion].llegada):
      self.intercambiar(padre, posicion)
      if padre > 0:
        self.minHeap(padre)
    
  def minHeap_inverso(self, posicion):
    hijoIzq = (posicion*2) + 1
    hijoDer = (posicion*2) + 2
    hijoCambio = posicion
    
    if hijoDer < len(self.cola) and hijoIzq < len(self.cola) and  self.cola[hijoIzq].triaje == self.cola[hijoDer].triaje and self.cola[posicion].triaje > self.cola[hijoDer].triaje:
      if self.cola[hijoIzq].llegada > self.cola[hijoDer].llegada:
        hijoCambio = hijoDer
      else:
        hijoCambio = hijoIzq  
    elif hijoIzq < len(self.cola) and self.cola[hijoIzq].triaje < self.cola[posicion].triaje:
      hijoCambio = hijoIzq
    elif hijoDer < len(self.cola) and self.cola[hijoDer].triaje < self.cola[posicion].triaje:
      hijoCambio = hijoDer
    elif hijoIzq < len(self.cola) and self.cola[hijoIzq].triaje == self.cola[posicion].triaje and self.cola[hijoIzq].llegada < self.cola[posicion].llegada:
      hijoCambio = hijoIzq
    elif hijoDer < len(self.cola) and self.cola[hijoDer].triaje == self.cola[posicion].triaje and self.cola[hijoDer].llegada < self.cola[posicion].llegada:
      hijoCambio = hijoDer
      
    if hijoCambio != posicion:
      self.intercambiar(hijoCambio, posicion)
      self.minHeap_inverso(hijoCambio)
           
  def insert(self, paciente:Paciente):
    self.orden = self.orden + 1
    paciente.llegada = self.orden
    self.cola.append(paciente)
    
    self.minHeap(len(self.cola) -1)
  
  def proximoPaciente(self):
    print(self.cola[0])
  
  def eliminarNodo(self, posicion):
    if posicion == len(self.cola) -1:
      self.cola.pop(posicion)
    else:  
      self.intercambiar(posicion, len(self.cola) -1)
      self.cola.pop(len(self.cola) -1)
      self.minHeap_inverso(posicion)
        
  def atender(self):
    print("Atender el paciente: " + str(self.cola[0]))
    self.eliminarNodo(0)
    
  def eliminarPaciente_id(self, id):
    for i in range(len(self.cola)-1):
      if self.cola[i].id_paciente == id:
        print("Elimina paciente: " + str(self.cola[i]))
        self.eliminarNodo(i)
    
  def eliminarPaciente_nombre(self, nombre):
    for i in range(len(self.cola)-1):
      if self.cola[i].nombre == nombre:
        print("Elimina paciente: " + str(self.cola[i]))
        self.eliminarNodo(i)
    
    
"""
tree.print_recursivo(0)
print("Total pacientes " + str(len(tree.cola)))

tree.consulta_Triaje(2)

tree.eliminarPaciente_id(32456)
tree.print_recursivo(0)

tree.eliminarPaciente_nombre("sofia")
tree.print_recursivo(0)
"""

