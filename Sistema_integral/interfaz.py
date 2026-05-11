import tkinter as tk
from datetime import datetime, timedelta
from tkinter import ttk, messagebox
from cliente import Cliente
from servicios_especializados import CorteCabello, Tinte, Manicura
from Reserva import Reserva, EstadoReserva
from datetime import datetime
from Logger import Logger

class interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reservas - Peluquería")
        self.root.geometry("900x700")
        self.reservas = []  # Lista en memoria
        
        self.crear_interfaz()
        self.cargar_datos_ejemplo()
    
    def crear_interfaz(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Cliente
        frame_cliente = ttk.LabelFrame(notebook, text="Nuevo Cliente", padding=10)
        notebook.add(frame_cliente, text="Cliente")
        self.crear_form_cliente(frame_cliente)
        
        # Reserva
        frame_reserva = ttk.LabelFrame(notebook, text="Nueva Reserva", padding=10)
        notebook.add(frame_reserva, text="Reserva")
        self.crear_form_reserva(frame_reserva)
        
        # Lista
        frame_lista = ttk.LabelFrame(notebook, text="Gestión de Reservas", padding=10)
        notebook.add(frame_lista, text="Reservas")
        self.crear_lista_reservas(frame_lista)
    
    def crear_form_cliente(self, parent):
        row = 0
        ttk.Label(parent, text="Nombre:").grid(row=row, column=0, sticky="w", padx=5, pady=5)
        self.entry_nombre = ttk.Entry(parent, width=30)
        self.entry_nombre.grid(row=row, column=1, padx=5, pady=5); row += 1
        
        ttk.Label(parent, text="Email:").grid(row=row, column=0, sticky="w", padx=5, pady=5)
        self.entry_email = ttk.Entry(parent, width=30)
        self.entry_email.grid(row=row, column=1, padx=5, pady=5); row += 1
        
        ttk.Label(parent, text="Teléfono:").grid(row=row, column=0, sticky="w", padx=5, pady=5)
        self.entry_telefono = ttk.Entry(parent, width=30)
        self.entry_telefono.grid(row=row, column=1, padx=5, pady=5); row += 1
        
        ttk.Label(parent, text="Documento:").grid(row=row, column=0, sticky="w", padx=5, pady=5)
        self.entry_documento = ttk.Entry(parent, width=30)
        self.entry_documento.grid(row=row, column=1, padx=5, pady=5); row += 1
        
        ttk.Button(parent, text="Guardar Cliente", 
                  command=self.guardar_cliente).grid(row=row, column=0, columnspan=2, pady=20)
        
        self.label_status_cliente = ttk.Label(parent, text="", foreground="green", font=("Arial", 10, "bold"))
        self.label_status_cliente.grid(row=row+1, column=0, columnspan=2, pady=5)
    
    def crear_form_reserva(self, parent):
        row = 0
        ttk.Label(parent, text="Cliente ID:").grid(row=row, column=0, sticky="w", padx=5, pady=5)
        self.entry_cliente_id = ttk.Entry(parent, width=25)
        self.entry_cliente_id.grid(row=row, column=1, padx=5, pady=5); row += 1
        
        ttk.Label(parent, text="Servicio:").grid(row=row, column=0, sticky="w", padx=5, pady=5)
        self.combo_servicio = ttk.Combobox(parent, values=["CorteCabello", "Tinte", "Manicura"], width=22)
        self.combo_servicio.grid(row=row, column=1, padx=5, pady=5); row += 1
        
        ttk.Label(parent, text="Duración (min):").grid(row=row, column=0, sticky="w", padx=5, pady=5)
        self.entry_duracion = ttk.Entry(parent, width=25)
        self.entry_duracion.grid(row=row, column=1, padx=5, pady=5); row += 1
        
        ttk.Label(parent, text="Fecha/Hora:").grid(row=row, column=0, sticky="w", padx=5, pady=5)
        self.entry_fecha = ttk.Entry(parent, width=25)
        self.entry_fecha.insert(0, (datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M"))
        self.entry_fecha.grid(row=row, column=1, padx=5, pady=5); row += 1
        
        ttk.Button(parent, text="Crear Reserva", 
                  command=self.crear_reserva).grid(row=row, column=0, columnspan=2, pady=20)
        
        self.label_status_reserva = ttk.Label(parent, text="", foreground="green", font=("Arial", 10, "bold"))
        self.label_status_reserva.grid(row=row+1, column=0, columnspan=2, pady=5)
    
    def crear_lista_reservas(self, parent):
        columns = ("ID", "Cliente", "Servicio", "Duración", "Fecha", "Estado", "Costo")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings", height=12)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110)
        
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True, padx=(0,10), pady=10)
        scrollbar.pack(side="right", fill="y")
        
        frame_botones = ttk.Frame(parent)
        frame_botones.pack(fill="x", padx=10, pady=(0,10))
        
        ttk.Button(frame_botones, text="Confirmar", command=self.confirmar_reserva).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Cancelar", command=self.cancelar_reserva).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Completar", command=self.procesar_reserva).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Actualizar", command=self.actualizar_lista).pack(side="right", padx=5)
    
    def guardar_cliente(self):
        try:
            cliente = Cliente(
                self.entry_nombre.get(),
                self.entry_email.get(),
                self.entry_telefono.get(),
                self.entry_documento.get()
            )
            if cliente.validar():
                self.label_status_cliente.config(text=f"Cliente OK: {cliente.id}", foreground="green")
                self.entry_cliente_id.delete(0, tk.END)
                self.entry_cliente_id.insert(0, cliente.id)
            else:
                self.label_status_cliente.config(text="Datos inválidos", foreground="red")
        except Exception as e:
            self.label_status_cliente.config(text=f"Error: {str(e)}", foreground="red")
    
    def crear_reserva(self):
        try:
            duracion = float(self.entry_duracion.get())
            fecha_str = self.entry_fecha.get()
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
            servicio_tipo = self.combo_servicio.get()
            
            # Cliente simulado (en prod buscar por ID)
            cliente = Cliente("Juan Pérez", "juan@email.com", "+54 11 1234-5678", "30-12345678-9")
            
            # Servicio polimórfico
            if servicio_tipo == "CorteCabello":
                servicio = CorteCabello("Corte Clásico", 25.0)
            elif servicio_tipo == "Tinte":
                servicio = Tinte("Tinte Permanente", 60.0, "permanente")
            else:
                servicio = Manicura("Manicura Completa", 30.0)
            
            reserva = Reserva(cliente, servicio, duracion, fecha)
            reserva.confirmar()
            self.reservas.append(reserva)
            
            costo = f"${reserva.costo_total:.2f}"
            self.label_status_reserva.config(text=f" Reserva {reserva.id} | {servicio.nombre} | {costo}", 
                                           foreground="green")
            self.actualizar_lista()
            
        except ValueError as e:
            self.label_status_reserva.config(text=f"Error: {str(e)}", foreground="red")
    
    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for reserva in self.reservas:
            self.tree.insert("", "end", values=(
                reserva.id, reserva.cliente.nombre, 
                reserva.servicio.nombre, f"{reserva.duracion}min",
                reserva.fecha.strftime("%Y-%m-%d %H:%M"),
                reserva.estado.value.upper(), f"${reserva.costo_total:.2f}"
            ))
    
    def confirmar_reserva(self):
        seleccion = self.tree.selection()
        if seleccion:
            messagebox.showinfo("Reserva confirmada exitosamente!")
            self.actualizar_lista()
    
    def cancelar_reserva(self):
        seleccion = self.tree.selection()
        if seleccion:
            messagebox.showinfo( "Reserva cancelada!")
            self.actualizar_lista()
    
    def procesar_reserva(self):
        seleccion = self.tree.selection()
        if seleccion:
            messagebox.showinfo( "Reserva completada!")
            self.actualizar_lista()
    
    def cargar_datos_ejemplo(self):
        # Datos de prueba
        cliente_ejemplo = Cliente("María García", "maria@email.com", "+54 11 9876-5432", "30-98765432-1")
        self.entry_cliente_id.insert(0, cliente_ejemplo.id)