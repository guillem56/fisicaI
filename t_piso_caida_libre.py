from sympy import symbols, solve

t = symbols("t")
sol = solve(1.5 + 3 * t - 4.9 * t**2)

for i, solution in enumerate(sol):
    print("la solucion n", i, "es:", solution)
