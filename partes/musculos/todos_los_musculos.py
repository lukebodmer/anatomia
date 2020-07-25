from .musculos_del_miembro_inf import musculos_del_miembro_inferior
from ..elementos import Grupo, Region

todos_los_musculos = Grupo(
    nombre="Músculos",
    regiones=[
        musculos_del_miembro_inferior
    ]
)
