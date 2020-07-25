from .elementos import Region, Plano
from .musculos.musculos_del_miembro_inf import musculo_glúteo_mayor, musculo_glúteo_mediano, musculo_glúteo_menor


musculos_del_miembro_inferior = Region(
    regiones = [
        Region(
            nombre="glutea",
            planos=[
                Plano("superficial",
                    musculos = [
                        musculo_glúteo_mayor
                    ]
                ),
                Plano("medio",
                    musculos = [
                        musculo_glúteo_mediano
                    ]
                ),
                Plano("profundo",
                    musculos = [
                        musculo_glúteo_menor
                    ]
                )
            ]
        )
    ]
)