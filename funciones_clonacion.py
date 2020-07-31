import os
import shutil
import platform
from datetime import *
import time
from tkinter import filedialog
from tkinter import messagebox


def obtener_origen(tipo_clonacion):
    base = os.getcwd()

    diccio_rutas = {
        "mantenimiento": f"{s}data{s}ORDEN_MNTO{s}Origen{s}Plantilla_Mantenimiento.pdf",
        "alcantarillado": f"{s}data{s}ORDEN_ALCANTARILLADO{s}Origen{s}Plantilla_Alcantarillado.pdf",
        "fuentes": f"{s}data{s}ORDEN_FUENTE{s}Origen{s}Plantilla_Fuente.pdf",
        "residuos cornella": f"{s}data{s}RESIDUOS{s}Origen{s}Plantilla_Res_Cornella.pdf",
        "residuos hospitalet": f"{s}data{s}RESIDUOS{s}Origen{s}Plantilla_Res_Hospitalet.pdf",
        "residuos santacoloma": f"{s}data{s}RESIDUOS{s}Origen{s}Plantilla_Res_SantaColoma.pdf",
        "residuos recogidas": f"{s}data{s}ORDEN_MNTO{s}Origen{s}Plantilla_Res_Recogidas.pdf"
    }

    return base + diccio_rutas[tipo_clonacion]


def obtener_destino(tipo_clonacion):
    base = os.getcwd()

    diccio_rutas = {
        "mantenimiento": f"{s}data{s}ORDEN_MNTO{s}Destino{s}",
        "alcantarillado": f"{s}data{s}ORDEN_ALCANTARILLADO{s}Destino{s}",
        "fuentes": f"{s}data{s}ORDEN_FUENTE{s}Destino{s}",
        "residuos cornella": f"{s}data{s}RESIDUOS{s}Destino{s}RESIDUOS_CORNELLA{s}",
        "residuos hospitalet": f"{s}data{s}RESIDUOS{s}Destino{s}RESIDUOS_HOSPITALET{s}",
        "residuos santacoloma": f"{s}data{s}RESIDUOS{s}Destino{s}RESIDUOS_SANTACOLOMA{s}",
        "residuos recogidas": f"{s}data{s}RESIDUOS{s}Destino{s}RESIDUOS_RECOGIDAS{s}"
    }

    diccio_meses = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre"
    }

    destino = diccio_rutas[tipo_clonacion]
    destino = destino + time.strftime(f"%Y")

    hoy = date.today()
    presente = hoy
    un_dia = timedelta(days=1)
    fecha_str = hoy.strftime(f"%Y%m%d")

    hora = int(hoy.strftime(f"%H"))

    if hora < 8:
        hoy = hoy - un_dia
        fecha_str = hoy.strftime(f"%Y%m%d")

    if tipo_clonacion == "mantenimiento":
        destino = (
                destino +
                time.strftime(
                    f"{s}Semana_%W{s}MANT_{fecha_str}.pdf"
                )
        )

    elif tipo_clonacion == "alcantarillado":
        destino = (
                destino +
                time.strftime(
                    f"{s}%m_{diccio_meses[hoy.strftime(f'%m')]}{s}ALCANT_{fecha_str}.pdf"
                )
        )

    elif tipo_clonacion == "fuentes":
        destino = (
                destino +
                time.strftime(
                    f"{s}%m_{diccio_meses[hoy.strftime(f'%m')]}{s}FUENT_{fecha_str}"
                )
        )

    elif tipo_clonacion == "residuos hospitalet":
        dia_int = int(hoy.strftime(f"%d"))
        un_mes = timedelta(weeks=2)  # Dos semanas más, para que caiga en el mes siguiente

        if dia_int > 21:
            presente = presente + un_mes

        destino = (
                destino +
                time.strftime(
                    f"{s}Hospitalet_Hasta_el_21_de_{diccio_meses[presente.strftime(f'%m')]}"
                    f"_de_{presente.strftime(f'%Y')}.pdf"
                )
        )

    elif tipo_clonacion == "residuos cornella":
        dia_int = int(hoy.strftime(f"%d"))
        un_mes = timedelta(weeks=2)  # Dos semanas más, para que caiga en el mes siguiente

        if dia_int > 21:
            presente = presente + un_mes

        destino = (
                destino +
                time.strftime(
                    f"{s}Cornella_Hasta_el_21_de_{diccio_meses[presente.strftime(f'%m')]}"
                    f"_de_{presente.strftime(f'%Y')}.pdf"
                )
        )

    elif tipo_clonacion == "residuos santacoloma":
        dia_int = int(hoy.strftime(f"%d"))
        un_mes = timedelta(weeks=2)  # Dos semanas más, para que caiga en el mes siguiente

        if dia_int > 21:
            presente = presente + un_mes

        destino = (
                destino +
                time.strftime(
                    f"{s}SantaColoma_Hasta_el_21_de_{diccio_meses[presente.strftime(f'%m')]}"
                    f"_de_{presente.strftime(f'%Y')}.pdf"
                )
        )

    elif tipo_clonacion == "residuos recogidas":
        destino = (
                destino +
                time.strftime(
                    f"{s}Recogidas_{diccio_meses[presente.strftime(f'%m')]}{presente.strftime(f'%Y')}.pdf"
                )
        )

    return base + destino


