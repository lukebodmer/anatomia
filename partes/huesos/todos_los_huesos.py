from .huesos_del_miembro_inf import huesos_del_miembro_inferior, huesos_del_pie
from .huesos_del_columna_vertebral import (
    huesos_de_la_columna_cervical,
    huesos_de_la_columna_dorsal,
    huesos_de_la_columna_lumbar,
    sacro,
    cóccix
    )
from .huesos_del_torax import huesos_del_torax
from ..elementos import Grupo, Region

todos_los_huesos = Grupo(
    nombre="Huesos",
    regiones=[
        huesos_de_la_columna_cervical,
        huesos_de_la_columna_dorsal,
        huesos_de_la_columna_lumbar,
        huesos_del_torax,
        huesos_del_miembro_inferior,
        huesos_del_pie
    ]
)