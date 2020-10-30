import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize 
"""
Una particula es lanzada verticalmente hacia arriba con una velocidad
de 3 m/s desde una altura de 1,5 metros.
a) Cuanto tiempo tardara en caer al suelo?
b) Con que velocidad llegara al suelo?
"""


#a)
#defino sr con y positivo hacia arriba

#la ecuacion de posicion de un cuerpo en caida libre es
def y(t):
    y_f = y_0 + v_0 * (t - t_0) - 1/2 * g * (t - t_0) ** 2
    return y_f
#la ecuacion de la velocidad de un cuerpo en caida libre es
def v(t):
    v_f = v_0 - g * (t - t_0)
    return v_f

#especializo las ecuaciones
t_0 = 0 #s
y_0 = 1.5 #m
v_0 = 3 #m/s
g = 9.8 #m/s ** 2

x = np.arange(0, 1.5, 0.01)
y_ = y(x)
##plt.plot(x,y_)
##plt.show()
#en el grafico se puede ver que dos puntos corchetes validos que "encierran"
#la raiz son 0.4 y 0.7. Podria usar entonces el metodo de la secante o de
#la biseccion con estos valores para hallar una aproximacion de la raiz
root = optimize.bisect(y, 0.8, 1.2)
print("Metodo de la Biseccion (t cuando llega al piso):", root)
#el metodo de la secante es una de las opciones al metodo de newton.
root = optimize.newton(y, 0.8)
print("Metodo de la Secante (t cuando llega al piso): ", root)
#para de hecho usar el metodo de newton, tengo que calcular la derivada de
#la funcion y, yprima. Pero esto ya esta calculado, es v(t). Tambien tengo que
#dar un valor cercano a la raiz.
root = optimize.newton(y, 0.8, v)
print("Metodo de Newton-Raphson (t cuando llega al piso): ", root)
#tambien puedo usar el metodo de Brent, que es el que aconsejan usar en el
#libro Computational Physics. Esto metodo utiliza dos valores corchete
#que encuerran el valor de la raiz, al igual que el metodo de la biseccion
root = optimize.brentq(y, 0.8, 1.2)
print("Metodo de Brent (t cuando llega al piso): ", root)
#compruebo evaluando el t hallado
t = root
print(y(t))
#la velocidad con la que cuerpo llega al piso es
print(v(t))
#los calculos a mano, a su vez, arrojan que
t = 0.936797
print(y(t))
#los calculos en Mathematica arrojan que
t = 0.938446
print(y(t))
#debo haberme equivocado en las cuentas, porque las raices halladas por
#los programas se acercan mucho mas a cero que mis calculos, siendo la mejor
#aproximacion el valor calculado por python (porque amplia los decimales de la
#solucion que tambien da Mathematica)


#c) en que t alcanza la altura maxima ?
#cuando v_f = 0
#ploteo la velocidad en funcion del tiempo para hallar valores cercanos a la
#raiz y luego utilizo el metodo de la biseccion para hallarla
v_ = v(x)
plt.plot(x, v_)
##plt.show()
#la raiz esta entre 0 y 0.4
root = optimize.brentq(v , 0, 0.4)
print("t cuando v_f = 0 (Brent):", root)
#compruebo con el metodo de la secante.
root = optimize.newton(v, 0)
print("t cuando v_f = 0 (Secante):",root)




