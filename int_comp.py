import sys

def main():

    # Inversión Inicial
    try:
        capital = float(input('Ingresa el capital inicial a invertir: '))
    except ValueError:
        print('El capital inicial debe ser un número')
        sys.exit()
    
    # Tasa/Retorno
    try:
        tasa = float(input('Ingresa el retorno esperado (ejemplo: 3.45): ')) / 100
    except ValueError:
        print('El retorno debe ser un número')
        sys.exit()

    # Periodos
    try:
        periodos = int(input('Ingresa la cantidad de años en la que tu dinero va a crecer: '))
    except ValueError:
        print('La cantidad de años debe ser un número entero')
        sys.exit()

    # Aportes mensuales
    try:
        aportes_mensuales = float(input('¿Harás aportes adicionales a tu inversión? ' \
            + 'de ser así, ingresa el monto mensual de los aportes que vas a hacer, pero ' \
            + 'de no ser así, ingresa el número cero: '))
    except ValueError:
        print('El monto de aportes debe ser un número')
        sys.exit()

    for i in range(periodos + 1):
        # Si es el primer periodo, el capital es el indicado por el usuario,
        # y los intereses, son inicializados con $0
        if i == 0:
            aporte_anual = 0
            total_aportes = aporte_anual
            capital_inicial = capital + total_aportes
            interes_del_periodo = 0
            interes_acumulado = 0
        else:
            # Si hay aportes mensuales, se considera dentro del capital inicial
            # para que el aporte sea considerado en el cálculo de intereses del
            # periodo
            capital_inicial = capital_final
            aporte_anual = aportes_mensuales * 12
            total_aportes += aporte_anual

            interes_del_periodo = capital_inicial * tasa
            interes_acumulado += interes_del_periodo

        capital_final = capital_inicial + interes_del_periodo + aporte_anual
        
    
        print(
            f'Periodo: {i}', 
            f'Capital Ini.: {capital_inicial}',  
            f'Interes periodo: {interes_del_periodo}',
            f'Capital Fin.: {capital_final}', 
            f'Interes Acum: {interes_acumulado}', 
            f'Aportes: {total_aportes}'
        )

#cambio
if __name__ == '__main__':
    main()