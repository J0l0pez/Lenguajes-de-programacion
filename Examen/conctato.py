def agregar_contacto(self, contacto):
    self.contactos.append(contacto)
    print("Contacto agregado")

def mostrar_contactos(self):
    if not self.contactos:
        print("No hay contactos")
    else:
        print("Lista de contactos:")
        for contacto in self.contactos:
            print("Nombre: ", contacto.nombre)
            print("Teléfono: ", contacto.telefono)
            print("-" * 20)