# Prepara una cadena con únicamente los directorios
def preparar_directorio(directorio_string):
    directorios_ = directorio_string.split(f'{s}')
    i = 1
    directorio_destino = ""

    while i < len(directorios_) - 1:
        directorio_destino = directorio_destino + (s + directorios_[i])
        i += 1

    return directorio_destino


# Método que realiza la clonación de cualquier clase de plantilla
def clonar_plantilla(tipo):
    global s
    tipo_clonacion = ""

    if platform.system() == "Windows":
        s = r"\\"
    elif platform.system() == "Linux":
        s = r"/"

    if tipo == 0:  # Clona mantenimiento
        tipo_clonacion = "mantenimiento"
    elif tipo == 1:  # Clona alcantarillado
        tipo_clonacion = "alcantarillado"
    elif tipo == 2:  # Clona fuentes
        tipo_clonacion = "fuentes"
    elif tipo == 3:  # Clona residuos de Cornellà
        tipo_clonacion = "residuos cornella"
    elif tipo == 4:  # Clona residuos de Hospitalet
        tipo_clonacion = "residuos hospitalet"
    elif tipo == 5:  # Clona residuos de Santa Coloma
        tipo_clonacion = "residuos santacoloma"
    elif tipo == 6:  # Clona recogida de residuos
        tipo_clonacion = "residuos recogidas"

    origen = obtener_origen(tipo_clonacion)
    destino = obtener_destino(tipo_clonacion)

    # Se prepara la ruta de carpetas de origen
    ruta_directorios = preparar_directorio(origen)
    print(ruta_directorios)
    os.makedirs(ruta_directorios, exist_ok=True)

    # Se comprueba que el archivo de origen existe, en caso contrario se localiza y se copia a ORIGEN.
    if not os.path.exists(origen):
        archivo_origen = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Seleccione archivo de origen", filetypes=(('pdf files', '*.pdf'),)
        )
        print(archivo_origen)
        shutil.copy(archivo_origen, origen)

    # Se prepara la ruta de carpetas de destino
    ruta_directorios = preparar_directorio(destino)
    print(ruta_directorios)
    os.makedirs(ruta_directorios, exist_ok=True)

    # Se comprueba que el archivo de destino existe, en caso contrario se localiza y se copia a DESTINO.
    if not os.path.exists(destino):
        shutil.copy(origen, destino)
        messagebox.showinfo(title="Aviso", message="El archivo ha sido clonado correctamente.")
    else:
        messagebox.showwarning(title="Error", message="El archivo ya fue clonado.")
