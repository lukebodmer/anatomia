import copy 

from ..elementos import Hueso, Region


vertebra = [
    "vertebra",
    ["agujero vertebral",
    "apofisis espinosa",
    "lamina",
    "apofisis articular superior",
    "apófisis articular inferior"],
    {"apofisis transversa": (
        ["carilla articular"],
        {}
    )
    }
]

C3 = copy.deepcopy(vertebra)
C4 = copy.deepcopy(vertebra)
C5 = copy.deepcopy(vertebra)
C6 = copy.deepcopy(vertebra)
C7 = copy.deepcopy(vertebra)

T1 = copy.deepcopy(vertebra)
T2 = copy.deepcopy(vertebra)
T3 = copy.deepcopy(vertebra)
T4 = copy.deepcopy(vertebra)
T5 = copy.deepcopy(vertebra)
T6 = copy.deepcopy(vertebra)
T7 = copy.deepcopy(vertebra)
T8 = copy.deepcopy(vertebra)
T9 = copy.deepcopy(vertebra)
T10 = copy.deepcopy(vertebra)
T11 = copy.deepcopy(vertebra)
T12 = copy.deepcopy(vertebra)

L1 = copy.deepcopy(vertebra)
L2 = copy.deepcopy(vertebra)
L3 = copy.deepcopy(vertebra)
L4 = copy.deepcopy(vertebra)
L5 = copy.deepcopy(vertebra)

vertebras = [C3,C4,C5,C6,C7,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,L1,L2,L3,L4,L5]
vertebra_nombres = ["C3","C4","C5","C6","C7","T1","T2","T3","T4","T5","T6","T7","T8","T9","T10","T11","T12","L1","L2","L3","L4","L5"]

for index, value in enumerate(vertebras):
    value[0] = vertebra_nombres[index]
    tuple(value)

sacro = (
    ["base",
    "vertice"],
    {"cara anterior" : (
        ["crestas transverales",
        "agujeros sacros anteriores"],
        {}
    ),
    "cara posterior" : (
        ["cresta sacra",
        "astas del sacro",
        "canales sacros",
        "tubérculos sacros posterointernos",
        "agujeros sacros posteriores",
        "tubérculos sacros posteroexternos"],
        {}
    )}
)

cóccix = (
    ["cara anterior",
    "cara posterior",
    "vertice"],
    {}
)

huesos_de_la_columna_cervical = Region(
    nombre="huesos de la columna cervical",
    huesos=[
        C3,
        C4,
        C5,
        C6,
        C7
    ]
)

huesos_de_la_columna_dorsal = Region(
    nombre="huesos de la columna dorsal",
    huesos=[
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        T8,
        T9,
        T10,
        T11,
        T12,
    ]
)

huesos_de_la_columna_lumbar = Region(
    nombre="huesos de la columna lumbar",
    huesos=[
        L1,
        L2,
        L3,
        L4,
        L5
    ]
)


