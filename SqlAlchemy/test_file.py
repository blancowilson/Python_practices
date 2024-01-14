monedas=[2,1,0.5,0.2,0.1,0.05,0.02,0.01]

resultado = []
def Calcular_Cantidad_Monedas(monto, moneda):
    cantidad_monedas =  monto//moneda
    resto = round(monto%moneda,2)
    return resto,cantidad_monedas

monto = float(input("ingrese el numero a evaluar:"))

for index,moneda in enumerate(monedas):
    if monto >= moneda and (monto//moneda)>0:
        monto,cantidad_monedas = Calcular_Cantidad_Monedas(monto, moneda)
        resultado.append((moneda,cantidad_monedas))
print(resultado)
