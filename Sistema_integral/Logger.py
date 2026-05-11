from datetime import datetime
import os

class Logger:
    _log_file = "reservas.log"
    
    @classmethod
    def log_info(cls, mensaje: str):
        cls._log(mensaje, "INFO")
    
    @classmethod
    def log_error(cls, mensaje: str):
        cls._log(mensaje, "ERROR")
    
    @classmethod
    def _log(cls, mensaje: str, nivel: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{nivel}] {mensaje}"
        
        print(log_entry)  # Consola
        
        # Archivo
        with open(cls._log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
            