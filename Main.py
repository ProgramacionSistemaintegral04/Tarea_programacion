#!/usr/bin/env python3


import tkinter as tk
from interfaz import interfaz
from Logger import Logger

def main():
    print("Iniciando Sistema de Reservas de Peluquería...")
    Logger.log_info("=== SISTEMA INICIADO ===")
    
    root = tk.Tk()
    app = interfaz(root)
    root.mainloop()
    
    Logger.log_info("=== SISTEMA FINALIZADO ===")

if __name__ == "__main__":
    main()