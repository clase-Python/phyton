def draw_sierpinski(level):
    def sierpinski(n):
        if n == 0:
            return ["▲"]
        else:
            prev = sierpinski(n - 1)
            top = [row + row for row in prev]
            bottom = [row + " " * len(row) + row for row in prev]
            return top + bottom

    # Generar el triángulo
    triangle = sierpinski(level)
    max_width = len(triangle[-1])

    # Imprimir el triángulo centrado
    for row in triangle:
        print(row.center(max_width))

# Nivel de recursión para el triángulo de Sierpinski
draw_sierpinski(5)
