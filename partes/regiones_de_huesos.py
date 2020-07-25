from .elementos import Region, Fila
from .huesos.huesos_del_miembro_inf import astrágalo, calcáneo, cuboides, primera_cueiforme, segunda_cueiforme, tercera_cueiforme


tarso = Region(
    filas=[
        Fila(orden="primera", elementos=[astrágalo, calcáneo]),
        Fila(orden="segunda", elementos=[cuboides, primera_cueiforme, segunda_cueiforme, tercera_cueiforme]),
    ]
)
