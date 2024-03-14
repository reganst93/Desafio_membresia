# Importando
from abc import ABC, abstractmethod

#Definicion de la clase base abstracta Membresia
class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Constructor de la clase Membresia.

        Args:
            correo_suscriptor (str): Correo electrónico del suscriptor.
            numero_tarjeta (str): Número de tarjeta del suscriptor.
        """
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        """
        Método getter para el correo electrónico del suscriptor.

        Returns:
            str: Correo electrónico del suscriptor.
        """
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        """
        Método getter para el número de tarjeta del suscriptor.

        Returns:
            str: Número de tarjeta del suscriptor.
        """
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
         """
        Método abstracto para cambiar la suscripción a un tipo de membresía diferente.

        Args:
            nueva_membresia (int): Número que representa el tipo de membresía deseada.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        """
        Método protegido para crear una nueva instancia de membresía según el tipo especificado.

        Args:
            nueva_membresia (int): Número que representa el tipo de membresía deseada.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

#Definicion de la clase gratis que hereda de Membresia
class Gratis(Membresia):
    costo = 0
    cantidad_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Método para cambiar la suscripción a un tipo de membresía diferente para Gratis.

        Args:
            nueva_membresia (int): Número que representa el tipo de membresía deseada.

        Returns:
            Membresia: Objeto de la nueva membresía o la misma Gratis si la selección es inválida.
        """
        #Si la selección es inválida, se mantiene la membresía actual
        else:
        if nueva_membresia < 1 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

#Definicion de la clase Basica que hereda de Membresia
class Basica(Membresia):
    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
         """
        Constructor de la clase Basica.

        Args:
            correo_suscriptor (str): Correo electrónico del suscriptor.
            numero_tarjeta (str): Número de tarjeta del suscriptor.
        """
        super().__init__(correo_suscriptor, numero_tarjeta)
        # Asignación de días de regalo según el tipo de membresía
        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7

        elif isinstance(self, Pro):
            self.__dias_regalo = 15

    def cancelar_suscripcion(self):
         """
        Método para cancelar la suscripción y cambiar a una membresía Gratis.

        Returns:
            Gratis: Objeto de la membresía Gratis con los mismos datos del suscriptor.
        """
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Método para cambiar la suscripción a un tipo de membresía diferente para Basica.

        Args:
            nueva_membresia (int): Número que representa el tipo de membresía deseada.

        Returns:
            Membresia: Objeto de la nueva membresía o la misma Basica si la selección es inválida.
        """
        # Si la selección es inválida, se mantiene la membresía actual
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

#Definicion de la clase Familiar que hereda de Basica
class Familiar(Basica):
    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Método para cambiar la suscripción a un tipo de membresía diferente para Familiar.

        Args:
            nueva_membresia (int): Número que representa el tipo de membresía deseada.

        Returns:
            Membresia: Objeto de la nueva membresía o la misma Familiar si la selección es inválida.
        """
        # Si la selección es inválida, se mantiene la membresía actual
        if nueva_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        """
        Método para modificar el control parental (no implementado).
        """
        pass

#Definicion de la clase SinConexion que hereda de Basica
class SinConexion(Basica):
    costo = 3500

    def cambiar_suscripcion(self, nueva_membresia: int):
          """
        Método para cambiar la suscripción a un tipo de membresía diferente para SinConexion.

        Args:
            nueva_membresia (int): Número que representa el tipo de membresía deseada.

        Returns:
            Membresia: Objeto de la nueva membresía o la misma SinConexion si la selección es inválida.
        """
        # Si la selección es inválida, se mantiene la membresía actual
        if nueva_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_maxima_offline(self):
         """
        Método para incrementar la cantidad máxima de contenido disponible para ver sin conexión (no implementado).
        """
        pass

#Definicion de la clase Pro que hereda de Familiar y de SinConexion
class Pro(Familiar, SinConexion):
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Método para cambiar la suscripción a un tipo de membresía diferente para Pro.

        Args:
            nueva_membresia (int): Número que representa el tipo de membresía deseada.

        Returns:
            Membresia: Objeto de la nueva membresía o la misma Pro si la selección es inválida.
        """
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

#Creacion de instancias de membresias y pruebas
g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))
