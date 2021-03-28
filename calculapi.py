def calculapi(lados):
    """
    Esta função vai calcular o pi usando o método do poligono inscrito em uma circunferência de raio 1.
    This function calculates pi using a polygon inscribed in a circunference of radius 1.
    :param lados: Quantos lados terá o polígono, (quanto mais lados, mais preciso).
                  How many sides will the polygon have, (more sides, more precise).
    :return: Retorna pi, (o mais preciso que chega é 3.141592653589793).
             Returns pi, (the most precise it gets is 3.141592653589793).
    """
    from math import sin, cos, radians
    try:
        if lados < 3:
            lados = 3
        teta = 360 / lados  # angle in degrees
        meio_teta = teta / 2  # half of the angle
        seno_meio_teta = sin(radians(meio_teta))  # sin of the angle to get the side of the triangle (python works in radians)
        cos_meio_teta = cos(radians(meio_teta))  # cos (other side of the triangle)
        area = cos_meio_teta * seno_meio_teta  # area of the triangle
        pi = area * lados
    except Exception as erro:
        return erro
    else:
        return pi
