def calculapi(lados):
    """
    Esta função vai calcular o pi usando o método do poligono inscrito em uma circunferência de raio 1.
    :param lados: Quantos lados terá o polígono, (quanto mais lados, mais preciso).
    :return: Retorna pi, (o mais preciso que chega é 3.141592653589793).
    """
    from math import sin, cos, radians
    try:
        teta = 360 / lados  # angulo
        meio_teta = teta / 2  # meio angulo
        seno_meio_teta = sin(radians(meio_teta))  # seno
        cos_meio_teta = cos(radians(meio_teta))  # cosseno
        area = cos_meio_teta * seno_meio_teta  # area do triangulo
        pi = area * lados
    except Exception as erro:
        return erro
    return pi


print(calculapi(int(input("numero de lados do polígono: "))))
