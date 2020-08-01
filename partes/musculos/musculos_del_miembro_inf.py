from ..elementos import Musculo, Region, Plano, Grupo
from ..huesos.huesos_del_miembro_inf import coxal, femur, tibia, perone, astrágalo, calcáneo

# musculo_ = Musculo(
#     origen=[
        
#     ],
#     insercion=[

#     ],
#     irrigacion=[

#     ],
#     inervacion=[

#     ]
# )


### REGION GLUTEA ###
###### plano superficial
musculo_glúteo_mayor = Musculo(
    nombre="Glúteo Mayor",
    origen=[
        ("1/4 posterior del ", coxal[2]["borde superior o Cresta Ilíaca"][0][1], ""),
        ("", coxal[2]["cara lateral"][1]["fosa ilíaca externa"][0][2] ,"de la fosa ilíaca externa"),
        ("", "" , "")
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

###### plano medio
musculo_glúteo_mediano = Musculo(
    nombre="Glúteo mediano",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

###### plano profundo
musculo_glúteo_menor = Musculo(
    nombre="Glúteo menor",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_piriforme = Musculo(
    nombre="Piriforme",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_gémino_superior = Musculo(
    nombre="Gémino superior",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_gémino_inferior = Musculo(
    nombre="Gémino inferior",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_obturador_interno = Musculo(
    nombre="Obturador interno",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_obturador_externo = Musculo(
    nombre="Obturador externo",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_cuadrado_crural = Musculo(
    nombre="Cuadrado crural",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

### REGION DEL MUSLO
###### region antero externa
######### primer plano
musculo_sartorio = Musculo(
    nombre="Sartorio",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_tensor_de_la_fascia_lata = Musculo(
    nombre="Tensor de la fascia lata",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

######### segundo plano
musculo_recto_anterior = Musculo(
    nombre="recto anterior",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_vasto_externo = Musculo(
    nombre="vasto externo",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)


musculo__vasto_interno = Musculo(
    nombre="vasto interno",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_crural = Musculo(
    nombre="Crural",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_cuadríceps_crural = [musculo_recto_anterior, musculo_vasto_externo, musculo__vasto_interno, musculo_crural]


###### region posterointerna
musculo_pectíneo = Musculo(
    nombre="pectíneo",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_primer_apoximador = Musculo(
    nombre="Primer apoximador",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)
musculo_segundo_aproximador = Musculo(
    nombre="Segundo aproximador",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)
musculo_tercer_aproximador = Musculo(
    nombre="tercer aproximador",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)
musculo_recto_interno = Musculo(
    nombre="recto interno",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)
musculo_bíceps_crural = Musculo(
    nombre="Bíceps crural",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)
musculo_semitendinoso = Musculo(
    nombre="semitendinoso",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)
musculo_semimembranoso = Musculo(
    nombre="semimembranoso",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

### REGION DE LA PIERNA
###### region anterior
######### primer plano
musculo_tibial_anterior = Musculo(
    nombre="Tibial anterior",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_extensor_común_de_los_dedos = Musculo(
    nombre="Extensor común de los dedos",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

######### segundo plano
musculo_peroneo_anterior = Musculo(
    nombre="Peroneo anterior",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_extensor_propio_del_dedo_gordo = Musculo(
    nombre="Extensor propio del dedo gordo",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

###### region posterior
######### primer plano
musculo_gemelos = Musculo(
    nombre="Gemelos",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_sóleo = Musculo(
    nombre="Sóleo",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_plantar_delgado = Musculo(
    nombre="Plantar delgado",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

######### segundo plano
musculo_poplíteo = Musculo(
    nombre="Poplíteo",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_tibial_posterior = Musculo(
    nombre="Tibial posterior",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_flexor_común_de_los_dedos = Musculo(
    nombre="Flexor común de los dedos",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

musculo_flexor_largo_propio_del_dedo_gordo = Musculo(
    nombre="Flexor largo propio del dedo gordo",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

###### region externa
######### primer plano
musculo_peroneo_lateral_largo = Musculo(
    nombre="Peroneo lateral largo",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)
######### segundo plano
musculo_peroneo_lateral_corto = Musculo(
    nombre="Peroneo lateral corto",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)

### REGION DEL PIE
###### region dorsal
musculo_pedio = Musculo(
    nombre="Pedio",
    origen=[
        
    ],
    insercion=[

    ],
    irrigacion=[

    ],
    inervacion=[

    ]
)
###### region plantar
######### region plantar interna
######### region plantar media
######### region plantar externa

######################
###### REGIONES ######
######################
musculos_del_miembro_inferior = Grupo(
    nombre="músculos del miembro inferior",
    regiones=[
        Region(
            nombre="región glutea",
            regiones=[
                Region(
                    nombre="plano superficial",
                    musculos = [
                        musculo_glúteo_mayor
                    ]
                ),
                Region(
                    nombre="plano medio",
                    musculos = [
                        musculo_glúteo_mediano
                    ]
                ),
                Region(
                    nombre="plano profundo",
                    musculos = [
                        musculo_glúteo_menor,
                        musculo_piriforme,
                        musculo_gémino_inferior,
                        musculo_gémino_superior,
                        musculo_obturador_externo,
                        musculo_obturador_interno,
                        musculo_cuadrado_crural
                    ]
                )
            ]
        ),
        Region(
            nombre="musculos del muslo",
            regiones=[
                Region(
                    nombre="región anteroexterna",
                    regiones=[
                        Region(
                            nombre="primer plano",
                            musculos = [
                                musculo_sartorio,
                                musculo_tensor_de_la_fascia_lata
                            ]
                        ),
                        Region(
                            nombre="segundo plano",
                            musculos = [
                                musculo_cuadrado_crural
                            ]
                        ),
                    ]
                ),
                Region(
                    nombre="región posterointerna",
                    musculos = [
                        musculo_pectíneo,
                        musculo_primer_apoximador,
                        musculo_segundo_aproximador,
                        musculo_tercer_aproximador,
                        musculo_recto_anterior,
                        musculo_bíceps_crural,
                        musculo_semitendinoso,
                        musculo_semimembranoso
                    ]
                )
            ]
        ),
        Region(
            nombre="musculos de la pierna",
            regiones=[
                Region(
                    nombre="región anterior",
                    regiones=[
                        Region(
                            nombre="primer plano",
                            musculos = [
                                musculo_tibial_anterior,
                                musculo_extensor_común_de_los_dedos
                            ]
                        ),
                        Region(
                            nombre="segundo plano",
                            musculos = [
                                musculo_peroneo_anterior,
                                musculo_extensor_propio_del_dedo_gordo
                            ]
                        ),
                    ]
                ),
                Region(
                    nombre="región posterior",
                    regiones=[
                        Region(
                            nombre="primer plano",
                            musculos = [
                                musculo_gemelos,
                                musculo_sóleo,
                                musculo_plantar_delgado
                            ]
                        ),
                        Region(
                            nombre="segundo plano",
                            musculos = [
                                musculo_poplíteo,
                                musculo_tibial_anterior,
                                musculo_flexor_común_de_los_dedos,
                                musculo_flexor_largo_propio_del_dedo_gordo
                            ]
                        ),
                    ]
                ),
                Region(
                    nombre="región externa",
                    regiones=[
                        Region(
                            nombre="primer plano",
                            musculos = [
                                musculo_peroneo_lateral_largo
                            ]
                        ),
                        Region(
                            nombre="segundo plano",
                            musculos = [
                                musculo_peroneo_lateral_corto
                            ]
                        ),
                    ]
                )
            ]
        ),
        Region(
            nombre="musculos del pie",
            regiones=[
                Region(
                    nombre="región dorsal",
                    musculos = [
                                
                    ]
                ),
                Region(
                    nombre="región plantar",
                    regiones=[
                        Region(
                            nombre="región plantar interna",
                            musculos = [
                                        
                            ]
                        ),
                        Region(
                            nombre="región plantar media",
                            musculos = [
                                        
                            ]
                        ),
                        Region(
                            nombre="región plantar externa",
                            musculos = [
                                        
                            ]
                        ),
                    ]
                ),
            ]
        )
    ]
)

musculos_de_la_región_glutea = []
musculos_del_muslo = []
musculos_de_la_pierna = []
musculos_del_pie = []