from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

class Entidad(ABC):
    
    def __init__(self, id: str = None):
        self._id = id or self._generar_id()
        self._fecha_creacion = datetime.now()
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def fecha_creacion(self) -> datetime:
        return self._fecha_creacion
    
    def _generar_id(self) -> str:
        return f"ENT-{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    
    @abstractmethod
    def validar(self) -> bool:
        pass
    def to_dict(self) -> dict:
        return {
            'id': self._id,
            'fecha_creacion': self._fecha_creacion.isoformat()
        }