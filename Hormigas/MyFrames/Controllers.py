from tkinter import E, N, S, W, BooleanVar, Checkbutton, IntVar, Radiobutton, Spinbox, Tk,Label,Frame,Entry,Button,Scale



class Controllers(Frame):
    
    def __init__(self,master):
        # Constructor de Frame()
        super().__init__(master,width=1000,height=700,background="gray")
        
        # Variable del deslizador para el tamaño de la matriz
        self.SizeMatrix=10
        # Variable del deslizador para la velocidad del simulador
        self.SpeedSim=0.00001
        
        self.InverterColorCells=BooleanVar()
        self.OptionBorder=IntVar()
        
        # empaquetando elementos dentro de su ventana contenedora
        self.createWidgets()
        self.pack()
        
    # Aqui se crean todos los widgets del frame
    def createWidgets(self):
        value_padx=10
        value_pady=10
        
        # Fila 0
        self.lbl1=Label(self,text="Dezliza para la cantidad de celdas en la matriz.")
        # self.lbl1.config(background="blue")
        self.lbl1.grid(row=0,column=0,columnspan=3,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.lbl_num_live=Label(self,text="Vida:")
        self.lbl_num_live.grid(row=0,column=3,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        # Fila 1
        self.scale_size_matrix=Scale(self,orient="horizontal",command=self.setLabelScaleSizeMatrix,from_=10,to=200,
                        # tickinterval=10,
                        resolution=10)
        self.scale_size_matrix.grid(row=1,column=0,columnspan=3,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        
        self.lbl_num_generations=Label(self,text="Generacion:")
        self.lbl_num_generations.grid(row=1,column=3,padx=value_padx,pady=value_pady,sticky=N+E+W)
        
        self.lbl_num_cells=Label(self,text="Celulas Vivas:")
        self.lbl_num_cells.grid(row=1,column=3,padx=value_padx,pady=value_pady,sticky=S+E+W)
        
        # Fila 2
        self.btn_load_conf=Button(self,text="Cargar Config")
        self.btn_load_conf.grid(row=2,column=0,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.rbtn_open_border=Radiobutton(self,text="Frontera Abierta",variable=self.OptionBorder,value=0)
        self.rbtn_open_border.grid(row=2,column=3,padx=value_padx,pady=value_pady,sticky=N)
        
        self.lbl_file_path=Label(self,text="Ruta Archivo:")
        self.lbl_file_path.grid(row=2,column=1,columnspan=2,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        # Fila 3
        self.rbtn_circular_border=Radiobutton(self,text="Frontera Circular",variable=self.OptionBorder,value=1)
        self.rbtn_circular_border.grid(row=3,column=3,padx=value_padx,pady=value_pady,sticky=S)
        
        self.lbl2=Label(self,text="Vel:                   msegs.")
        self.lbl2.grid(row=3,column=1,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.spn_box_speed=Spinbox(self,from_=100,to=10000,increment=100)
        self.spn_box_speed.config(width=4)
        self.spn_box_speed.grid(row=3,column=1,padx=value_padx,pady=value_pady)
        
        self.btn_save_conf=Button(self,text="Guardar Config")
        self.btn_save_conf.grid(row=3,column=0,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        # Fila 4
        self.btn_pause=Button(self,text="Pausar")
        self.btn_pause.grid(row=4,column=1,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.btn_clear=Button(self,text="Limpiar")
        self.btn_clear.grid(row=4,column=0,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.btn_run_simulation=Button(self,text="Correr/Reanudar simulacion")
        self.btn_run_simulation.grid(row=4,column=2,columnspan=2,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        # Fila 5
        self.lbl6=Label(self,text="Reinas:               ")
        self.lbl6.grid(row=5,column=0,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.spn_box_reinas=Spinbox(self,from_=1,to=90,)
        self.spn_box_reinas.config(width=4)
        self.spn_box_reinas.grid(row=5,column=0,padx=value_padx,pady=value_pady,sticky=E)
        
        self.lbl7=Label(self,text="Trabajadoras:              ")
        self.lbl7.grid(row=5,column=1,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.spn_box_trabajadoras=Spinbox(self,from_=1,to=90)
        self.spn_box_trabajadoras.config(width=4)
        self.spn_box_trabajadoras.grid(row=5,column=1,padx=value_padx,pady=value_pady,sticky=E)
        
        self.lbl8=Label(self,text="Reproductoras:         ")
        self.lbl8.grid(row=5,column=2,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.spn_box_reproductoras=Spinbox(self,from_=1,to=90)
        self.spn_box_reproductoras.config(width=4)
        self.spn_box_reproductoras.grid(row=5,column=2,padx=value_padx,pady=value_pady,sticky=E)
        
        self.lbl9=Label(self,text="Soldados:             ")
        self.lbl9.grid(row=5,column=3,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.spn_box_soldados=Spinbox(self,from_=1,to=90)
        self.spn_box_soldados.config(width=4)
        self.spn_box_soldados.grid(row=5,column=3,padx=value_padx,pady=value_pady,sticky=E)
        
        # Fila 6
        self.btn_reset_type_density=Button(self,text="Restablecer")
        self.btn_reset_type_density.grid(row=6,column=0,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
        self.lbl10=Label(self,text="Parametros validos:")
        self.lbl10.grid(row=6,column=1,columnspan=3,padx=value_padx,pady=value_pady,sticky=S+N+E+W)
        
    def setLabelScaleSizeMatrix(self,v):
        # automaticamente obtiene el valor del Scale
        cad="Tamaño cuadro: "+v+" X "+v
        self.SizeMatrix=int(v)
        self.lbl1.config(text=cad)


# root=Tk()
# root.title("Controles")
# app=Controllers(root)
# app.mainloop()