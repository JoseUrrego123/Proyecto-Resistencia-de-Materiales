#Programa que realiza la transformacion de esfuerzos y deformaciones mediante tensores con el objetivos
#de determinar en que angulos y magnitudes ocurren las deformaciones y esfuerzos principales

import os
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
print("Gij Cortante = {:1.2f}".format(gc))