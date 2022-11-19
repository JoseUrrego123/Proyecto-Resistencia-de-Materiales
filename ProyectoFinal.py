#Programa que realiza la transformacion de esfuerzos y deformaciones mediante tensores con el objetivos
#de determinar en que angulos y magnitudes ocurren las deformaciones y esfuerzos principales


#Interfaz de usuario

import tkinter as tk #Se importa para crear la ventana
from tkinter import * #Se importa para crear el Label frame
from tkinter import messagebox as mb # Se importa para crear los cuadros emergentes


class Aplicacion: 

    def __init__(self,ventana):
        
        self.ventana=ventana
        self.ventana.title("Calculo de esfuerzos y deformaciones principales mediante tensores")
        marco=LabelFrame(self.ventana,text="Introduzca las constantes")
        marco.grid(row=0,column=0,pady=20,padx=20)

        Label(marco,text="Ingrese el módulo elástico (Pa): ").grid(row=0,column=0) #Recordar pasar el codigo plano a Gigapascales
        self.dato1=DoubleVar(value=None)
        self.me=Entry(marco,textvariable=self.dato1,justify=CENTER).grid(row=0,column=1,pady=10,padx=10) #Modulo elastico

        Label(marco,text="Ingrese el coeficiente de Poison").grid(row=1,column=0)
        self.dato2=DoubleVar(value=None)
        self.po=Entry(marco,textvariable=self.dato2,justify=CENTER).grid(row=1,column=1,pady=10,padx=10) #Coeficiente de Poison


        #Tensor de esfuerzos
        marco1=LabelFrame(self.ventana,text="Introduzca los datos en el tensor de esfuerzos (Mpa): ")
        marco1.grid(row=2,column=0,pady=20,padx=20)

        #Primera fila del tensor de esfuerzos
        Label(marco1,text="σx").grid(row=2,column=0)
        self.dato3=DoubleVar(value=None)
        self.rx=Entry(marco1,textvariable=self.dato3,justify=CENTER).grid(row=3,column=0,pady=10,padx=10)

        Label(marco1,text="𝛕xy").grid(row=2,column=1)
        self.dato4=DoubleVar(value=None)
        self.txy=Entry(marco1,textvariable=self.dato4,justify=CENTER).grid(row=3,column=1,pady=10,padx=10)

        Label(marco1,text="𝛕xz").grid(row=2,column=2)
        self.dato5=DoubleVar(value=None)
        self.txz=Entry(marco1,textvariable=self.dato5,justify=CENTER).grid(row=3,column=2,pady=10,padx=10)

        #Segunda fila del tensor de esfuerzos
        Label(marco1,text="𝛕yx").grid(row=4,column=0)
        self.dato6=DoubleVar(value=None)
        self.tyx=Entry(marco1,textvariable=self.dato6,justify=CENTER).grid(row=5,column=0,pady=10,padx=10)

        Label(marco1,text="σy").grid(row=4,column=1)
        self.dato7=DoubleVar(value=None)
        self.ry=Entry(marco1,textvariable=self.dato7,justify=CENTER).grid(row=5,column=1,pady=10,padx=10)

        Label(marco1,text="𝛕yz").grid(row=4,column=2)
        self.dato8=DoubleVar(value=None)
        self.tyz=Entry(marco1,textvariable=self.dato8,justify=CENTER).grid(row=5,column=2,pady=10,padx=10)

        #Tercer fila del tensor de esfuerzos
        Label(marco1,text="𝛕zx").grid(row=6,column=0)
        self.dato9=DoubleVar(value=None)
        self.tzx=Entry(marco1,textvariable=self.dato9,justify=CENTER).grid(row=7,column=0,pady=10,padx=10)

        Label(marco1,text="𝛕zy").grid(row=6,column=1)
        self.dato10=DoubleVar(value=None)
        self.tzy=Entry(marco1,textvariable=self.dato10,justify=CENTER).grid(row=7,column=1,pady=10,padx=10)

        Label(marco1,text="σz").grid(row=6,column=2)
        self.dato11=DoubleVar(value=None)
        self.rz=Entry(marco1,textvariable=self.dato11,justify=CENTER).grid(row=7,column=2,pady=10,padx=10)

        self.boton1=tk.Button(self.ventana, text="Calcular", command=self.tensordeformacion)
        self.boton1.grid(row=0, column=1)

        marco2=LabelFrame(self.ventana,text="Tensor de deformaciones (m/m): ")
        marco2.grid(row=8,column=0,pady=20,padx=20)

        #Primera fila del tensor de deformaciones

        self.resultado1=DoubleVar()
        Label(marco2,text="εx").grid(row=8,column=0,sticky=W+E)
        #self.label1=Label(marco2,textvariable=self.resultado1).grid(row=9,column=0,pady=10,padx=10)
        self.ex=Entry(marco2,textvariable=self.resultado1,state=DISABLED,justify=CENTER).grid(row=9,column=0,pady=10,padx=10)

        self.resultado2=DoubleVar()
        Label(marco2,text="γxy/2").grid(row=8,column=1)
        #self.label2=Label(marco2).grid(row=9,column=1,pady=10,padx=10)
        self.ecxy=Entry(marco2,textvariable=self.resultado2,state=DISABLED,justify=CENTER).grid(row=9,column=1,pady=10,padx=10)

        self.resultado3=DoubleVar()
        Label(marco2,text="γxz/2").grid(row=8,column=2)
        #self.label3=Label(marco2).grid(row=9,column=2,pady=10,padx=10)
        self.ecxz=Entry(marco2,textvariable=self.resultado3,state=DISABLED,justify=CENTER).grid(row=9,column=2,pady=10,padx=10)

        #Segunda fila del tensor de deformaciones

        self.resultado4=DoubleVar()
        Label(marco2,text="γyx/2").grid(row=10,column=0)
        #self.label4=Label(marco2).grid(row=11,column=0,pady=10,padx=10)
        self.ecyx=Entry(marco2,textvariable=self.resultado4,state=DISABLED,justify=CENTER).grid(row=11,column=0,pady=10,padx=10)

        self.resultado5=DoubleVar()
        Label(marco2,text="εy").grid(row=10,column=1)
        #self.label5=Label(marco2).grid(row=11,column=1,pady=10,padx=10)
        self.ey=Entry(marco2,textvariable=self.resultado5,state=DISABLED,justify=CENTER).grid(row=11,column=1,pady=10,padx=10)

        self.resultado6=DoubleVar()
        Label(marco2,text="γyz/2").grid(row=10,column=2)
        #self.label6=Label(marco2).grid(row=11,column=2,pady=10,padx=10)
        self.ecyz=Entry(marco2,textvariable=self.resultado6,state=DISABLED,justify=CENTER).grid(row=11,column=2,pady=10,padx=10)

        #Tercer fila del tensor de esfuerzos

        self.resultado7=DoubleVar()
        Label(marco2,text="γzx/2").grid(row=12,column=0)
        #self.label7=Label(marco2).grid(row=13,column=0,pady=10,padx=10)
        self.eczx=Entry(marco2,textvariable=self.resultado7,state=DISABLED,justify=CENTER).grid(row=13,column=0,pady=10,padx=10)

        self.resultado8=DoubleVar()
        Label(marco2,text="γzy/2").grid(row=12,column=1)
        #self.label8=Label(marco2).grid(row=13,column=1,pady=10,padx=10)
        self.eczy=Entry(marco2,textvariable=self.resultado8,state=DISABLED,justify=CENTER).grid(row=13,column=1,pady=10,padx=10)

        self.resultado9=DoubleVar()
        Label(marco2,text="εz").grid(row=12,column=2)
        #self.label9=Label(marco2).grid(row=13,column=2,pady=10,padx=10)  
        self.ez=Entry(marco2,textvariable=self.resultado9,state=DISABLED,justify=CENTER).grid(row=13,column=2,pady=10,padx=10)   

    def tensordeformacion(self):
        
        #Tensor de deformaciones

        #Calculo de las deformaciones

    
        e=float(self.dato1.get())
        v=float(self.dato2.get())

        G=(e)/(2*(1+v)) #Modulo de rigidez 

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
    

