

print('Módulo de Nómina')


nombre = input("Favor ingresar el nombre del empleado: ")


sueldo = float(input('Favor ingresar el sueldo del empleado: '))
while sueldo < 16262.50:
    print('El sueldo ingresado es menor al sueldo mínimo. Intente de nuevo.')
    sueldo = float(input('Favor ingresar el sueldo del empleado: '))


sfs = (sueldo * 3.04) / 100
afp = (sueldo * 2.87) / 100
salario_horas = sueldo / 23.83 / 8
horas_extras_pagada = 0
horario_hora_extra = 0
horas_extras_trabajadas = 0

hora_ex_texto = int(input('''EL empleado ha trabajado horas extra:
                             1. Si
                             2. No
                          '''))

if hora_ex_texto == 1:
    horas_extras_trabajadas = float(input("Ingrese las horas extras trabajadas: "))

    horario_hora_extra = int(input('''
        Seleccione el horario de las horas extras:
        1. Diurno
        2. Nocturno
        3. Días feriados
        '''))


if horario_hora_extra == 1:
    tarifa_hora_extra = salario_horas * 1.15
elif horario_hora_extra == 2:
    tarifa_hora_extra = salario_horas * 1.35
elif horario_hora_extra == 3:
    tarifa_hora_extra = salario_horas * 2.00
else:
    print("Opción no válida. Se asumirá tarifa diurna por defecto.")
    tarifa_hora_extra = salario_horas * 1.15


horas_extras_pagada = tarifa_hora_extra * horas_extras_trabajadas


def descuentos_isr(sfs, afp, sueldo, horas_extras_pagada):
    
    sueldo_bruto_anual = (sueldo + horas_extras_pagada) * 12
    ingreso_neto_imponible = sueldo_bruto_anual - (sfs * 12) - (afp * 12)
    
  
    if ingreso_neto_imponible <= 416220:
        isr_anual = 0
    elif ingreso_neto_imponible <= 624329:
        restante = ingreso_neto_imponible - 416220
        isr_anual = (restante * 0.15)
    elif ingreso_neto_imponible <= 867123:
        restante = ingreso_neto_imponible - 624329
        isr_anual = ((restante * 0.20) + 31216)
    else:
        restante = ingreso_neto_imponible - 867123
        isr_anual = ((restante * 0.25) + 79776)
    
    
    isr_mensual = isr_anual / 12
    
    return isr_mensual

isr_mensual = descuentos_isr(sfs, afp, sueldo, horas_extras_pagada)

salario_neto_mensual = sueldo - sfs - afp - isr_mensual + (horas_extras_pagada / 12)

print('----------------------------Comprobante de pago----------------------------------')
print(f'Nombre de Empleado: {nombre}')
print(f'El salario bruto mensual es: RD$ {sueldo:.2f}')
print(f'El salario neto mensual es: RD$ {salario_neto_mensual:.2f}')
print('--------------------------------Descuentos---------------------------------------')
print(f'El SFS mensual a pagar es: RD$ {sfs:.2f}')
print(f'El AFP mensual a pagar es: RD$ {afp:.2f}')
print(f'El ISR mensual a pagar es: RD$ {isr_mensual:.2f}')


