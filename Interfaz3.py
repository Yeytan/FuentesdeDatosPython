#Actividad 2
from tkinter import *
from tkinter import ttk
from tkinter import Tk
import csv

class Formulario:
    def __init__(self):


        self.raiz = Tk()
        self.raiz.title("Formulario")

        self.nombre = StringVar()
        self.paterno =StringVar()
        self.materno =StringVar()
        self.correo =StringVar()
        self.movil =StringVar()

        self.leer = StringVar()
        self.musica = StringVar()
        self.videojuegos = StringVar()

        self.estudiante = StringVar()
        self.empleado  = StringVar()
        self.desempleado = StringVar()

        self.guardar = StringVar()
        self.cancelar = StringVar()

        self.estado = StringVar()


        mainFrame = ttk.Frame(self.raiz, padding=" 20 30 20 30", relief="raised", width=300, height=300) #el pading sirve para poder hacer una distancia del widget al panel. (izquierda arriba derecha abajo)
        mainFrame.grid(column=0, row=0, pady=25)

        subFrame = ttk.Frame(self.raiz, padding=" 65 30 65 30", relief="raised", width=300, height=300)
        subFrame.grid(column=0, row= 1)

        treeFrame = ttk.Frame(self.raiz, padding=" 20 30 20 30")
        treeFrame.grid(column=0, row=2)

        cuarFrame = ttk.Frame(self.raiz, padding=" 20 30 20 30")
        cuarFrame.grid(column=1, row=0)

        quinFrame = ttk.Frame(self.raiz, padding=" 20 30 20 30")
        quinFrame.grid(column=1, row=1)
        #Entrys
        self.nombreEntry = ttk.Entry(mainFrame, width=35, textvariable=self.nombre)
        self.nombreEntry.grid(column=1, row=0)

        self.paternoEntry = ttk.Entry(mainFrame, width=35, textvariable=self.paterno)
        self.paternoEntry.grid(column=1, row=2)

        self.maternoEntry = ttk.Entry(mainFrame, width=35, textvariable=self.materno)
        self.maternoEntry.grid(column=1, row=4)

        self.correoEntry = ttk.Entry(mainFrame, width=35, textvariable=self.correo)
        self.correoEntry.grid(column=1, row=6)

        self.movilEntry = ttk.Entry(mainFrame, width=35, textvariable=self.movil)
        self.movilEntry.grid(column=1, row=8)
        #Datos frame 1

        ttk.Label(mainFrame, text="Nombre: ").grid(column=0, row=0,padx=15, pady=15) 
        ttk.Label(mainFrame, text="A. Paterno: ").grid(column=0, row=2,padx=15, pady=15) 
        ttk.Label(mainFrame, text="A. Materno: ").grid(column=0, row=4, padx=15,  pady=15) 
        ttk.Label(mainFrame, text="Correo: ").grid(column=0, row=6,padx=15, pady=15) 
        ttk.Label(mainFrame, text="Movil: ").grid(column=0, row=8,padx=15, pady=15) 
        #Botones Guardar y cancelar
        #Frame3
        self.guardarc = ttk.Button(treeFrame, text="Guardar", command= self.boton_guardar)
        self.guardarc.grid(column=0,row=15)
        self.cancelarc = ttk.Button(treeFrame, text="Cancelar",command= self.cancelar_boton)
        self.cancelarc.grid(column=1,row=15)
        self.formularioc=ttk.Button(treeFrame,text="Formulario",command= self.formulario_vent)
        self.formularioc.grid(column=2, row=15, sticky=(W))

        #Aficiones frame 2
        ttk.Label(subFrame, text="Aficiones: ").grid(column=1, row= 12, sticky=(W,S,N,E))
        self.leerv= ttk.Checkbutton(subFrame, text="Leer", variable= self.leer).grid(column=1, row= 13, padx=5)
        self.musicav= ttk.Checkbutton(subFrame, text="Musica", variable= self.musica).grid(column=2, row= 13,padx=5)
        self.videojuegosv= ttk.Checkbutton(subFrame, text="Videojuegos", variable= self.videojuegos).grid(column=3, row= 13, padx=5)
        #RadioButtons
        #Frame4
        self.estudiantev=ttk.Radiobutton(cuarFrame, text="Estudiante", variable= self.estudiante).grid(column=3, row=5, sticky=(W,S,N,E))
        self.empleadov=ttk.Radiobutton(cuarFrame, text="Empleado", variable= self.empleado).grid(column=3, row=6, sticky=(W,S,N,E))
        self.desempleadov=ttk.Radiobutton(cuarFrame, text="Desempleado", variable= self.desempleado).grid(column=3, row=7, sticky=(W,S,N,E))
        #WIDGET ESTADOS LINEA DE ELECCION
        comboEstados = ttk.Combobox(quinFrame, textvariable=self.estado)
        comboEstados.grid(column=2, row=4, sticky=(W))
        comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

        self.raiz.mainloop()
              
    def boton_guardar(self):
              nombreg = self.nombre.get()
              paternog = self.paterno.get()
              maternog = self.materno.get()
              correog = self.correo.get()
              movilg = self.movil.get()
              leerg = self.leer.get()
              musicag = self.musica.get()
              videojuegosg = self.videojuegos.get()
              estudiarg = self.estudiante.get()
              empleadog = self.empleado.get()
              desempleadog = self.desempleado.get()

              with open("DatosFormulario.csv", "a", newline="") as file:
                    formu = csv.writer(file)
                    if file.tell() == 0:
                          formu.writerow(["Nombre", "A.Paterno", "A.Materno", "Correo", "Movil", "Leer", "Musica", "Videojuegos", "Estado", "Ocupacion"])
                    formu.writerow([nombreg,paternog,maternog, correog, movilg,leerg,musicag,videojuegosg,estudiarg,empleadog,desempleadog])

                    self.nombreEntry.delete(0,"end")
                    self.paternoEntry.delete(0,"end")
                    self.maternoEntry.delete(0,"end")
                    self.correoEntry.delete(0,"end")
                    self.movilEntry.delete(0,"end")
                    self.leer.set(False)
                    self.musica.set(False)
                    self.videojuegos.set(False)
                    self.estudiante.set(False)
                    self.empleado.set(False)
                    self.desempleado.set(False)
                    self.estado.set("Estados")

    def cancelar_boton(self):
              self.raiz.destroy()


    def formulario_vent(self):
                ventana = Toplevel(self.raiz)
                ventana.title("Datos de formulario")

                with open("DatosFormulario.csv", mode="r") as file:
                        leercsv = csv.reader(file)
                        newframe1 = ttk.LabelFrame(ventana, text="Datos Formulario")
                        newframe1.pack(fill=BOTH, expand = 1, padx = 5, pady = 5)
                        row_numero = 0

                        for row in leercsv:
                                frame1 = ttk.Label(newframe1, text=row[0], width=20, borderwidth=1, relief="raised")
                                frame1.grid(row=row_numero, column=0)

                                frame2 = ttk.Label(newframe1, text=row[1], width=20, borderwidth=1, relief="raised")
                                frame2.grid(row=row_numero, column=1)
                                
                                frame3 = ttk.Label(newframe1, text=row[2], width=20, borderwidth=1, relief="raised")
                                frame3.grid(row=row_numero, column=2)

                                frame4 = ttk.Label(newframe1, text=row[3], width=20, borderwidth=1, relief="raised")
                                frame4.grid(row=row_numero, column=4)

                                frame5 = ttk.Label(newframe1, text=row[4], width=20, borderwidth=1, relief="raised")
                                frame5.grid(row=row_numero, column=5)

                                frame6 = ttk.Label(newframe1, text=row[5], width=20, borderwidth=1, relief="raised")
                                frame6.grid(row=row_numero, column=6)

                                frame7 = ttk.Label(newframe1, text=row[6], width=20, borderwidth=1, relief="raised")
                                frame7.grid(row=row_numero, column=7)

                                frame8 = ttk.Label(newframe1, text=row[7], width=20, borderwidth=1, relief="raised")
                                frame8.grid(row=row_numero, column=8)

                                frame9 = ttk.Label(newframe1, text=row[8], width=20, borderwidth=1, relief="raised")
                                frame9.grid(row=row_numero, column=9)

                                frame10 = ttk.Label(newframe1, text=row[9], width=20, borderwidth=1, relief="raised")
                                frame10.grid(row=row_numero, column=9)

                                row_numero += 1

Formulario()




            


