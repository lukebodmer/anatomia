import copy 

from ..elementos import Region

esternón = (
    "esternón",
    ["Extremidad inferior o apófisis xifoides",
    "cara posterior"],
    {"cara anteiror": (
        ["líneas transversales",
        "ángulo esternal de Louis",
        "fosita supraxifoidea"],
        {}
    ),
     "Extremidad superior o manubrio": (
        ["escotadura yugular",
        "escotaduras claviculares"],
        {}
    ),
    "borde derecho": (
        ["primera escotadura costal",
        "segunda escotadura costal",
        "tercera escotadura costal",
        "cuarta escotadura costal",
        "quinta escotadura costal",
        "sexta escotadura costal",
        "septima escotadura costal",
        "escotaduras intercostales"],
        {}
    ),
    "borde izquierdo": (
        ["primera escotadura costal",
        "segunda escotadura costal",
        "tercera escotadura costal",
        "cuarta escotadura costal",
        "quinta escotadura costal",
        "sexta escotadura costal",
        "septima escotadura costal",
        "escotaduras intercostales"],
        {}
    )}
)

costilla = [
    "primera costilla",
    ["tubérculo",
    "cuello",
    "angulo",
    "Extremidad anterior"],
    {"cabeza": (
        [],
        {"carilla articular": (
            ["superficie superior",
            "superficie inferior",
            "cresta costal"],
            {}
        )}
    ),
    "cuerpo": (
        ["cara lateral",
        "borde superior",
        "borde inferior"],
        {"cara medial": (
            ["surco costal"],
            {}
        )}
    ),
    "cartilago costal": (
        ["cara anterior",
        "borde superior",
        "borde inferior",
        "cara posterior"],
        {}
    )}
]


tercera_costilla = copy.deepcopy(costilla)
cuarta_costilla = copy.deepcopy(costilla)
quinta_costilla = copy.deepcopy(costilla)
sexta_costilla = copy.deepcopy(costilla)
septima_costilla = copy.deepcopy(costilla)
octava_costilla = copy.deepcopy(costilla)
novena_costilla = copy.deepcopy(costilla)
decima_costilla = copy.deepcopy(costilla)

costillas = [tercera_costilla, cuarta_costilla, quinta_costilla, sexta_costilla, septima_costilla, octava_costilla, novena_costilla, decima_costilla]
costillas_nombres = ["tercera costilla", "cuarta costilla", "quinta costilla", "sexta costilla", "septima costilla", "octava costilla", "novena costilla", "decima costilla"]

for index, value in enumerate(costillas):
    value[0] = costillas_nombres[index]
    tuple(value)

primera_costilla = (
    "primera costilla",
    ["cuello",
    "tubérculo"],
    {"cabeza": (
        ["carilla articular"],
        {}
    ),
    "cuerpo": (
        ["cara inferior",
        "borde medial",
        "borde lateral",
        "extremidad anterior"],
        {"cara superior": (
            ["porción posterior muscular",
            "porción anterior vascular",
            "tubérculo del músculo escaleno anterior o de Lisfranc"],
            {}
        )}
    )}
)

segunda_costilla = (
    "segunda costilla",
    ["cuello",
    "cuerpo",
    "tubérculo",
    "cara superolateral",
    "cara inferomedial"
    "borde superior",
    "borde inferior",
    "extremidad anterior"],
    {"cabeza": (
        [],
        {"carilla articular": (
            ["superficie superior",
            "superficie inferior",
            "cresta costal"],
            {}
        )}
    ),}
)

undécima_costilla = (
    "undécima costilla",
    ["cuello",
    "cuerpo",
    "angulo",
    "cara lateral",
    "cara medial",
    "borde superior",
    "borde inferior"
    "extremidad anterior"],
    {"cabeza": (
        ["carilla articular"],
        {}
    )}
)

duodécima_costilla = (
    "duodécima costilla",
    ["cuello",
    "cuerpo",
    "angulo",
    "cara lateral",
    "cara medial",
    "borde superior",
    "borde inferior"
    "extremidad anterior"],
    {"cabeza": (
        ["carilla articular"],
        {}
    )}
)

cartilago_costal_común = (
    "cartilago costal común",
    ["cara anterior",
        "borde superior",
        "borde inferior",
        "cara posterior"],
    {}
)

huesos_del_torax = Region(
    nombre="huesos del torax",
    huesos=[
        esternón,
        primera_costilla,
        segunda_costilla,
        tercera_costilla,
        cuarta_costilla,
        quinta_costilla,
        sexta_costilla,
        septima_costilla,
        octava_costilla,
        novena_costilla,
        decima_costilla,
        undécima_costilla,
        duodécima_costilla
    ]
)