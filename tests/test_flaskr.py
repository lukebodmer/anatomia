import os
import tempfile

import pytest


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
    def __init__(self, direccion="gotta fix", **kwargs):
        super().__init__(**kwargs)
        self.tipo = "borde"
        self.direccion = direccion

class Cabeza(objectoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "cabeza"

class Cara(objectoBase):
    def __init__(self, direccion="gotta fix", **kwargs):
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
    def __init__(self, nombre, rasgos, **kwargs):
        self.__dict__.update(kwargs)
        self.nombre = nombre
        self.rasgos = rasgos 


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

# coxal = Hueso(
#     nombre="Coxal",
#     rasgos={
#         "cara lateral" : Cara(
#                             nombre="cara lateral", 
#                             rasgos={
#                                 "cavidad articular" : CavidadArticular(
#                                                             nombre="cavidad articular",
#                                                             rasgos={
#                                                                 "borde acetabular" : "borde acetabular",
#                                                                 "escotadura iliosquiática" : "escotadura iliosquiática",
#                                                                 "escotadura iliopúbica" : "escotadura iliopúbica",
#                                                                 "escotadura acetabular" : "escotadura acetabular",
#                                                                 "parte no artciular" : Parte(
#                                                                                         nombre="parte no articular",
#                                                                                         rasgos={"fosa acetabular" : "fosa acetabular"},
#                                                                                     ),
#                                                                 "parte artciular" : Parte(
#                                                                     nombre="parte articular", 
#                                                                     rasgos={"semilunar" : "semilunar"}
#                                                                 )
#                                                             }
#                                                         ),
#                                 "fosa ilíaca externa" : Fosa(
#                                                             nombre="fosa ilíaca externa",
#                                                             rasgos={
#                                                                 "linea glútea anterior" : "linea glútea anterior",
#                                                                 "linea glútea posterior" : "linea glútea posterior",
#                                                                 "parte posterior" : "parte posterior",
#                                                                 "parte media" : "parte media",
#                                                                 "parte anterior" : "parte anterior"
#                                                             }
#                                                         ),
#                                 "surco supraacetabular" : "surco supraacetabular",
#                                 "agujeros nutricio" : "agujeros nutricio",
#                                 "agujeros obturador" : "agujeros obturador"
#                             }
#                         ),
#         "cara interna" : Cara(
#                             nombre="cara interna",
#                             rasgos={
#                                 "fosa ilíaca interna" : "fosa ilíaca interna",
#                                 "tuberosidad ilíaca" : "tuberosidad ilíaca",
#                                 "carilla auricular" : "carilla auricular", # para el sacro
#                                 "superficie cuadrilátera" : "superficie cuadrilátera"
#                             }
#                         ),
#         "borde anterior" : Borde(
#                             nombre="borde anterior",
#                             rasgos={
#                                 "espinas ilíaca anterior superior" : "espinas ilíaca anterior superior",
#                                 "espinas iliáca anterior inferior" : "espinas iliáca anterior inferior",
#                                 "espinas púbica" : "espinas púbica",
#                                 "escotaduras innominada" : "escotaduras innominada",
#                                 "escotaduras del psoas ilíaco" : "escotaduras del psoas ilíaco",
#                                 "eminencia iliopectínea" : "eminencia iliopectínea",
#                                 "superficie pectínea" : "superficie pectínea",
#                                 "cresta pectínea" : "cresta pectínea",
#                                 "cresta del pubis" : "cresta del pubis"
#                             }
#                         ),
#         "borde posterior" : Borde(
#                                 nombre="borde posterior",
#                                 rasgos={
#                                     "espina ilíaca posterosuperior" : "espina ilíaca posterosuperior",
#                                     "espina ilíaca posteroinferior" : "espina ilíaca posteroinferior",
#                                     "espina ciática" : "espina ciática",
#                                     "escotadura innominada" : "escotadura innominada",
#                                     "escotadura ciática mayor" : "escotadura ciática mayor",
#                                     "escotadura ciática menor" : "escotadura ciática menor",
#                                     "tuberosidad isquiática" : "tuberosidad isquiática"
#                                 }
#                             ),
#         "borde superior" : Borde(
#                                 nombre="borde superior o Cresta Ilíaca",
#                                 rasgos={
#                                     "labio interno" : "labio interno",
#                                     "labio externo" : "labio externo",
#                                     "línea intermedia" : "línea intermedia"
#                                 }
#                             ),
#         "borde inferior" : Borde(
#                                 nombre="borde inferior",
#                                 rasgos={
#                                     "carilla articular del sínfisis pubiana" : "carilla articular del sínfisis pubiana",
#                                     "rama isquiopubiana" : "rama isquiopubiana"
#                                 }
#                             ),
#         "angulo anterosuperior" : "angulo anterosuperior", # espina iliaca anterosuperior
#         "angulo posteriorsuperior": "angulo posteriorsuperior", # espina iliaca posterosuperior
#         "angulo medial" : "angulo medial", # angulo del pubis
#         "angulo posteroinferior" : "angulo posteroinferior", # tuberosidad isquiática
#         "pubis" : Parte(
#                     nombre="pubis",
#                     rasgos={
#                         "rama ascendente" : "rama ascendente",
#                         "rama descendente" : "rama descendente"
#                     }
#                 ),
#         "isquion" : Parte(
#                         nombre="isquion",
#                         rasgos={
#                             "rama ascendente" : "rama ascendente",
#                             "rama descendente" : "rama descendente"
#                         }
#                     )
#     }
# )

coxal = {
    "nombre": "coxal",
    "cara lateral" : {
        "cavidad articular" : {
            "borde acetabular" : "borde acetabular",
            "escotadura iliosquiática" : "escotadura iliosquiática",
            "escotadura iliopúbica" : "escotadura iliopúbica",
            "escotadura acetabular" : "escotadura acetabular",
            "parte no artciular" : {
                "fosa acetabular" : "fosa acetabular"
                },
            "parte artciular" :{
                "semilunar" : "semilunar"
                }
        },
        "fosa ilíaca externa" : {
            "linea glútea anterior" : "linea glútea anterior",
            "linea glútea posterior" : "linea glútea posterior",
            "parte posterior" : "parte posterior",
            "parte media" : "parte media",
            "parte anterior" : "parte anterior"
            },
        "surco supraacetabular" : "surco supraacetabular",
        "agujeros nutricio" : "agujeros nutricio",
        "agujeros obturador" : "agujeros obturador"
    },
    "cara interna" : {
        "fosa ilíaca interna" : "fosa ilíaca interna",
        "tuberosidad ilíaca" : "tuberosidad ilíaca",
        "carilla auricular" : "carilla auricular", # para el sacro
        "superficie cuadrilátera" : "superficie cuadrilátera"
    },
    "borde anterior" : {
        "espinas ilíaca anterior superior" : "espinas ilíaca anterior superior",
        "espinas iliáca anterior inferior" : "espinas iliáca anterior inferior",
        "espinas púbica" : "espinas púbica",
        "escotaduras innominada" : "escotaduras innominada",
        "escotaduras del psoas ilíaco" : "escotaduras del psoas ilíaco",
        "eminencia iliopectínea" : "eminencia iliopectínea",
        "superficie pectínea" : "superficie pectínea",
        "cresta pectínea" : "cresta pectínea",
        "cresta del pubis" : "cresta del pubis"
    },
    "borde posterior" : {
        "espina ilíaca posterosuperior" : "espina ilíaca posterosuperior",
        "espina ilíaca posteroinferior" : "espina ilíaca posteroinferior",
        "espina ciática" : "espina ciática",
        "escotadura innominada" : "escotadura innominada",
        "escotadura ciática mayor" : "escotadura ciática mayor",
        "escotadura ciática menor" : "escotadura ciática menor",
        "tuberosidad isquiática" : "tuberosidad isquiática"
    },
    "borde superior" : {
        "labio interno" : "labio interno",
        "labio externo" : "labio externo",
        "línea intermedia" : "línea intermedia"
    },
    "borde inferior" : {
        "carilla articular del sínfisis pubiana" : "carilla articular del sínfisis pubiana",
        "rama isquiopubiana" : "rama isquiopubiana"
    },
    "angulo anterosuperior" : "angulo anterosuperior", # espina iliaca anterosuperior
    "angulo posteriorsuperior": "angulo posteriorsuperior", # espina iliaca posterosuperior
    "angulo medial" : "angulo medial", # angulo del pubis
    "angulo posteroinferior" : "angulo posteroinferior", # tuberosidad isquiática
    "pubis" : {
        "rama ascendente" : "rama ascendente",
        "rama descendente" : "rama descendente"
    },
    "isquion" : {
        "rama ascendente" : "rama ascendente",
        "rama descendente" : "rama descendente"
    }
}


print(coxal["cara lateral"])

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
