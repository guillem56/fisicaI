from sympy import symbols, solve

#la funcion de la posicion en la caida libre es
def y(t): #I
    y_f = y_0 + v_0 * (t - t_0) + 1/2 * g * (t - t_0) ** 2
    return y_f

#la funcion de la velocidad en la caida libre es
def v(t): #II
    v_f = v_0 + g * (t - t_0)
    return v_f

#especializo para el ejericio 3 cap 1
#SR: y positivo hacia arriba, y = 0 en el suelo
t_0 = 0
#y_0 = ?
g = -9.8 #m/s**2 
v_0 = 12.25 #m/s
#la pelota llega al suelo (y = 0) cuando
t = 4.25 #s

#sabiendo que y(t=4.25s) = 0m despejo la posicion inicial, y_0
#de I
y_0 = -v_0 * t - 1/2 * g * (t - t_0) **2
print(y_0)
#esto responde la pregunta b) Que altura tiene el edificio?

#estando ahora definidas todas las variables en la funcion y(t), puedo usarla
#para saber la posicion de la particula para todo instante t, por ejemplo, t = 2
print(y(2))

#puedo saber el tiempo en el que llega arriba haciendo v(t) = 0 y despejando t
#de II
t = -v_0 / g
#compruebo
print(v(t))
#a)cual es la altura maxima que alcanza la pelota?
#la posicion en que se alcanza entonces la posicion maxima es
print(y(t))
#compruebo, evaluando en un tiempo un dt menor y un dt mayor
dt = 0.1
print(y(t - dt), y(t), y(t + dt))
