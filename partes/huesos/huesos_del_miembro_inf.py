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
    Tuberosidad)

femur = Hueso(
    cupero=Cuerpo(
       caras=[
           Cara("anterior"),
           Cara("interna"),
           Cara("lateral")
       ],
       bordes=[
           Borde("posterior",
                nombre="línea áspera",
                labios=[
                    "interna",
                    "externo"
                ],
                intersticio="intersticio",
                ramas=[
                    "rama de trifurcación externa",
                    "rama de trifurcación media",
                    "rama de trifurcación interna",
                ],
                lineas=[
                    "líneas supracondílea interna",
                    "líneas supracondílea externa",
                ],
                agujero="nutricio"
           ),
           "externo",
           "interno"
       ] 
    ),
    extremidad_superior=Extremidad("superior",
        cabeza=Cabeza(
            fostia="fostia del ligamento redondo"
        ),
        cuellos=[
            "cuello anatómico",
            "cuello quirúrgico"
        ],
        trocanter_mayor=Eminencia(
            fosa="digital", 
            cara="cara interna",
            bordes=[
                "borde anterior",
                "borde posterior",
                "borde superior",
                "borde inferior"
            ]        
        ),
        trocanter_menor="trocanter menor",
        crestas=[
            Cresta(
                nombre="cresta intertrocantérea anterior",
                tubérculos=[
                    "pretrocantéreo",
                    "pretrocantíneo"
                ]
            ),
            "cresta intertrocantérea posterior"
        ]
    ),
    extremidad_inferior=Extremidad("inferior",
        cóndilos=[
            Cóndilo(
                direccion="interno",
                caras=[
                    "anterior",
                    "inferior",
                    "posterior",
                    "interna",
                    Cara("externa", tuberosidad="tuberosidad")
                ],
                tubérculo="tubérculo del aductor"
            ),
            Cóndilo(
                direccion="externo",
                caras=[
                    "anterior",
                    "inferior",
                    "posterior",
                    "interna",
                    Cara("externa", tuberosidad="tuberosidad")
                ],
                fositas=[
                    Fosa(direccion="superior", nombre="fosita del músculo gemelo externo"),
                    Fosa(direccion="inferior", nombre="fosita del músculo poplíteo")
                ]
            )
        ],
        tróclea="tróclea femoral",
        fosa="fosa intercondílea",

    )
)

perone = Hueso(
    cuerpo=Cuerpo(
        caras=[
            Cara("interna", cresta="interosea"),
            Cara("externa", canal="longitudinal"),
            Cara("posterior", agujero="nutricional")
        ]
    ),
    extremidad_superior=Extremidad("superior", 
        carilla="articular", 
        apofisis="estiloides"),
    extermidad_inferior=Extremidad("inferior", 
        apofisis="maleolo externo")
)

tibia = Hueso(
    cuerpo=Cuerpo(
        caras=[
            Cara("anterointerna"),
            Cara("anteroexterna"),
            Cara("posterior", linea="oblicua", agujero="nutricio")
        ],
        bordes=[
            Borde("anterior"),
            Borde("interno"),
            Borde("externo")
        ]
    ),
    extermidad_superior=Extremidad("superior", 
        tuberosidades=[
            Tuberosidad(direccion="externa", carilla="peronea", tubérculo="tubérculo de Gerdy"),
            Tuberosidad(direccion="interna", canal="canal transversal")
            ], 
        espina="espina de la tibia"),
    extremidad_inferior=Extremidad("inferior",
        caras=[
            Cara("anterior"),
            Cara("posterior"),
            Cara("interna", maleolo="maleolo interno"),
            Cara("externa", escotadura="peronea"),
            Cara("inferior")
        ],
    )
)

