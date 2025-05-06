fecha_ingresada = input("Ingrese fecha en formato AAAAMMDD:")
mes = fecha_ingresada[4:6]

primer_digito_mes = mes[0]
segundo_digito_mes = mes[1]

es_primer_digito = ('0' <= primer_digito_mes <= '9')
es_segundo_digito = ('0' <= segundo_digito_mes <= '9')

if es_primer_digito:
    if es_segundo_digito:
        nombre_del_mes = ""
        if mes == "01":
            nombre_del_mes = "Enero"
        elif mes == "02":
            nombre_del_mes = "Febrero"
        elif mes == "03":
            nombre_del_mes = "Marzo"
        elif mes == "04":
            nombre_del_mes = "Abril"
        elif mes == "05":
            nombre_del_mes = "Mayo"
        elif mes == "06":
            nombre_del_mes = "Junio"
        elif mes == "07":
            nombre_del_mes = "Julio"
        elif mes == "08":
            nombre_del_mes = "Agosto"
        elif mes == "09":
            nombre_del_mes = "Septiembre"
        elif mes == "10":
            nombre_del_mes = "Octubre"
        elif mes == "11":
            nombre_del_mes = "Noviembre"
        elif mes == "12":
            nombre_del_mes = "Diciembre"
        else:
            print("Número de mes inválido.")

        if nombre_del_mes != "":
            print("El mes es:", nombre_del_mes)

    else:
        print("Formato de mes inválido (el segundo carácter no es número).")
else:
    print("Formato de mes inválido (el primer carácter no es número).")