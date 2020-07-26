from .huesos_del_miembro_inf import huesos_del_miembro_inferior, huesos_del_pie
from ..elementos import Grupo, Region

todos_los_huesos = Grupo(
    nombre="Huesos",
    regiones=[
        huesos_del_miembro_inferior,
        huesos_del_pie
    ]
)