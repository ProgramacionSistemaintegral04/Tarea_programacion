from Entidad import Entidad
from cliente import Cliente
from servicio import Servicio
from servicios_especializados import CorteCabello, Tinte, Manicura
from datetime import datetime, timedelta
from enum import Enum
from Logger import Logger

class EstadoReserva(Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    COMPLETADA = "completada"

class Reserva(Entidad):
    """Clase Reserva con manejo completo de estados y excepciones."""
    
    def __init__(self, cliente: Cliente, servicio: Servicio, 
                 duracion: float, fecha: datetime):
        super().__init__()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._fecha = fecha
        self._estado = EstadoReserva.PENDIENTE
        self._costo_total = 0.0
        
        if not self._validar():
            raise ValueError(f"Reserva inválida: {self._servicio.nombre}")
    
    @property
    def cliente(self) -> Cliente:
        return self._cliente
    
    @property
    def servicio(self) -> Servicio:
        return self._servicio
    
    @property
    def duracion(self) -> float:
        return self._duracion
    
    @property
    def fecha(self) -> datetime:
        return self._fecha
    
    @property
    def estado(self) -> EstadoReserva:
        return self._estado
    
    @property
    def costo_total(self) -> float:
        return self._costo_total
    
    def confirmar(self) -> bool:
        try:
            if self._estado != EstadoReserva.PENDIENTE:
                raise ValueError("Reserva no está en estado PENDIENTE")
            self._estado = EstadoReserva.CONFIRMADA
            self._calcular_costo()
            Logger.log_info(f"Reserva {self.id} CONFIRMADA - ${self._costo_total}")
            return True
        except Exception as e:
            Logger.log_error(f"Error confirmando {self.id}: {str(e)}")
            return False
    
    def cancelar(self) -> bool:
        try:
            self._estado = EstadoReserva.CANCELADA
            Logger.log_info(f"Reserva {self.id} CANCELADA")
            return True
        except Exception as e:
            Logger.log_error(f"Error cancelando {self.id}: {str(e)}")
            return False
    
    def procesar(self) -> bool:
        try:
            if self._estado != EstadoReserva.CONFIRMADA:
                raise ValueError("Reserva debe estar CONFIRMADA")
            self._estado = EstadoReserva.COMPLETADA
            Logger.log_info(f"Reserva {self.id} COMPLETADA")
            return True
        except Exception as e:
            Logger.log_error(f"Error procesando {self.id}: {str(e)}")
            return False
    
    def _validar(self) -> bool:
        return (self._cliente.validar() and 
                self._servicio.validar_parametros(duracion=self._duracion))
    
    def _calcular_costo(self):
        self._costo_total = self._servicio.calcular_costo_completo(self._duracion)
    
    def __str__(self):
        return (f"Reserva {self.id} | {self.cliente.nombre} | "
                f"{self.servicio.nombre} | {self.estado.value.upper()} | ${self.costo_total}")