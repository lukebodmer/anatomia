from ..elementos import (
    Hueso, 
    Borde, 
    Cara, 
    Cabeza, 
    CavidadArticular,
    Cóndilo, 
    Cresta, 
    Cuerpo, 
    Eminencia, 
    Extremidad, 
    Fosa,
    Parte,
    Tuberosidad,
    Region
    )

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


# perone = Hueso(
#     cuerpo=Cuerpo(
#         caras=[
#             Cara("interna", cresta="interosea"),
#             Cara("externa", canal="longitudinal"),
#             Cara("posterior", agujero="nutricional")
#         ]
#     ),
#     extremidad_superior=Extremidad("superior", 
#         carilla="articular", 
#         apofisis="estiloides"),
#     extermidad_inferior=Extremidad("inferior", 
#         apofisis="maleolo externo")
# )

# tibia = Hueso(
#     cuerpo=Cuerpo(
#         caras=[
#             Cara("anterointerna"),
#             Cara("anteroexterna"),
#             Cara("posterior", linea="oblicua", agujero="nutricio")
#         ],
#         bordes=[
#             Borde("anterior"),
#             Borde("interno"),
#             Borde("externo")
#         ]
#     ),
#     extermidad_superior=Extremidad("superior", 
#         tuberosidades=[
#             Tuberosidad(direccion="externa", carilla="peronea", tubérculo="tubérculo de Gerdy"),
#             Tuberosidad(direccion="interna", canal="canal transversal")
#             ], 
#         espina="espina de la tibia"),
#     extremidad_inferior=Extremidad("inferior",
#         caras=[
#             Cara("anterior"),
#             Cara("posterior"),
#             Cara("interna", maleolo="maleolo interno"),
#             Cara("externa", escotadura="peronea"),
#             Cara("inferior")
#         ],
#     )
# )

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
    "borde superior" : (
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

# astrágalo = Hueso(
#     cuerpo="cuerpo",
#     cuello="cuello",
#     caras=[
#         Cara("superior",
#             tróclea="tróclea astragalina",
#         ),
#         "inferior",
#         "maleolar lateral",
#         "maleolar medial",
#         "posterior",
#         "anterior"
#     ]
# )

# calcáneo = Hueso(
#     caras=[
#         "superior"
#         "inferior",
#         "lateral",
#         "medial",
#         "posterior",
#         "anterior"
#     ]
# )

# cuboides = Hueso(
#     caras=[
#         "superior"
#         "inferior",
#         "lateral",
#         "medial",
#         "posterior",
#         "anterior"
#     ]
# )

# escafoides = Hueso(
#     caras=[
#         "superior"
#         "inferior",
#         "lateral",
#         "medial",
#         "posterior",
#         "anterior"
#     ]
# )

# primera_cueiforme = Hueso(
#     caras=[
#         "superior"
#         "inferior",
#         "lateral",
#         "medial",
#         "posterior",
#         "anterior"
#     ]
# )

# segunda_cueiforme = Hueso(
#     caras=[
#         "superior"
#         "inferior",
#         "lateral",
#         "medial",
#         "posterior",
#         "anterior"
#     ]
# )

# tercera_cueiforme = Hueso(
#     caras=[
#         "superior"
#         "inferior",
#         "lateral",
#         "medial",
#         "posterior",
#         "anterior"
#     ]
# )

huesos_del_miembro_inferior = Region(
    nombre="huesos del miembro inferior",
    huesos=[
        coxal,
        femur,
        # tibia,
        # perone,
        # astrágalo,
        # calcáneo,
        # cuboides,
        # escafoides,
        # primera_cueiforme,
        # segunda_cueiforme,
        # tercera_cueiforme,
    ]
)

# huesos_del_pie = [
#     astrágalo,
#     calcáneo,
#     cuboides,
#     escafoides,
#     primera_cueiforme,
#     segunda_cueiforme,
#     tercera_cueiforme,
# ]