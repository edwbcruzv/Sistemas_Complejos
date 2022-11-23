from tkinter import Checkbutton, IntVar, Radiobutton, Tk,Label,Frame,Entry,Button,Scale



class Controllers(Frame):
    
    def __init__(self,master):
        # Constructor de Frame()
        super().__init__(master,width=420,height=500,background="gray")
        
        # Variable del deslizador para el tamaño de la matriz
        self.SizeMatrix=100
        # Variable del deslizador para la velocidad del simulador
        self.SpeedSim=0.00001
        
        self.option_border=IntVar()
        
        # empaquetando elementos dentro de su ventana contenedora
        self.createWidgets()
        self.pack()
        
    # Aqui se crean todos los widgets del frame
    def createWidgets(self):
        self.lbl1=Label(self,text="Dezliza para la cantidad de celdas en la matriz.")
        self.lbl1.config(background="blue")
        self.lbl1.place(x=10,y=50,width=400,height=30)
        
        self.scale_size_matrix=Scale(self,orient="horizontal",command=self.setLabelScaleSizeMatrix,from_=500,to=5000,
                        tickinterval=100,resolution=0)
        self.scale_size_matrix.config(background="red")
        self.scale_size_matrix.place(x=10,y=10,width=400,height=40)

        self.btn_save_conf=Button(self,text="Guardar Config")
        self.btn_save_conf.config(background="red")
        self.btn_save_conf.place(x=10,y=300,width=130,height=30)
        
        self.btn_load_conf=Button(self,text="Cargar Config")
        self.btn_load_conf.config(background="red")
        self.btn_load_conf.place(x=10,y=90,width=130,height=30)
        
        self.lbl_path_file_load=Label(self,text="Ruta Archivo")
        self.lbl_path_file_load.config(background="blue")
        self.lbl_path_file_load.place(x=150,y=95,width=260,height=20)

        self.lbl_num_generations=Label(self,text="No. generaciones:")
        self.lbl_num_generations.config(background="blue")
        self.lbl_num_generations.place(x=150,y=340,width=260,height=20)
        
        self.lbl_num_cells=Label(self,text="No. celulas:")
        self.lbl_num_cells.config(background="blue")
        self.lbl_num_cells.place(x=150,y=370,width=260,height=20)
        
        self.btn_run_simulation=Button(self,text="Correr simulacion")
        self.btn_run_simulation.config(background="blue")
        self.btn_run_simulation.place(x=150,y=300,width=260,height=30)
        
        self.btn_pause=Button(self,text="Pausar")
        self.btn_pause.config(background="red")
        self.btn_pause.place(x=10,y=340,width=130,height=30)
        
        self.btn_reset=Button(self,text="Resetear")
        self.btn_reset.config(background="red")
        self.btn_reset.place(x=10,y=460,width=400,height=30)
        
        self.lbl4=Label(self,text="Dezliza para controlar la velocidad de la simulacion.")
        self.lbl4.config(background="blue")
        self.lbl4.place(x=10,y=230,width=400,height=30)
        
        self.scale_speed_sim=Scale(self,orient="horizontal",command=self.setLabelScaleSpeedSim,from_=0.00001,to=10,
                        tickinterval=0.00001,resolution=0.00001)
        self.scale_speed_sim.config(background="red")
        self.scale_speed_sim.place(x=10,y=260,width=400,height=40)
        
        self.btn_density_graph=Button(self,text="Graficas Densidades")
        self.btn_density_graph.config(background="blue")
        self.btn_density_graph.place(x=10,y=420,width=400,height=30)
        
        
        self.rbtn_open_border=Radiobutton(self,text="Frontera Abierta",variable=self.option_border,value=1)
        self.rbtn_open_border.config(background="green")
        self.rbtn_open_border.place(x=15,y=130,width=120,height=30)
        
        self.rbtn_close_border=Radiobutton(self,text="Frontera Cerrada",variable=self.option_border,value=2)
        self.rbtn_close_border.config(background="green")
        self.rbtn_close_border.place(x=140,y=130,width=120,height=30)
        
        self.rbtn_circular_border=Radiobutton(self,text="Frontera Circular",variable=self.option_border,value=3)
        self.rbtn_circular_border.config(background="green")
        self.rbtn_circular_border.place(x=270,y=130,width=120,height=30)
        
        self.cbtn_inverter_color_cells=Checkbutton(self,text="Inverir color")
        self.cbtn_inverter_color_cells.config(background="green")
        self.cbtn_inverter_color_cells.place(x=270,y=180,width=120,height=30)
        
        self.cbtn_show_cells=Checkbutton(self,text="Mostrar Celdas")
        self.cbtn_show_cells.config(background="green")
        self.cbtn_show_cells.place(x=140,y=180,width=120,height=30)
    
    def setLabelScaleSizeMatrix(self,v):
        # automaticamente obtiene el valor del Scale
        cad="Tamaño cuadro: "+v+" X "+v
        self.SizeMatrix=v
        self.lbl1.config(text=cad)
    
    def setLabelScaleSpeedSim(self,v):
        # automaticamente obtiene el valor del Scale
        cad="Velocidad simulacion: "+v
        self.SpeedSim=float(v)
        self.lbl4.config(text=cad)
    
        
        
# root=Tk()
# root.title("Controles simulador")
# app=Controllers(root)
# app.mainloop()