if __name__=="__main__":
    ventana=Tk()
    aplicacion=Aplicacion(ventana)
    ventana.mainloop()


#Codigo plano

'''import os
import math as mt

os.system("cls")
e=eval(input("Ingrese el modulo elastico (pa): "))
v=eval(input("Ingrese el coeficiente de poison: "))
G=(e)/(2*(1+v)) #Modulo de rigidez

#Componentes de esfuerzo (Normales y cortantes)
#La idea es poner un entry (Tkinter) en cada caso y que el usuario las llene todas

rx=eval(input("Ingrese el esfuerzo normal en x (Mpa)= "))
ry=eval(input("Ingrese el esfuerzo normal en y (Mpa)= "))
rz=eval(input("Ingrese el esfuerzo normal en z (Mpa)= "))

txy=eval(input("Ingrese el esfuerzo cortante en xy (Mpa)= "))
txz=eval(input("Ingrese el esfuerzo cortante en xz (Mpa)= "))
tyx=eval(input("Ingrese el esfuerzo cortante en yx (Mpa)= "))
tyz=eval(input("Ingrese el esfuerzo cortante en yz (Mpa)= "))
tzx=eval(input("Ingrese el esfuerzo cortante en zx (Mpa)= "))
tzy=eval(input("Ingrese el esfuerzo cortante en zy (Mpa)= "))

#Calculo de las deformaciones

ex=(rx/e)-((v/e)*(ry+rz))
ey=(ry/e)-((v/e)*(rx+rz))
ez=(rz/e)-((v/e)*(ry+rx))
ecxy=txy/(2*G)
ecxz=txz/(2*G)
ecyx=tyx/(2*G)
ecyz=tyz/(2*G)
eczx=tzx/(2*G)
eczy=tzy/(2*G)


#Calculo de los angulos, maximos y minimos

i=str(input("Ingrese el valor de i= "))
j=str(input("Ingrese el valor de j= "))

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
    
elif((i=="z") and (j=="y")):
    
    tetape=(mt.atan((tzy*2)/(rz-ry))/2)
    tetapd=(mt.atan((eczy*2)/(ez-ey))/2)
    tetase=(mt.atan(-(rz-ry)/(tzy*2))/2)
    tetasd=(mt.atan(-(ez-ey)/(eczy*2))/2)
    
    rin=((rz+ry)/2)+((rz-ry)/2)*mt.cos(2*tetape)+(tzy)*mt.sin(2*tetape)
    rjn=((rz+ry)/2)-((rz-ry)/2)*mt.cos(2*tetape)-(tzy)*mt.sin(2*tetape)
    tn=-((rz-ry)/2)*mt.sin(2*tetape)+(tzy)*mt.cos(2*tetape)
    ric=((rz+ry)/2)+((rz-ry)/2)*mt.cos(2*tetase)+(tzy)*mt.sin(2*tetase)
    rjc=((rz+ry)/2)-((rz-ry)/2)*mt.cos(2*tetase)-(tzy)*mt.sin(2*tetase)
    tc=-((rz-ry)/2)*mt.sin(2*tetase)+(tzy)*mt.cos(2*tetase)
    
    ein=((ez+ey)/2)+((ez-ey)/2)*mt.cos(2*tetapd)+(eczy)*mt.sin(2*tetapd)
    ejn=((ez+ey)/2)-((ez-ey)/2)*mt.cos(2*tetapd)-(eczy)*mt.sin(2*tetapd)
    gn=-((ez-ey)/2)*mt.sin(2*tetapd)+(eczy)*mt.cos(2*tetapd)
    eic=((ez+ey)/2)+((ez-ey)/2)*mt.cos(2* tetasd)+(eczy)*mt.sin(2* tetasd)
    ejc=((ez+ey)/2)-((ez-ey)/2)*mt.cos(2* tetasd)-(eczy)*mt.sin(2* tetasd)
    gc=-((ez-ey)/2)*mt.sin(2* tetasd)+(eczy)*mt.cos(2* tetasd)

#  Impresion de los datos

print("El angulo de esfuerzo normal es (grados): {:1.2f}".format(tetape*(180/mt.pi)))
print("El angulo de esfuerzo cortante es (grados): {:1.2f}".format(tetase*(180/mt.pi)))
print("El angulo de deformacion normal es (grados): {:1.2f}".format(tetapd*(180/mt.pi)))
print("El angulo de deformacion cortante es (grados): {:1.2f}".format(tetasd*(180/mt.pi)))

#ESFUERZOS PRINCIPALES

print("Ri Normal (Mpa)= {:1.2f}".format(rin))
print("Rj Normal (Mpa)= {:1.2f}".format(rjn))
print("Tij Normal (Mpa)= {:1.2f}".format(tn))
print("Ri Cortante (Mpa)= {:1.2f}".format(ric))
print("Rj Cortante (Mpa)= {:1.2f}".format(rjc))
print("Tij Cortante (Mpa)= {:1.2f}".format(tc))

#DEFORMACIONES PRICIPALES

print("Ei Normal = {:1.2f}".format(ein))
print("Ej Normal = {:1.2f}".format(ejn))
print("Gij Normal = {:1.2f}".format(gn))
print("Ei Cortante = {:1.2f}".format(eic))
print("Ej Cortante = {:1.2f}".format(ejc))
print("Gij Cortante = {:1.2f}".format(gc))'''