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
    y_f = v_0 * (t - t_0) - g * (t - t_0) ** 2
    return y_f
#la ecuacion de la velocidad de un cuerpo en caida libre es
def v(t):
    v_f = v_0 - g * (t - t_0)
    return v_f

#especializo las ecuaciones
t_0 = 0 #s
v_0 = 3 #m/s
g = 9.8 #m/s ** 2
t = 5 #s
print(y(t))

