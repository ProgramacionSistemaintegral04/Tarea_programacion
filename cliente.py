from Entidad import Entidad
import re

class Cliente(Entidad):
    
    def __init__(self, nombre: str, email: str, telefono: str, 
                 documento: str, direccion: str = None):
        super().__init__()
        self._nombre = None
        self._email = None
        self._telefono = None
        self._documento = None
        self._direccion = None
        
        # Validaciones robustas
        if self._validar_nombre(nombre):
            self._nombre = nombre.strip().title()
        if self._validar_email(email):
            self._email = email.lower().strip()
        if self._validar_telefono(telefono):
            self._telefono = telefono
        if self._validar_documento(documento):
            self._documento = documento
        if direccion:
            self._direccion = direccion.strip()
        
        if not self.validar():
            print(f"Cliente inválido: {self._nombre}")
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def telefono(self) -> str:
        return self._telefono
    
    @property
    def documento(self) -> str:
        return self._documento
    
    @property
    def direccion(self) -> str:
        return self._direccion
    
    def validar(self) -> bool:
        return all([
            self._nombre is not None,
            self._email is not None,
            self._telefono is not None,
            self._documento is not None
        ])
    
    def _validar_nombre(self, nombre: str) -> bool:
        return bool(nombre and 2 <= len(nombre.strip()) <= 100)
    
    def _validar_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def _validar_telefono(self, telefono: str) -> bool:
        pattern = r'^\+?[\d\s\-\$\$]{10,15}$'
        return bool(re.match(pattern, telefono))
    
    def _validar_documento(self, documento: str) -> bool:
        return bool(documento and 7 <= len(documento.strip()) <= 20)
    
    def to_dict(self) -> dict:
        return super().to_dict() | {
            'nombre': self._nombre,
            'email': self._email,
            'telefono': self._telefono,
            'documento': self._documento,
            'direccion': self._direccion
        }
