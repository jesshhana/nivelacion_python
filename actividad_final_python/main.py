from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class SistemaGPS:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion

    def mostrar_ubicacion(self):
        return f"Ubicación actual: {self.ubicacion}"


class SistemaAudio:
    def __init__(self, volumen):
        self.volumen = volumen

    def subir_volumen(self):
        self.volumen += 1
        return f"Volumen aumentado a {self.volumen}"


class VehiculoInteligente(Vehiculo, SistemaGPS, SistemaAudio):
    def __init__(self, marca, modelo, ubicacion, volumen, velocidad):
        Vehiculo.__init__(self, marca, modelo)
        SistemaGPS.__init__(self, ubicacion)
        SistemaAudio.__init__(self, volumen)

        self.__velocidad = velocidad  

    def encender(self):
        return f"El vehículo {self.marca} {self.modelo} ha sido encendido."

    def __str__(self):
        return f"{self.marca} {self.modelo} - Velocidad: {self.__velocidad} km/h"

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        if nueva_velocidad >= 0 and nueva_velocidad <= 200:
            self.__velocidad = nueva_velocidad
        else:
            print(" Velocidad inválida. Debe estar entre 0 y 200.")



if __name__ == "__main__":

    v1 = VehiculoInteligente("Toyota", "Corolla", "Riohacha", 10, 60)
    v2 = VehiculoInteligente("Mazda", "3", "Maicao", 15, 80)
    v3 = VehiculoInteligente("Chevrolet", "Spark", "Santa Marta", 8, 40)

    # Polimorfismo
    print(v1.encender())
    print(v2.encender())
    print(v3.encender())

    print(v1)
    print(v2)
    print(v3)

    print(v1.mostrar_ubicacion())
    print(v2.mostrar_ubicacion())
    print(v3.mostrar_ubicacion())

    
    print(v1.subir_volumen())
    print(v2.subir_volumen())

    # Encapsulamiento
    print("Velocidad actual:", v1.velocidad)

    v1.velocidad = 120
    print("Nueva velocidad:", v1.velocidad)

    v1.velocidad = 300  

  