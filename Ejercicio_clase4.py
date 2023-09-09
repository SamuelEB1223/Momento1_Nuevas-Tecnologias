""" La aplicacion debe permitir registrar ingresos y contar el saldo de estos
debe permitir registrar egresos y mostrar el saldo
si el egreso es mayor que el saldo no debe permitir el registro y mostrara un mensaje de saldo insuficiente
la aplicacion llevara registro de los movimientos indicando el numero de ingresos y de egresos   """

saldo = 0
acumingresos = 0
acumegresos = 0
isOn = int(input("Ingrese 1 para inicializar el servicio: "))

while isOn !=0:

    opc = int(input ("1. ingreso: \n 2. Egreso\n 3. Salir"))

    if opc == 1:
        ingreso = int(input("Registre el ingreso"))

        saldo = saldo + ingreso

        print (f"Su saldo es: {saldo}")
        acumingresos+=1
        print (acumingresos)

    elif opc==2:
        egreso = int(input("Registre el monto a retirar:"))
        saldo = saldo - egreso

        if saldo < 0:
            print("Saldo insuficiente")
            saldo = saldo + egreso
            print (saldo)
            
        else:
            print(f"Su saldo es:$ {saldo}")
            acumegresos+=1
            print(acumegresos)
    elif opc==3:
        print("salir")
        isOn=0
    else:
        print("Ingrese una opcion valida") 

        