#Programa que realiza la transformacion de esfuerzos y deformaciones mediante tensores con el objetivos
#de determinar en que angulos y magnitudes ocurren las deformaciones y esfuerzos principales


#Interfaz de usuario

import tkinter as tk #Se importa para crear la ventana
from tkinter import * #Se importa para crear el Label frame
from tkinter import messagebox as mb # Se importa para crear los cuadros emergentes
import math as mt


class Aplicacion: 

    def __init__(self,ventana):
        
        self.ventana=ventana
        self.ventana.title("Transformación de esfuerzos y deformaciones ")
        marco=LabelFrame(self.ventana,text="Introduzca las constantes")
        marco.grid(row=0,column=0,pady=5,padx=50)

        Label(marco,text="Ingrese el módulo elástico (Pa)").grid(row=0,column=0) #Recordar pasar el codigo plano a Gigapascales
        self.dato1=DoubleVar(value=None)
        self.me=Entry(marco,textvariable=self.dato1,justify=CENTER).grid(row=0,column=1,pady=10,padx=10) #Modulo elastico


        Label(marco,text="Ingrese el coeficiente de Poison").grid(row=1,column=0)
        self.dato2=DoubleVar(value=None)
        self.po=Entry(marco,textvariable=self.dato2,justify=CENTER).grid(row=1,column=1,pady=10,padx=10) #Coeficiente de Poison

        Label(marco, text="Ingrese el valor de i").grid(row=2,column=0) #Entrada del dato del valor de i
        self.datoi=StringVar()
        self.i=Entry(marco,textvariable=self.datoi,justify=CENTER).grid(row=2,column=1,pady=10,padx=10)

        Label(marco, text="Ingrese el valor de j").grid(row=3,column=0) #Entrda del dato del valor de j
        self.datoj=StringVar()
        self.j=Entry(marco,textvariable=self.datoj,justify=CENTER).grid(row=3,column=1,pady=10,padx=10)

        self.boton1=tk.Button(marco, text="Calcular", command=self.tensordeformacion_angulosprincipales)
        self.boton1.grid(row=4, pady=10,sticky=W+E,columnspan=2)


        #Inseción de imagenes

        self.imagen1=PhotoImage(file="Imagen1.png")
        self.img1=Label(self.ventana, image=self.imagen1).grid(row=0,column=2,pady=5,padx=30)

        self.imagen2=PhotoImage(file="Imagen2.png")
        self.fimg2=Label(self.ventana, image=self.imagen2).grid(row=1,column=2,padx=30)

        #Tensor de esfuerzos
        marco1=LabelFrame(self.ventana,text="Introduzca los datos en el tensor de esfuerzos (Mpa)")
        marco1.grid(row=1,column=0,pady=5,padx=50)

        #Primera fila del tensor de esfuerzos
        Label(marco1,text="σx").grid(row=0,column=0)
        self.dato3=DoubleVar(value=None)
        self.rx=Entry(marco1,textvariable=self.dato3,justify=CENTER).grid(row=1,column=0,pady=10,padx=10)

        Label(marco1,text="𝛕xy").grid(row=0,column=1)
        self.dato4=DoubleVar(value=None)
        self.txy=Entry(marco1,textvariable=self.dato4,justify=CENTER).grid(row=1,column=1,pady=10,padx=10)

        Label(marco1,text="𝛕xz").grid(row=0,column=2)
        self.dato5=DoubleVar(value=None)
        self.txz=Entry(marco1,textvariable=self.dato5,justify=CENTER).grid(row=1,column=2,pady=10,padx=10)

        #Segunda fila del tensor de esfuerzos
        Label(marco1,text="𝛕yx").grid(row=2,column=0)
        self.dato6=DoubleVar(value=None)
        self.tyx=Entry(marco1,textvariable=self.dato6,justify=CENTER).grid(row=3,column=0,pady=10,padx=10)

        Label(marco1,text="σy").grid(row=2,column=1)
        self.dato7=DoubleVar(value=None)
        self.ry=Entry(marco1,textvariable=self.dato7,justify=CENTER).grid(row=3,column=1,pady=10,padx=10)

        Label(marco1,text="𝛕yz").grid(row=2,column=2)
        self.dato8=DoubleVar(value=None)
        self.tyz=Entry(marco1,textvariable=self.dato8,justify=CENTER).grid(row=3,column=2,pady=10,padx=10)

        #Tercer fila del tensor de esfuerzos
        Label(marco1,text="𝛕zx").grid(row=4,column=0)
        self.dato9=DoubleVar(value=None)
        self.tzx=Entry(marco1,textvariable=self.dato9,justify=CENTER).grid(row=5,column=0,pady=10,padx=10)

        Label(marco1,text="𝛕zy").grid(row=4,column=1)
        self.dato10=DoubleVar(value=None)
        self.tzy=Entry(marco1,textvariable=self.dato10,justify=CENTER).grid(row=5,column=1,pady=10,padx=10)

        Label(marco1,text="σz").grid(row=4,column=2)
        self.dato11=DoubleVar(value=None)
        self.rz=Entry(marco1,textvariable=self.dato11,justify=CENTER).grid(row=5,column=2,pady=10,padx=10)

        marco2=LabelFrame(self.ventana,text="Tensor de deformaciones (m/m)")
        marco2.grid(row=2,column=0,pady=5,padx=50)

        #Primera fila del tensor de deformaciones

        self.resultado1=DoubleVar()
        Label(marco2,text="εx").grid(row=0,column=0,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.ex=Entry(marco2,textvariable=self.resultado1,state=DISABLED,justify=CENTER).grid(row=1,column=0,pady=10,padx=10)

        self.resultado2=DoubleVar()
        Label(marco2,text="γxy/2").grid(row=0,column=1)
        #self.label2=Label(marco2).grid(row=9,column=1,pady=10,padx=10)
        self.ecxy=Entry(marco2,textvariable=self.resultado2,state=DISABLED,justify=CENTER).grid(row=1,column=1,pady=10,padx=10)

        self.resultado3=DoubleVar()
        Label(marco2,text="γxz/2").grid(row=0,column=2)
        #self.label3=Label(marco2).grid(row=9,column=2,pady=10,padx=10)
        self.ecxz=Entry(marco2,textvariable=self.resultado3,state=DISABLED,justify=CENTER).grid(row=1,column=2,pady=10,padx=10)

        #Segunda fila del tensor de deformaciones

        self.resultado4=DoubleVar()
        Label(marco2,text="γyx/2").grid(row=2,column=0)
        #self.label4=Label(marco2).grid(row=11,column=0,pady=10,padx=10)
        self.ecyx=Entry(marco2,textvariable=self.resultado4,state=DISABLED,justify=CENTER).grid(row=3,column=0,pady=10,padx=10)

        self.resultado5=DoubleVar()
        Label(marco2,text="εy").grid(row=2,column=1)
        #self.label5=Label(marco2).grid(row=11,column=1,pady=10,padx=10)
        self.ey=Entry(marco2,textvariable=self.resultado5,state=DISABLED,justify=CENTER).grid(row=3,column=1,pady=10,padx=10)

        self.resultado6=DoubleVar()
        Label(marco2,text="γyz/2").grid(row=2,column=2)
        #self.label6=Label(marco2).grid(row=11,column=2,pady=10,padx=10)
        self.ecyz=Entry(marco2,textvariable=self.resultado6,state=DISABLED,justify=CENTER).grid(row=3,column=2,pady=10,padx=10)

        #Tercer fila del tensor de deformaciones

        self.resultado7=DoubleVar()
        Label(marco2,text="γzx/2").grid(row=4,column=0)
        #self.label7=Label(marco2).grid(row=13,column=0,pady=10,padx=10)
        self.eczx=Entry(marco2,textvariable=self.resultado7,state=DISABLED,justify=CENTER).grid(row=5,column=0,pady=10,padx=10)

        self.resultado8=DoubleVar()
        Label(marco2,text="γzy/2").grid(row=4,column=1)
        #self.label8=Label(marco2).grid(row=13,column=1,pady=10,padx=10)
        self.eczy=Entry(marco2,textvariable=self.resultado8,state=DISABLED,justify=CENTER).grid(row=5,column=1,pady=10,padx=10)

        self.resultado9=DoubleVar()
        Label(marco2,text="εz").grid(row=4,column=2)
        #self.label9=Label(marco2).grid(row=13,column=2,pady=10,padx=10)  
        self.ez=Entry(marco2,textvariable=self.resultado9,state=DISABLED,justify=CENTER).grid(row=5,column=2,pady=10,padx=10) 

        

        #Resultados de angulos para esfuerzos y deformaciones 

        marco3=LabelFrame(self.ventana,text="Angulos (Grados)")
        marco3.grid(row=0,column=5,pady=5,padx=50)

        self.angulo1=DoubleVar()
        Label(marco3,text="θs Esfuerzo").grid(row=0,column=0,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.an1=Entry(marco3,textvariable=self.angulo1,state=DISABLED,justify=CENTER).grid(row=1,column=0,pady=10,padx=10)

        self.angulo2=DoubleVar()
        Label(marco3,text="θp Esfuerzo").grid(row=2,column=0)
        #self.label2=Label(marco2).grid(row=9,column=1,pady=10,padx=10)
        self.an2=Entry(marco3,textvariable=self.angulo2,state=DISABLED,justify=CENTER).grid(row=3,column=0,pady=10,padx=10)

        self.angulo3=DoubleVar()
        Label(marco3,text="θs Deformación").grid(row=0,column=1,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.an3=Entry(marco3,textvariable=self.angulo3,state=DISABLED,justify=CENTER).grid(row=1,column=1,pady=10,padx=10)

        self.angulo4=DoubleVar()
        Label(marco3,text="θp Deformación").grid(row=2,column=1)
        #self.label2=Label(marco2).grid(row=9,column=1,pady=10,padx=10)
        self.an4=Entry(marco3,textvariable=self.angulo4,state=DISABLED,justify=CENTER).grid(row=3,column=1,pady=10,padx=10)

        #Resultados de esfuerzos principales 

        marco4=LabelFrame(self.ventana,text="Esfuerzos principales (Mpa)")
        marco4.grid(row=1,column=5,pady=5,padx=50)

        self.esfuerzo1=DoubleVar()
        Label(marco4,text="Ri Normal").grid(row=0,column=0,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.es1=Entry(marco4,textvariable=self.esfuerzo1,state=DISABLED,justify=CENTER).grid(row=1,column=0,pady=10,padx=10)

        self.esfuerzo2=DoubleVar()
        Label(marco4,text="Rj Normal").grid(row=2,column=0,sticky=W+E)
        #self.label2=Label(marco2).grid(row=9,column=1,pady=10,padx=10)
        self.es2=Entry(marco4,textvariable=self.esfuerzo2,state=DISABLED,justify=CENTER).grid(row=3,column=0,pady=10,padx=10)

        self.esfuerzo3=DoubleVar()
        Label(marco4,text="Tij Normal").grid(row=4,column=0,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.es3=Entry(marco4,textvariable=self.esfuerzo3,state=DISABLED,justify=CENTER).grid(row=5,column=0,pady=10,padx=10)

        self.esfuerzo4=DoubleVar()
        Label(marco4,text="Ri Cortante").grid(row=0,column=1,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.es4=Entry(marco4,textvariable=self.esfuerzo4,state=DISABLED,justify=CENTER).grid(row=1,column=1,pady=10,padx=10)

        self.esfuerzo5=DoubleVar()
        Label(marco4,text="Rj Cortante").grid(row=2,column=1,sticky=W+E)
        #self.label2=Label(marco2).grid(row=9,column=1,pady=10,padx=10)
        self.es5=Entry(marco4,textvariable=self.esfuerzo5,state=DISABLED,justify=CENTER).grid(row=3,column=1,pady=10,padx=10)

        self.esfuerzo6=DoubleVar()
        Label(marco4,text="Tij Cortante").grid(row=4,column=1,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.es6=Entry(marco4,textvariable=self.esfuerzo6,state=DISABLED,justify=CENTER).grid(row=5,column=1,pady=10,padx=10)

        #Resultados de deformaciones principales 

        marco5=LabelFrame(self.ventana,text="Deformaciones principales")
        marco5.grid(row=2,column=5,pady=5,padx=50)

        self.deformacion1=DoubleVar()
        Label(marco5,text="Ei Normal").grid(row=0,column=0,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.de1=Entry(marco5,textvariable=self.deformacion1,state=DISABLED,justify=CENTER).grid(row=1,column=0,pady=10,padx=10)

        self.deformacion2=DoubleVar()
        Label(marco5,text="Ej Normal").grid(row=2,column=0,sticky=W+E)
        #self.label2=Label(marco2).grid(row=9,column=1,pady=10,padx=10)
        self.de2=Entry(marco5,textvariable=self.deformacion2,state=DISABLED,justify=CENTER).grid(row=3,column=0,pady=10,padx=10)

        self.deformacion3=DoubleVar()
        Label(marco5,text="Gij Normal").grid(row=4,column=0,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.de3=Entry(marco5,textvariable=self.deformacion3,state=DISABLED,justify=CENTER).grid(row=5,column=0,pady=10,padx=10)

        self.deformacion4=DoubleVar()
        Label(marco5,text="Ei Cortante").grid(row=0,column=1,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.de4=Entry(marco5,textvariable=self.deformacion4,state=DISABLED,justify=CENTER).grid(row=1,column=1,pady=10,padx=10)

        self.deformacion5=DoubleVar()
        Label(marco5,text="Ej Cortante").grid(row=2,column=1,sticky=W+E)
        #self.label2=Label(marco2).grid(row=9,column=1,pady=10,padx=10)
        self.de5=Entry(marco5,textvariable=self.deformacion5,state=DISABLED,justify=CENTER).grid(row=3,column=1,pady=10,padx=10)

        self.deformacion6=DoubleVar()
        Label(marco5,text="Gij Cortante").grid(row=4,column=1,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.de6=Entry(marco5,textvariable=self.deformacion6,state=DISABLED,justify=CENTER).grid(row=5,column=1,pady=10,padx=10)

        marco6=LabelFrame(self.ventana,text="Autores")
        marco6.grid(row=2,column=2,pady=5,padx=50)
        Label(marco6,text="José Alejandro Urrego Pabon").grid(row=0,column=0,sticky=W+E)
        Label(marco6,text="Juan Carlos Mercado Montes").grid(row=1,column=0,sticky=W+E)
        Label(marco6,text="Samuel Alejandro Gallo").grid(row=2,column=0,sticky=W+E)
        Label(marco6,text="Sebastian Grisales Cadavid").grid(row=3,column=0,sticky=W+E)
        Label(marco6,text="Agradecimientos: ").grid(row=4,column=0,sticky=W+E,pady=10)
        Label(marco6,text="William Humberto Usuga Giraldo").grid(row=5,column=0,sticky=W+E)
        Label(marco6,text="Edwin Lenin Chica Arrieta").grid(row=6,column=0,sticky=W+E)

    def tensordeformacion_angulosprincipales(self):
        
        #Tensor de deformaciones

        #Calculo de las deformaciones

        try:
            if type(float(self.dato1.get()))==float and type(float(self.dato1.get()))==float:
                e=float(self.dato1.get())
                v=float(self.dato2.get())
                G=(e)/(2*(1+v)) #Modulo de rigidez 
        except Exception as err:
            mb.showerror(message="Los datos del modulo elastico y el coeficiente de Poison deben ser numericos", title="Error modulo elastico o coeficiente de Poison")

        #Validación de los componentes del esfuerzo cortante
        
        try:
            if (type(float(self.dato3.get()))==float and type(float(self.dato7.get()))==float and type(float(self.dato11.get()))==float 
                and type(float(self.dato4.get()))==float and type(float(self.dato5.get()))==float and type(float(self.dato6.get()))==float
                and type(float(self.dato8.get()))==float and type(float(self.dato9.get()))==float and type(float(self.dato10.get()))==float):

                    rx=float(self.dato3.get())
                    ry=float(self.dato7.get())
                    rz=float(self.dato11.get())

                    ex=(rx/e)-((v/e)*(ry+rz))
                    self.resultado1.set(ex)

                    ey=(ry/e)-((v/e)*(rx+rz))
                    self.resultado5.set(ey)

                    ez=(rz/e)-((v/e)*(ry+rx))
                    self.resultado9.set(ez)

                    txy=float(self.dato4.get())
                    ecxy=txy/(2*G)
                    self.resultado2.set(ecxy)

                    txz=float(self.dato5.get())
                    ecxz=txz/(2*G)
                    self.resultado3.set(ecxz)

                    tyx=float(self.dato6.get())
                    ecyx=tyx/(2*G)
                    self.resultado4.set(ecyx)

                    tyz=float(self.dato8.get())
                    ecyz=tyz/(2*G)
                    self.resultado6.set(ecyz)

                    tzx=float(self.dato9.get())
                    eczx=tzx/(2*G)
                    self.resultado7.set(eczx)

                    tzy=float(self.dato10.get())
                    eczy=tzy/(2*G)
                    self.resultado8.set(eczy)

        except Exception as err:
            mb.showerror(message="Los esfuerzos deben ser datos numericos y no deben estar vacios, ponga (0.0 en caso de no haber dato)",title="Error tensor de esfuerzos")
        
        boleano=False
       
        i=(self.datoi.get())
        j=(self.datoj.get())

        if (i=="x" and j=="y"):
            tetape=(mt.atan((txy*2)/(rx-ry))/2)
            tetapd=(mt.atan((ecxy*2)/(ex-ey))/2)
            tetase=(mt.atan(-(rx-ry)/(txy*2))/2)
            tetasd=(mt.atan(-(ex-ey)/(ecxy*2))/2)
            
            rin=((rx+ry)/2)+((rx-ry)/2)*mt.cos(2*tetape)+(txy)*mt.sin(2*tetape)
            rjn=((rx+ry)/2)-((rx-ry)/2)*mt.cos(2*tetape)-(txy)*mt.sin(2*tetape)
            tn=-((rx-ry)/2)*mt.sin(2*tetape)+(txy)*mt.cos(2*tetape)
            ric=((rx+ry)/2)+((rx-ry)/2)*mt.cos(2*tetase)+(txy)*mt.sin(2*tetase)
            rjc=((rx+ry)/2)-((rx-ry)/2)*mt.cos(2*tetase)-(txy)*mt.sin(2*tetase)
            tc=-((rx-ry)/2)*mt.sin(2*tetase)+(txy)*mt.cos(2*tetase)
            
            ein=((ex+ey)/2)+((ex-ey)/2)*mt.cos(2*tetapd)+(ecxy)*mt.sin(2*tetapd)
            ejn=((ex+ey)/2)-((ex-ey)/2)*mt.cos(2*tetapd)-(ecxy)*mt.sin(2*tetapd)
            gn=-((ex-ey)/2)*mt.sin(2*tetapd)+(ecxy)*mt.cos(2*tetapd)
            eic=((ex+ey)/2)+((ex-ey)/2)*mt.cos(2* tetasd)+(ecxy)*mt.sin(2* tetasd)
            ejc=((ex+ey)/2)-((ex-ey)/2)*mt.cos(2* tetasd)-(ecxy)*mt.sin(2* tetasd)
            gc=-((ex-ey)/2)*mt.sin(2* tetasd)+(ecxy)*mt.cos(2* tetasd)
            boleano=True

        elif((i=="x") and (j=="z")):
            
            tetape=(mt.atan((txz*2)/(rx-rz))/2)
            tetapd=(mt.atan((ecxz*2)/(ex-ez))/2)
            tetase=(mt.atan(-(rx-rz)/(txz*2))/2)
            tetasd=(mt.atan(-(ex-ez)/(ecxz*2))/2)
            
            rin=((rx+rz)/2)+((rx-rz)/2)*mt.cos(2*tetape)+(txz)*mt.sin(2*tetape)
            rjn=((rx+rz)/2)-((rx-rz)/2)*mt.cos(2*tetape)-(txz)*mt.sin(2*tetape)
            tn=-((rx-rz)/2)*mt.sin(2*tetape)+(txz)*mt.cos(2*tetape)
            ric=((rx+rz)/2)+((rx-rz)/2)*mt.cos(2*tetase)+(txz)*mt.sin(2*tetase)
            rjc=((rx+rz)/2)-((rx-rz)/2)*mt.cos(2*tetase)-(txz)*mt.sin(2*tetase)
            tc=-((rx-rz)/2)*mt.sin(2*tetase)+(txz)*mt.cos(2*tetase)
            
            ein=((ex+ez)/2)+((ex-ez)/2)*mt.cos(2*tetapd)+(ecxz)*mt.sin(2*tetapd)
            ejn=((ex+ez)/2)-((ex-ez)/2)*mt.cos(2*tetapd)-(ecxz)*mt.sin(2*tetapd)
            gn=-((ex-ez)/2)*mt.sin(2*tetapd)+(ecxz)*mt.cos(2*tetapd)
            eic=((ex+ez)/2)+((ex-ez)/2)*mt.cos(2* tetasd)+(ecxz)*mt.sin(2* tetasd)
            ejc=((ex+ez)/2)-((ex-ez)/2)*mt.cos(2* tetasd)-(ecxz)*mt.sin(2* tetasd)
            gc=-((ex-ez)/2)*mt.sin(2* tetasd)+(ecxz)*mt.cos(2* tetasd)
            boleano=True
    
        elif((i=="y") and (j=="x")):
    
            tetape=(mt.atan((tyx*2)/(ry-rx))/2)
            tetapd=(mt.atan((ecyx*2)/(ey-ex))/2)
            tetase=(mt.atan(-(ry-rx)/(tyx*2))/2)
            tetasd=(mt.atan(-(ey-ex)/(ecyx*2))/2)
            
            rin=((ry+rx)/2)+((ry-rx)/2)*mt.cos(2*tetape)+(tyx)*mt.sin(2*tetape)
            rjn=((ry+rx)/2)-((ry-rx)/2)*mt.cos(2*tetape)-(tyx)*mt.sin(2*tetape)
            tn=-((ry-rx)/2)*mt.sin(2*tetape)+(tyx)*mt.cos(2*tetape)
            ric=((ry+rx)/2)+((ry-rx)/2)*mt.cos(2*tetase)+(tyx)*mt.sin(2*tetase)
            rjc=((ry+rx)/2)-((ry-rx)/2)*mt.cos(2*tetase)-(tyx)*mt.sin(2*tetase)
            tc=-((ry-rx)/2)*mt.sin(2*tetase)+(tyx)*mt.cos(2*tetase)
            
            ein=((ey+ex)/2)+((ey-ex)/2)*mt.cos(2*tetapd)+(ecyx)*mt.sin(2*tetapd)
            ejn=((ey+ex)/2)-((ey-ex)/2)*mt.cos(2*tetapd)-(ecyx)*mt.sin(2*tetapd)
            gn=-((ey-ex)/2)*mt.sin(2*tetapd)+(ecyx)*mt.cos(2*tetapd)
            eic=((ey+ex)/2)+((ey-ex)/2)*mt.cos(2* tetasd)+(ecyx)*mt.sin(2* tetasd)
            ejc=((ey+ex)/2)-((ey-ex)/2)*mt.cos(2* tetasd)-(ecyx)*mt.sin(2* tetasd)
            gc=-((ey-ex)/2)*mt.sin(2* tetasd)+(ecyx)*mt.cos(2* tetasd)
            boleano=True
            
        elif((i=="y") and (j=="z")):
            
            tetape=(mt.atan((tyz*2)/(ry-rz))/2)
            tetapd=(mt.atan((ecyz*2)/(ey-ez))/2)
            tetase=(mt.atan(-(ry-rz)/(tyz*2))/2)
            tetasd=(mt.atan(-(ey-ez)/(ecyz*2))/2)
            
            rin=((ry+rz)/2)+(((ry-rz)/2)*mt.cos(2*tetape))+(tyz)*mt.sin(2*tetape)
            rjn=((ry+rz)/2)-(((ry-rz)/2)*mt.cos(2*tetape))-(tyz)*mt.sin(2*tetape)
            tn=-((ry-rz)/2)*mt.sin(2*tetape)+(tyz)*mt.cos(2*tetape)
            ric=((ry+rz)/2)+((ry-rz)/2)*mt.cos(2*tetase)+(tyz)*mt.sin(2*tetase)
            rjc=((ry+rz)/2)-((ry-rz)/2)*mt.cos(2*tetase)-(tyz)*mt.sin(2*tetase)
            tc=-((ry-rz)/2)*mt.sin(2*tetase)+(tyz)*mt.cos(2*tetase)
            
            ein=((ey+ez)/2)+((ey-ez)/2)*mt.cos(2*tetapd)+(ecyz)*mt.sin(2*tetapd)
            ejn=((ey+ez)/2)-((ey-ez)/2)*mt.cos(2*tetapd)-(ecyz)*mt.sin(2*tetapd)
            gn=-((ey-ez)/2)*mt.sin(2*tetapd)+(ecyz)*mt.cos(2*tetapd)
            eic=((ey+ez)/2)+((ey-ez)/2)*mt.cos(2* tetasd)+(ecyz)*mt.sin(2* tetasd)
            ejc=((ey+ez)/2)-((ey-ez)/2)*mt.cos(2* tetasd)-(ecyz)*mt.sin(2* tetasd)
            gc=-((ey-ez)/2)*mt.sin(2* tetasd)+(ecyz)*mt.cos(2* tetasd)
            boleano=True
    
        elif((i=="z") and (j=="x")):
    
            tetape=(mt.atan((tzx*2)/(rz-rx))/2)
            tetapd=(mt.atan((eczx*2)/(ez-ex))/2)
            tetase=(mt.atan(-(rz-rx)/(tzx*2))/2)
            tetasd=(mt.atan(-(ez-ex)/(eczx*2))/2)
            
            rin=((rz+rx)/2)+((rz-rx)/2)*mt.cos(2*tetape)+(tzx)*mt.sin(2*tetape)
            rjn=((rz+rx)/2)-((rz-rx)/2)*mt.cos(2*tetape)-(tzx)*mt.sin(2*tetape)
            tn=-((rz-rx)/2)*mt.sin(2*tetape)+(tzx)*mt.cos(2*tetape)
            ric=((rz+rx)/2)+((rz-rx)/2)*mt.cos(2*tetase)+(tzx)*mt.sin(2*tetase)
            rjc=((rz+rx)/2)-((rz-rx)/2)*mt.cos(2*tetase)-(tzx)*mt.sin(2*tetase)
            tc=-((rz-rx)/2)*mt.sin(2*tetase)+(tzx)*mt.cos(2*tetase)
            
            ein=((ez+ex)/2)+((ez-ex)/2)*mt.cos(2*tetapd)+(eczx)*mt.sin(2*tetapd)
            ejn=((ez+ex)/2)-((ez-ex)/2)*mt.cos(2*tetapd)-(eczx)*mt.sin(2*tetapd)
            gn=-((ez-ex)/2)*mt.sin(2*tetapd)+(eczx)*mt.cos(2*tetapd)
            eic=((ez+ex)/2)+((ez-ex)/2)*mt.cos(2* tetasd)+(eczx)*mt.sin(2* tetasd)
            ejc=((ez+ex)/2)-((ez-ex)/2)*mt.cos(2* tetasd)-(eczx)*mt.sin(2* tetasd)
            gc=-((ez-ex)/2)*mt.sin(2* tetasd)+(eczx)*mt.cos(2* tetasd)
            boleano=True
    
        elif((i=="z") and (j=="y")):
    
            tetape=(mt.atan((tzy*2)/(rz-ry))/2)
            an1=round(tetape*(180/mt.pi),2)
            tetapd=(mt.atan((eczy*2)/(ez-ey))/2)
            an2=round(tetapd*(180/mt.pi),2)
            tetase=(mt.atan(-(rz-ry)/(tzy*2))/2)
            an3=round(tetase*(180/mt.pi),2)
            tetasd=(mt.atan(-(ez-ey)/(eczy*2))/2)
            an4=round(tetasd*(180/mt.pi),2)
            
            rin=((rz+ry)/2)+((rz-ry)/2)*mt.cos(2*tetape)+(tzy)*mt.sin(2*tetape)
            rinapprox=round(rin,2)
            rjn=((rz+ry)/2)-((rz-ry)/2)*mt.cos(2*tetape)-(tzy)*mt.sin(2*tetape)
            rjnapprox=round(rjn,2)
            tn=-((rz-ry)/2)*mt.sin(2*tetape)+(tzy)*mt.cos(2*tetape)
            tnapprox=round(tn,2)
            ric=((rz+ry)/2)+((rz-ry)/2)*mt.cos(2*tetase)+(tzy)*mt.sin(2*tetase)
            ricapprox=round(ric,2)
            rjc=((rz+ry)/2)-((rz-ry)/2)*mt.cos(2*tetase)-(tzy)*mt.sin(2*tetase)
            rjcapprox=round(rjc,2)
            tc=-((rz-ry)/2)*mt.sin(2*tetase)+(tzy)*mt.cos(2*tetase)
            tcapprox=round(tc,2)
            
            ein=((ez+ey)/2)+((ez-ey)/2)*mt.cos(2*tetapd)+(eczy)*mt.sin(2*tetapd)
            einapprox=round(ein,2)
            ejn=((ez+ey)/2)-((ez-ey)/2)*mt.cos(2*tetapd)-(eczy)*mt.sin(2*tetapd)
            ejnapprox=round(ejn,2)
            gn=-((ez-ey)/2)*mt.sin(2*tetapd)+(eczy)*mt.cos(2*tetapd)
            gnapprox=round(gn,2)
            eic=((ez+ey)/2)+((ez-ey)/2)*mt.cos(2* tetasd)+(eczy)*mt.sin(2* tetasd)
            eicapprox=round(eic,2)
            ejc=((ez+ey)/2)-((ez-ey)/2)*mt.cos(2* tetasd)-(eczy)*mt.sin(2* tetasd)
            ejcapprox=round(ejc,2)
            gc=-((ez-ey)/2)*mt.sin(2* tetasd)+(eczy)*mt.cos(2* tetasd)
            gcapprox=round(gc,2)

            boleano=True
        else:
            mb.showerror(message="La opcion digitada para el valor de i o j no es valida", title="Error i o j")
        

        if boleano==True:
            self.angulo1.set(an3)
            self.angulo2.set(an1)
            self.angulo3.set(an4)
            self.angulo4.set(an2)

            self.esfuerzo1.set(rinapprox)
            self.esfuerzo2.set(rjnapprox)
            self.esfuerzo3.set(tnapprox)
            self.esfuerzo4.set(ricapprox)
            self.esfuerzo5.set(rjcapprox)
            self.esfuerzo6.set(tcapprox)

            self.deformacion1.set(einapprox)
            self.deformacion2.set(ejnapprox)
            self.deformacion3.set(gnapprox)
            self.deformacion4.set(eicapprox)
            self.deformacion5.set(ejcapprox)
            self.deformacion6.set(gcapprox)

    
        
        

if __name__=="__main__":
    ventana=Tk()
    aplicacion=Aplicacion(ventana)
    ventana.mainloop()


