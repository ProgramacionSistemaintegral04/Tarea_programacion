from servicio import Servicio

class CorteCabello(Servicio):
    """Servicio especializado - Corte de cabello."""
    
    def calcular_costo(self, duracion: float) -> float:
        return self.costo_base * (duracion / 30)  # Por cada 30 minutos
    
    def describir(self) -> str:
        return f"Corte de cabello - ${self.costo_base}/30min"
    
    def validar_parametros(self, **kwargs) -> bool:
        return 'duracion' in kwargs and kwargs['duracion'] > 0

class Tinte(Servicio):
    """Servicio especializado - Tinte."""
    
    def __init__(self, nombre: str, costo_base: float, tipo_tinte: str):
        super().__init__(nombre, costo_base)
        self._tipo_tinte = tipo_tinte
    
    def calcular_costo(self, duracion: float) -> float:
        return self.costo_base + (duracion * 5)  # Costo fijo + por minuto
    
    def describir(self) -> str:
        return f"Tinte {self._tipo_tinte} - ${self.costo_base} + $5/min"
    
    def validar_parametros(self, **kwargs) -> bool:
        return ('duracion' in kwargs and kwargs['duracion'] > 0 and 
                'tipo_tinte' in kwargs)

class Manicura(Servicio):
    """Servicio especializado - Manicura."""
    
    def calcular_costo(self, duracion: float) -> float:
        return self.costo_base + (duracion * 3)
    
    def describir(self) -> str:
        return f"Manicura profesional - ${self.costo_base} + $3/min"
    
    def validar_parametros(self, **kwargs) -> bool:
        return 'duracion' in kwargs and 30 <= kwargs['duracion'] <= 90