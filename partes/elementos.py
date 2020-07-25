
class objectoBase:
    def __init__(self, **kwargs):
        self.tipo = "null"
        self.__dict__.update(kwargs)

class Apofisis(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "apofisis"

class Agujero(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "agujero"

class Borde(objectoBase):
    def __init__(self, direccion, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "borde"
        self.direccion = direccion

class Cabeza(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "cabeza"

class Cara(objectoBase):
    def __init__(self, direccion, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "cara"
        self.direccion = direccion

class CavidadArticular(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "cavidad articular"

class Cuerpo(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "cuerpo"

class Cóndilo(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "cóndilo"

class Cresta(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "cresta"

class Eminencia(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "eminencia"

class Escotadura(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "escotadura"

class Espina(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "espina"

class Extremidad(objectoBase):
    def __init__(self, direccion, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "extremidad"
        self.direccion = direccion

class Fosa(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "fosa"

class Fila(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "fila"

class Labio(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "labio"

class Linea(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "línea"

class Parte(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "parte"

class Superficie(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "superficie"

class Tuberosidad(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "tuberosidad"


class Hueso():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Region(): # used por ejemplo para agrupar los tarsos del pie
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Plano(): # used por ejemplo para agrupar los tarsos del pie
    def __init__(self, nombre, **kwargs):
        self.__dict__.update(kwargs)
        self.nombre = nombre

class Musculo():
    def __init__(self, nombre, origen, insercion, inervacion="desconocido", irrigacion="desconocido"):
        self.nombre = nombre
        self.origen = origen 
        self.insercion = insercion
        self.inervacion = inervacion
        self.irrigacion = irrigacion

class Grupo(): # used por ejemplo para agrupar los tarsos del pie
    def __init__(self, nombre, regiones, **kwargs):
        self.__dict__.update(kwargs)
        self.nombre = nombre
        self.regiones = regiones

# femur = Hueso(
#     cupero=Cuerpo(
#        caras=[
#            Cara("anterior"),
#            Cara("interna"),
#            Cara("lateral")
#        ],
#        bordes=[
#            Borde("posterior",
#                 nombre="línea áspera",
#                 labios=[
#                     "interna",
#                     "externo"
#                 ],
#                 intersticio="intersticio",
#                 ramas=[
#                     "rama de trifurcación externa",
#                     "rama de trifurcación media",
#                     "rama de trifurcación interna",
#                 ],
#                 lineas=[
#                     "líneas supracondílea interna",
#                     "líneas supracondílea externa",
#                 ],
#                 agujero="nutricio"
#            ),
#            "externo",
#            "interno"
#        ] 
#     ),
#     extremidad_superior=Extremidad("superior",
#         cabeza=Cabeza(
#             fostia="fostia del ligamento redondo"
#         ),
#         cuellos=[
#             "cuello anatómico",
#             "cuello quirúrgico"
#         ],
#         trocanter_mayor=Eminencia(
#             fosa="digital", 
#             cara="cara interna",
#             bordes=[
#                 "borde anterior",
#                 "borde posterior",
#                 "borde superior",
#                 "borde inferior"
#             ]        
#         ),
#         trocanter_menor="trocanter menor",
#         crestas=[
#             Cresta(
#                 nombre="cresta intertrocantérea anterior",
#                 tubérculos=[
#                     "pretrocantéreo",
#                     "pretrocantíneo"
#                 ]
#             ),
#             "cresta intertrocantérea posterior"
#         ]
#     ),
#     extremidad_inferior=Extremidad("inferior",
#         cóndilos=[
#             Cóndilo(
#                 direccion="interno",
#                 caras=[
#                     "anterior",
#                     "inferior",
#                     "posterior",
#                     "interna",
#                     Cara("externa", tuberosidad="tuberosidad")
#                 ],
#                 tubérculo="tubérculo del aductor"
#             ),
#             Cóndilo(
#                 direccion="externo",
#                 caras=[
#                     "anterior",
#                     "inferior",
#                     "posterior",
#                     "interna",
#                     Cara("externa", tuberosidad="tuberosidad")
#                 ],
#                 fositas=[
#                     Fosa(direccion="superior", nombre="fosita del músculo gemelo externo"),
#                     Fosa(direccion="inferior", nombre="fosita del músculo poplíteo")
#                 ]
#             )
#         ],
#         tróclea="tróclea femoral",
#         fosa="fosa intercondílea",

#     )
# )

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

# coxal = Hueso(
#     caras=[
#         Cara("lateral", 
#             cavidad_articular=CavidadArticular(
#                 borde="acetabular",
#                 escotaduras=[
#                     "iliosquiática",
#                     "iliopúbica",
#                     "acetabular"
#                 ],
#                 partes=[
#                     Parte(tipo="no articular", fosa="fosa acetabular"),
#                     Parte(tipo="articular", carilla="semilunar")
#                 ]
#             ),
#             fosa=Fosa(
#                 nombre="ilíaca externa",
#                 lineas=[
#                     "glútea anterior",
#                     "glútea posterior"
#                 ],
#                 partes=[
#                     "posterior",
#                     "media",
#                     "anterior"
#                 ]
#             ),
#             surco="supraacetabular",
#             agujeros=[
#                 "nutricio",
#                 "obturador"
#             ]
#         ),
#         Cara("interna",
#             fosa="ilíaca interna",
#             tuberosidad="ilíaca",
#             carilla="auricular", # para el sacro
#             superficie="cuadrilátera"
#         )
#     ],
#     bordes=[
#         Borde("anterior",
#             espinas=[
#                 "ilíaca anterior superior",
#                 "iliáca anterior inferior",
#                 "púbica",
#             ],
#             escotaduras=[
#                 "innominada",
#                 "del psoas ilíaco"
#             ],
#             eminencia="iliopectínea",
#             superficie="pectínea",
#             crestas=[
#                 "pectínea",
#                 "del pubis"
#             ]
#         ),
#         Borde("posterior",
#             espinas=[
#                 "ilíaca posterosuperior",
#                 "ilíaca posteroinferior",
#                 "ciática"
#             ],
#             escotaduras=[
#                 "innominada",
#                 "ciática mayor",
#                 "ciática menor"
#             ],
#             tuberosidad="isquiática"
#         ),
#         Borde("superior",
#             nombre="Cresta Ilíaca",
#             labios=[
#                 "interno",
#                 "externo"
#             ],
#             línea="intermedia"
#         ),
#         Borde("inferior",
#             carilla="articular del sínfisis pubiana",
#             rama="isquiopubiana"
#         )
#     ],
#     angulos=[
#         "anterosuperior", # espina iliaca anterosuperior
#         "posteriorsuperior", # espina iliaca posterosuperior
#         "medial", # angulo del pubis
#         "posteroinferior" # tuberosidad isquiática
#     ],
#     partes=[
#         Parte(nombre="pubis",
#             ramas=[
#                 "ascendente",
#                 "descendente"
#             ]
#         ),
#         Parte(nombre="isquion",
#             ramas=[
#                 "ascendente",
#                 "descendente"
#             ]
#         )
#     ]
# )

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

# tarso = Region(
#     filas=[
#         Fila(orden="primera", elementos=[astrágalo, calcáneo]),
#         Fila(orden="segunda", elementos=[cuboides, primera_cueiforme, segunda_cueiforme, tercera_cueiforme]),
#     ]
# )

# musculos = []
# musculo_glúteo_mayor = Musculo(
#     inserciones=[

#     ]
# )
# musculo_glúteo_mediano = Musculo(
#     inserciones=[

#     ]
# )
# musculo_glúteo_menor = Musculo(
#     inserciones=[

#     ]
# )

# musculos_del_miembro_inferior = Region(
#     regiones = [
#         Region(
#             nombre="glutea",
#             planos=[
#                 Plano("superficial",
#                     musculos = [
#                         musculo_glúteo_mayor
#                     ]
#                 ),
#                 Plano("medio",
#                     musculos = [
#                         musculo_glúteo_mediano
#                     ]
#                 ),
#                 Plano("profundo",
#                     musculos = [
#                         musculo_glúteo_menor
#                     ]
#                 )
#             ]
#         )
#     ]
# )
# musculo_peroneo_lateral_largo = Musculo(inserciones=[perone.extremidad_superior])
# musculos.append(musculo_peroneo_lateral_largo)


# for musculo in musculos:
#     for insercion in musculo.inserciones:
#         if insercion == perone.extremidad_superior:
#             print("WE FOUND IT", musculo)