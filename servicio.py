from abc import ABC, abstractmethod
from Entidad import Entidad

class Servicio(ABC):
    """Clase abstracta para servicios."""
    
    def __init__(self, nombre: str, costo_base: float):
        self._nombre = nombre
        self._costo_base = max(0, costo_base)
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def costo_base(self) -> float:
        return self._costo_base
    
    @abstractmethod
    def calcular_costo(self, duracion: float) -> float:
        """Calcula el costo del servicio - POLIMORFISMO."""
        pass
    
    @abstractmethod
    def describir(self) -> str:
        """Descripción del servicio."""
        pass
    
    @abstractmethod
    def validar_parametros(self, **kwargs) -> bool:
        """Valida parámetros específicos del servicio."""
        pass
    
    # MÉTODOS SOBRECARGADOS
    def calcular_costo_con_impuestos(self, duracion: float, impuesto: float = 0.21) -> float:
        costo = self.calcular_costo(duracion)
        return round(costo * (1 + impuesto), 2)
    
    def calcular_costo_con_descuento(self, duracion: float, descuento: float = 0.0) -> float:
        costo = self.calcular_costo(duracion)
        return round(costo * (1 - descuento), 2)
    
    def calcular_costo_completo(self, duracion: float, descuento: float = 0.0, 
                               impuesto: float = 0.21) -> float:
        costo = self.calcular_costo(duracion)
        costo = costo * (1 - descuento)
        costo = costo * (1 + impuesto)
        return round(costo, 2)