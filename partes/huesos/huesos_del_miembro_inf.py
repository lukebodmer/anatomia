from ..elementos import Hueso, Region


femur = (
    "femur",
    ["tróclea femoral",
    "fosa intercondílea"],
    {"cuerpo" : (
        ["cara anterior",
        "cara interna",
        "cara lateral",
        "borde externo",
        "borde interno"],
        {"borde posterior o línea áspera" : (
            ["labio interna",
            "labio externo",
            "intersticio",
            "rama de trifurcación externa",
            "rama de trifurcación media",
            "rama de trifurcación interna",
            "líneas supracondílea interna",
            "líneas supracondílea externa",
            "agujero nutricio"],
            {}
        )}
        ),
     "extremidad superior" : (
        ["cuello anatómico",
        "cuello quirúrgico",
        "trocanter menor",
        "cresta intertrocantérea posterior"],
        {"cabeza" : (
            ["fostia del ligamento redondo"],
            {}
        ),
        "trocanter mayor" : (
            ["fosa digital",
            "cara interna",
            "borde anterior",
            "borde posterior",
            "borde superior",
            "borde inferior"],
            {}
        ),
        "cresta intertrocantérea anterior" : (
            ["pretrocantéreo",
            "pretrocantíneo"],
            {}
        )
        }
     ),
     "extremidad inferior" : (
        [],
        {"cóndilo interno": (
            ["cara anterior",
            "cara inferior",
            "cara posterior",
            "cara interna",],
            {"cara externa" : (
                ["tuberosidad"],
                {}
            )}
        ),
        "cóndilo externo": (
            ["cara anterior",
            "cara inferior",
            "cara posterior",
            "cara interna",
            "fosita del músculo gemelo externo",
            "fosita del músculo poplíteo"],
            {"cara externa" : (
                ["tuberosidad"],
                {}
            )
            }
        )
        }
     )
    }
)

perone = (
    "perone",
    [],
    {"cara interna" : (
        ["cresta interosea"],
        {}
    ),
    "cara externa" : (
        ["canal longitudinal"],
        {}
    ),
    "cara posterior" : (
        ["agujero nutricional"],
        {}
    ),
    "extremidad superior" : (
        ["carilla articular",
        "apofisis estiloides",
        ],
        {}
    ),
    "extremidad inferior" : (
        ["maleolo externo"],
        {}
    )}
)

tibia = (
    "tibia",
    [],
    {"cuerpo" : (
        ["cara anterointerna",
        "cara anteroexterna",
        "borde anterior"
        "borde externo",
        "borde interno"],
        {"cara posterior" : (
            ["linea oblicua",
            "agujero nutricio"],
            {}
        )
        }
    ),
    "extremidad superior" : (
        ["espina de la tibia",
        "superficie preespinosa",
        "superficie retroespinosa",
        "cavidad glenoidea interna",
        "cavidad glenoidea externa"],
        {"tuberosidad interna" : (
            ["canal transversal"],
            {}
        ),
        "tuberosidad externa" : (
            ["carilla peronea",
            "tubérculo de Gerdy"],
            {}
        )}
    ),
    "extremidad inferior" : (
        ["cara anterior",
        "cara posterior",
        "cara inferior",
        "cara interno"],
        {"cara externa" : (
            ["escotadura peronea"],
            {}
        ),
        "cara interna" : (
            ["maléolo interno"],
            {}
        )
        }
    ),
    }
)


coxal = (
    "coxal",
    ["angulo anterosuperior", # espina iliaca anterosuperior
    "angulo posteriorsuperior", # espina iliaca posterosuperior
    "angulo medial", # angulo del pubis
    "angulo posteroinferior"],
    {"cara lateral" : (
        ["borde acetabular",
        "escotadura iliosquiática",
        "escotadura iliopúbica",
        "escotadura acetabular",
        "parte no artciular o fosa acetabular",
        "parte artciular o semilunar",
        "surco supraacetabular",
        "agujeros nutricio",
        "agujeros obturador" 
        ],
        {"fosa ilíaca externa" : (
            ["linea glútea anterior",
             "linea glútea posterior",
             "parte posterior",
             "parte media",
             "parte anterior"],
             {}
        )}
    ),
    "cara interna" : (
        ["fosa ilíaca interna",
        "tuberosidad ilíaca",
        "carilla auricular",
        "superficie cuadrilátera"],
        {}
    ),
    "borde anterior" : (
        ["espina ilíaca anterior superior",
        "espina iliáca anterior inferior",
        "espina púbica",
        "escotadura innominada",
        "escotaduras del psoas ilíaco",
        "eminencia iliopectínea",
        "superficie pectínea",
        "cresta pectínea",
        "cresta del pubis"],
        {}
    ),
    "borde posterior" : (
        ["espina ilíaca posterosuperior",
        "espina ilíaca posteroinferior",
        "espina ciática",
        "escotadura innominada",
        "escotadura ciática mayor",
        "escotadura ciática menor",
        "tuberosidad isquiática"],
        {}
    ),
    "borde superior o Cresta Ilíaca" : (
        ["labio interno",
        "labio externo",
        "línea intermedia",],
        {}
    ),
    "borde inferior" : (
        ["rama isquiopubiana",
        "carilla articular del sínfisis pubiana"],
        {}
    ),
    "pubis" : (
        ["rama ascendente",
        "rama descendente",],
        {}
    ),
    "isquion" : (
        ["rama ascendente",
         "rama descendente",],
        {}
    )
    }
)

astrágalo = (
    "astrágalo",
    ["cuerpo",
    "cuello",
    "cara inferior",
    "cara maleolar lateral",
    "cara maleolar medial",
    "cara posterior",
    "cara anterior"],
    {"cara superior" : (
        ["tróclea astragalina"],
        {}
    )}
)


calcáneo = (
    "calcáneo",
    ["cara superior"
    "cara inferior",
    "cara lateral",
    "cara medial",
    "cara posterior",
    "cara anterior"],
    {}
)

cuboides = (
    "cuboides",
    ["cara superior"
    "cara inferior",
    "cara lateral",
    "cara medial",
    "cara posterior",
    "cara anterior"],
    {}
)

escafoides = (
    "escafoides",
    ["cara superior"
    "cara inferior",
    "cara lateral",
    "cara medial",
    "cara posterior",
    "cara anterior"],
    {}
)

primera_cueiforme = (
    "primera_cueiforme",
    ["cara superior"
    "cara inferior",
    "cara lateral",
    "cara medial",
    "cara posterior",
    "cara anterior"],
    {}
)

segunda_cueiforme = (
    "segunda_cueiforme",
    ["cara superior"
    "cara inferior",
    "cara lateral",
    "cara medial",
    "cara posterior",
    "cara anterior"],
    {}
)

tercera_cueiforme = (
    "tercera_cueiforme",
    ["cara superior"
    "cara inferior",
    "cara lateral",
    "cara medial",
    "cara posterior",
    "cara anterior"],
    {}
)

huesos_del_pie = Region(
    nombre="huesos del pie",
    huesos=[
        astrágalo,
        calcáneo,
        cuboides,
        escafoides,
        primera_cueiforme,
        segunda_cueiforme,
        tercera_cueiforme,
    ]
)


huesos_del_miembro_inferior = Region(
    nombre="huesos del miembro inferior",
    huesos=[
        coxal,
        femur,
        tibia,
        perone,
    ]
)
