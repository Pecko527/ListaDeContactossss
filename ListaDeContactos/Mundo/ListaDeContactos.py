from Mundo.Contacto import Contacto


class ListaDeContactos:
    def __init__(self):
        self.lista = []
        
    def darTodosLosContactos(self):
        contactos = []
        for contacto in self.lista:
            contactos.append(contacto.darNombre() + " " + contacto.darApellido())
        return contactos
    def buscarContactosPalabraClave(self, palabra):
        ListaDeContactos = []
        for contacto in self.lista:
            if palabra == contacto.darPalabras():
                ListaDeContactos.append(contacto.darNombre() + " " + contacto.darApellido())
        return ListaDeContactos

    def buscarContacto(self, nombre, apellido):
        for contacto in self.lista:
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
        return None
    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        contacto = Contacto(nombre, apellido, direccion, correo)
        contacto.agregarTelefono(telefonos)
        contacto.agregarPalabra(palabras)
        self.lista.append(contacto)
    def eliminarContacto(self, nombre, apellido):
        borrado=False
        for contacto in self.lista:
            if nombre == contacto.darNombre() and apellido == contacto.darApellido():
                self.lista.remove(contacto)
                borrado = True
                break
        return borrado
    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        modificado=False
        for contacto in self.lista:
            if nombre == contacto.darNombre() and apellido == contacto.darApellido():
                contacto.cambiarDireccion(direccion)
                contacto.cambiarCorreo(correo)
                for tel in contacto.darTelefonos():
                    contacto.eliminarTelefono(tel)
                for telefono in telefonos:
                    contacto.agregarTelefono(telefono)
                for palabra in contacto.darPalabras():
                    contacto.eliminarPalabra(palabra)
                for palabra in palabras:
                    contacto.agregarPalabra(palabra)
                modificado = True
        return modificado
            
    def actualizarTelefonos(self, telefonos, contacto):
         for telefono in telefonos:
            contacto.__telefono.clear()
            contacto.agregarTelefono(telefono)

    def actualizarPalabras(self, palabras, contacto):
        for palabra in palabras:
            contacto.__palabra.clear()
            contacto.agregarPalabra(palabra)
    #def metodo1(self):

    #def metodo2(self):
    
    
