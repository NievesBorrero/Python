class Cancion (object):
	titulo  = ""
	autor= ""
	duracion = 0

	def __init__ (self, titulo, autor):
		self.titulo = titulo;
		self.autor = autor;

	def dameTitulo(self):
		self.titulo = raw_input("Introduce el titulo");

	def dameAutor(self):
		self.autor = raw_input("Introduce el autor");

	def pon_titulo(self, titulo):
		self.titulo=titulo;

	def pon_autor(self, autor):
		self.autor= autor;

miCancion= Cancion ("Lija y Terciopelo", "Marea")


print 'Titulo: ', miCancion.titulo
print 'Autor: ', miCancion.autor

miCancion.dameTitulo()
miCancion.dameAutor()


print 'Titulo: ', miCancion.titulo
print 'Autor: ', miCancion.autor

miCancion.pon_titulo("hola")
miCancion.pon_autor("caracola")

print 'Titulo: ', miCancion.titulo
print 'Autor: ', miCancion.autor