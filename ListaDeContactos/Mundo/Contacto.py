class Contacto:
    
    def __init__(self, nombre, apellido, direccion, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__correo = correo
        self.__telefono = []
        self.__palabra = []
    def darNombre(self):
        return self.__nombre
    def darApellido(self):
        return self.__apellido
    def darDireccion(self):
        return self.__direccion
    def darCorreo(self):
        return self.__correo
    def darTelefonos(self):
        return self.__telefono
    def darPalabras(self):
        return self.__palabra
    def cambiarDireccion(self, direccion):
        self.__direccion = direccion
        return "la direccion ha sido cambiada a: ", self.__direccion
    def cambiarCorreo(self, correo):
        self.__correo = correo
        return "el correo ha sido cambiado a: ", self.__correo
    def agregarTelefono(self, telefono):
        self.__telefono.append(telefono)
        return "se ha añadido el telefono: ", self.__telefono," al contacto de: ", self.darNombre()
    def eliminarTelefono(self,telefonoEliminar):
        eliminar = False
        for telefonoEliminar in self.__telefono:
            if telefonoEliminar:
                self.__telefono.remove(telefonoEliminar)
                eliminar = True
                break
        return eliminar
                
    def agregarPalabra(self, palabra):
        self.__palabra.append(palabra)
        return "se ha añadido la palabra:", palabra," al contacto de: ", self.darNombre()
    def eliminarPalabra(self, palabraEliminar):
        self.__palabra.remove(palabraEliminar)
    def contienePalabraClave(self, palabra):
        return palabra in self.__palabra
