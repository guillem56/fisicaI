
def caidaLibre(y_0, v_0, t_0, t):
    y_f = y_0 + v_0(t - t_0) + 1/2 * g * (t - t_0) ** 2
    v_f = v_0 + g * t
    return (y_f, v_f)

g = 9.8
y_0 = 0
v_0 = 30
t_0 = 0
t = 5
res = caidaLibre(y_0, v_0, t_0, 5)
print(res)
