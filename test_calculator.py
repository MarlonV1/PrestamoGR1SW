from calculator import calcular_cuota

def test_cuota_con_interes():
    cuota = calcular_cuota(1000, 12, 12)
    assert round(cuota, 2) == 88.85  # Valor aproximado

def test_cuota_sin_interes():
    cuota = calcular_cuota(1200, 0, 12)
    assert cuota == 100.0