coxal = Hueso(
    caras=[
        Cara("lateral", 
            cavidad_articular=CavidadArticular(
                borde="acetabular",
                escotaduras=[
                    "iliosquiática",
                    "iliopúbica",
                    "acetabular"
                ],
                partes=[
                    Parte(tipo="no articular", fosa="fosa acetabular"),
                    Parte(tipo="articular", carilla="semilunar")
                ]
            ),
            fosa=Fosa(
                nombre="ilíaca externa",
                lineas=[
                    "glútea anterior",
                    "glútea posterior"
                ],
                partes=[
                    "posterior",
                    "media",
                    "anterior"
                ]
            ),
            surco="supraacetabular",
            agujeros=[
                "nutricio",
                "obturador"
            ]
        ),
        Cara("interna",
            fosa="ilíaca interna",
            tuberosidad="ilíaca",
            carilla="auricular", # para el sacro
            superficie="cuadrilátera"
        )
    ],
    bordes=[
        Borde("anterior",
            espinas=[
                "ilíaca anterior superior",
                "iliáca anterior inferior",
                "púbica",
            ],
            escotaduras=[
                "innominada",
                "del psoas ilíaco"
            ],
            eminencia="iliopectínea",
            superficie="pectínea",
            crestas=[
                "pectínea",
                "del pubis"
            ]
        ),
        Borde("posterior",
            espinas=[
                "ilíaca posterosuperior",
                "ilíaca posteroinferior",
                "ciática"
            ],
            escotaduras=[
                "innominada",
                "ciática mayor",
                "ciática menor"
            ],
            tuberosidad="isquiática"
        ),
        Borde("superior",
            nombre="Cresta Ilíaca",
            labios=[
                "interno",
                "externo"
            ],
            línea="intermedia"
        ),
        Borde("inferior",
            carilla="articular del sínfisis pubiana",
            rama="isquiopubiana"
        )
    ],
    angulos=[
        "anterosuperior", # espina iliaca anterosuperior
        "posteriorsuperior", # espina iliaca posterosuperior
        "medial", # angulo del pubis
        "posteroinferior" # tuberosidad isquiática
    ],
    partes=[
        Parte(nombre="pubis",
            ramas=[
                "ascendente",
                "descendente"
            ]
        ),
        Parte(nombre="isquion",
            ramas=[
                "ascendente",
                "descendente"
            ]
        )
    ]
)

astrágalo = Hueso(
    cuerpo="cuerpo",
    cuello="cuello",
    caras=[
        Cara("superior",
            tróclea="tróclea astragalina",
        ),
        "inferior",
        "maleolar lateral",
        "maleolar medial",
        "posterior",
        "anterior"
    ]
)

calcáneo = Hueso(
    caras=[
        "superior"
        "inferior",
        "lateral",
        "medial",
        "posterior",
        "anterior"
    ]
)

cuboides = Hueso(
    caras=[
        "superior"
        "inferior",
        "lateral",
        "medial",
        "posterior",
        "anterior"
    ]
)

escafoides = Hueso(
    caras=[
        "superior"
        "inferior",
        "lateral",
        "medial",
        "posterior",
        "anterior"
    ]
)

primera_cueiforme = Hueso(
    caras=[
        "superior"
        "inferior",
        "lateral",
        "medial",
        "posterior",
        "anterior"
    ]
)

segunda_cueiforme = Hueso(
    caras=[
        "superior"
        "inferior",
        "lateral",
        "medial",
        "posterior",
        "anterior"
    ]
)

tercera_cueiforme = Hueso(
    caras=[
        "superior"
        "inferior",
        "lateral",
        "medial",
        "posterior",
        "anterior"
    ]
)

huesos_del_miembro_inf = [
    coxal,
    femur,
    tibia,
    perone,
    astrágalo,
    calcáneo,
    cuboides,
    escafoides,
    primera_cueiforme,
    segunda_cueiforme,
    tercera_cueiforme,
]

huesos_del_pie = [
    astrágalo,
    calcáneo,
    cuboides,
    escafoides,
    primera_cueiforme,
    segunda_cueiforme,
    tercera_cueiforme,
]