def calcular_cuota(monto, tasa_anual, plazo_meses):
    r = tasa_anual / 100 / 12
    if r == 0:
        return monto / plazo_meses
    cuota = monto * (r * (1 + r) ** plazo_meses) / ((1 + r) ** plazo_meses - 1)
    return cuota