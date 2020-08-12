import tkinter as tk
from tkinter import *
from funciones_clonacion import *


class VentanaMain:
    def __init__(self, root, version):
        self.bg_color = "#2471a3"
        self.fg_color = "white"
        self.font_init = "Inconsolata 10"
        self.font_sec = "Inconsolata 14 bold"
        self.bg_boton1 = "#2e86c1"
        self.bg_boton2 = "#2ec177"
        self.raiz = root
        self.raiz.title(
            f"CICLON-*** (Clonador Integrado de ***) Versión:{version}"
        )
        self.raiz.resizable(0, 0)
        self.raiz.config(bg=self.bg_color)
        self.init_elementos()
        self.raiz.mainloop()



    def init_elementos(self):
        # Etiquetado principal
        etiq_init = Label(
            self.raiz,
            text="Seleccione uno de los botones " +
            "para realizar la clonación de plantillas:",
            bg=self.bg_color,
            fg=self.fg_color,
            font=self.font_init
        ).grid(row=0, column=0, columnspan=5, sticky=N)

        # Boton para clonar plantilla de mantenimiento.
        boton_mnto = Button(
            self.raiz,
            text="MANTENIMIENTO",
            font=self.font_sec,
            bg=self.bg_boton1,
            fg=self.fg_color,
            width=20,
            height=5,
            command=lambda: clonar_plantilla(tipo=0)
        ).grid(row=1, column=0)

        # Boton para clonar plantilla de alcantarillado.
        boton_alcantarillado = Button(
            self.raiz,
            text="ALCANTARILLADO",
            font=self.font_sec,
            bg=self.bg_boton1,
            fg=self.fg_color,
            width=20,
            height=5,
            command=lambda: clonar_plantilla(tipo=1)
        ).grid(row=1, column=1)

        # Boton para clonar plantilla de fuentes.
        boton_fuentes = Button(
            self.raiz,
            text="FUENTES",
            font=self.font_sec,
            bg=self.bg_boton1,
            fg=self.fg_color,
            width=20,
            height=5,
            command=lambda: clonar_plantilla(tipo=2)
        ).grid(row=1, column=2)

        # Boton para clonar plantilla de residuos cornellà.
        boton_residuos_cornella = Button(
            self.raiz,
            text="RESIDUOS CORNELLÀ",
            font=self.font_sec,
            bg=self.bg_boton1,
            fg=self.fg_color,
            width=20,
            height=1,
            pady=3,
            command=lambda: clonar_plantilla(tipo=3)
        ).grid(row=1, column=3)

        # Boton para clonar plantilla de residuos hospitalet.
        boton_residuos_hospitalet = Button(
            self.raiz,
            text="RESIDUOS HOSPITALET",
            font=self.font_sec,
            bg=self.bg_boton1,
            fg=self.fg_color,
            width=20,
            height=1,
            pady=3,
            command=lambda: clonar_plantilla(tipo=4)
        ).grid(row=1, column=3, sticky=N)

        # Boton para clonar plantilla de residuos santa coloma.
        boton_residuos_stacoloma = Button(
            self.raiz,
            text="RESIDUOS STA.COLOMA",
            font=self.font_sec,
            bg=self.bg_boton1,
            fg=self.fg_color,
            width=20,
            height=1,
            pady=3,
            command=lambda: clonar_plantilla(tipo=5)
        ).grid(row=1, column=3, sticky=S)

        # Boton para clonar plantilla de recogidas de residuos.
        boton_residuos_recogidas = Button(
            self.raiz,
            text="RESIDUOS\nRECOGIDAS",
            font=self.font_sec,
            bg=self.bg_boton1,
            fg=self.fg_color,
            width=8,
            height=5,
            padx=5,
            command=lambda: clonar_plantilla(tipo=6)
        ).grid(row=1, column=4, sticky=N)


app = tk.Tk()
ventana = VentanaMain(app, "1.02b")
app.mainloop()
