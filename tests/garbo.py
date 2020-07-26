# coxal = {
#     "nombre": "coxal",
#     "cara lateral" : {
#         "cavidad articular" : {
#             "borde acetabular" : "borde acetabular",
#             "escotadura iliosquiática" : "escotadura iliosquiática",
#             "escotadura iliopúbica" : "escotadura iliopúbica",
#             "escotadura acetabular" : "escotadura acetabular",
#             "parte no artciular" : {
#                 "fosa acetabular" : "fosa acetabular"
#                 },
#             "parte artciular" :{
#                 "semilunar" : "semilunar"
#                 }
#         },
#         "fosa ilíaca externa" : {
#             "linea glútea anterior" : "linea glútea anterior",
#             "linea glútea posterior" : "linea glútea posterior",
#             "parte posterior" : "parte posterior",
#             "parte media" : "parte media",
#             "parte anterior" : "parte anterior"
#             },
#         "surco supraacetabular" : "surco supraacetabular",
#         "agujeros nutricio" : "agujeros nutricio",
#         "agujeros obturador" : "agujeros obturador"
#     },
#     "cara interna" : {
#         "fosa ilíaca interna" : "fosa ilíaca interna",
#         "tuberosidad ilíaca" : "tuberosidad ilíaca",
#         "carilla auricular" : "carilla auricular", # para el sacro
#         "superficie cuadrilátera" : "superficie cuadrilátera"
#     },
#     "borde anterior" : {
#         "espinas ilíaca anterior superior" : "espinas ilíaca anterior superior",
#         "espinas iliáca anterior inferior" : "espinas iliáca anterior inferior",
#         "espinas púbica" : "espinas púbica",
#         "escotaduras innominada" : "escotaduras innominada",
#         "escotaduras del psoas ilíaco" : "escotaduras del psoas ilíaco",
#         "eminencia iliopectínea" : "eminencia iliopectínea",
#         "superficie pectínea" : "superficie pectínea",
#         "cresta pectínea" : "cresta pectínea",
#         "cresta del pubis" : "cresta del pubis"
#     },
#     "borde posterior" : {
#         "espina ilíaca posterosuperior" : "espina ilíaca posterosuperior",
#         "espina ilíaca posteroinferior" : "espina ilíaca posteroinferior",
#         "espina ciática" : "espina ciática",
#         "escotadura innominada" : "escotadura innominada",
#         "escotadura ciática mayor" : "escotadura ciática mayor",
#         "escotadura ciática menor" : "escotadura ciática menor",
#         "tuberosidad isquiática" : "tuberosidad isquiática"
#     },
#     "borde superior" : {
#         "labio interno" : "labio interno",
#         "labio externo" : "labio externo",
#         "línea intermedia" : "línea intermedia"
#     },
#     "borde inferior" : {
#         "carilla articular del sínfisis pubiana" : "carilla articular del sínfisis pubiana",
#         "rama isquiopubiana" : "rama isquiopubiana"
#     },
#     "angulo anterosuperior" : "angulo anterosuperior", # espina iliaca anterosuperior
#     "angulo posteriorsuperior": "angulo posteriorsuperior", # espina iliaca posterosuperior
#     "angulo medial" : "angulo medial", # angulo del pubis
#     "angulo posteroinferior" : "angulo posteroinferior", # tuberosidad isquiática
#     "pubis" : {
#         "rama ascendente" : "rama ascendente",
#         "rama descendente" : "rama descendente"
#     },
#     "isquion" : {
#         "rama ascendente" : "rama ascendente",
#         "rama descendente" : "rama descendente"
#     }
# }


# print(coxal["cara lateral"]["cavidad articular"]["borde acetabular"])










# coxal = (
#     "coxal",
#     ["angulo anterosuperior", # espina iliaca anterosuperior
#     "angulo posteriorsuperior", # espina iliaca posterosuperior
#     "angulo medial", # angulo del pubis
#     "angulo posteroinferior"],
#     {"cara lateral" : (
#         ["borde acetabular",
#         "escotadura iliosquiática",
#         "escotadura iliopúbica",
#         "escotadura acetabular",
#         "parte no artciular o fosa acetabular",
#         "parte artciular o semilunar",
#         "surco supraacetabular",
#         "agujeros nutricio",
#         "agujeros obturador" 
#         ],
#         {"fosa ilíaca externa" : (
#             ["linea glútea anterior",
#              "linea glútea posterior",
#              "parte posterior",
#              "parte media",
#              "parte anterior"],
#              {}
#         )}
#     ),
#     "cara interna" : (
#         ["fosa ilíaca interna",
#         "tuberosidad ilíaca",
#         "carilla auricular",
#         "superficie cuadrilátera"],
#         {}
#     ),
#     "borde anterior" : (
#         ["espina ilíaca anterior superior",
#         "espina iliáca anterior inferior",
#         "espina púbica",
#         "escotadura innominada",
#         "escotaduras del psoas ilíaco",
#         "eminencia iliopectínea",
#         "superficie pectínea",
#         "cresta pectínea",
#         "cresta del pubis"],
#         {}
#     ),
#     "borde posterior" : (
#         ["espina ilíaca posterosuperior",
#         "espina ilíaca posteroinferior",
#         "espina ciática",
#         "escotadura innominada",
#         "escotadura ciática mayor",
#         "escotadura ciática menor",
#         "tuberosidad isquiática"],
#         {}
#     ),
#     "borde superior" : (
#         ["labio interno",
#         "labio externo",
#         "línea intermedia",],
#         {}
#     ),
#     "borde inferior" : (
#         ["rama isquiopubiana",
#         "carilla articular del sínfisis pubiana"],
#         {}
#     ),
#     "pubis" : (
#         ["rama ascendente",
#         "rama descendente",],
#         {}
#     ),
#     "isquion" : (
#         ["rama ascendente",
#          "rama descendente",],
#         {}
#     )
#     }
# )    

# print(coxal[2]["cara lateral"][1]["fosa ilíaca externa"][1] + " 1/3 inferior de")

# musculo_glúteo_mayor = Musculo(
#     nombre="Glúteo Mayor",
#     origen=[
#     ],
#     insercion=[
#         ("", coxal[2]["cara lateral"][1]["fosa ilíaca externa"][1] + "")
#     ],
#     irrigacion=[

#     ],
#     inervacion=[

#     ]
# )

#     "borde anterior" : {
#         "espinas ilíaca anterior superior" : "espinas ilíaca anterior superior",
#         "espinas iliáca anterior inferior" : "espinas iliáca anterior inferior",
#         "espinas púbica" : "espinas púbica",
#         "escotaduras innominada" : "escotaduras innominada",
#         "escotaduras del psoas ilíaco" : "escotaduras del psoas ilíaco",
#         "eminencia iliopectínea" : "eminencia iliopectínea",
#         "superficie pectínea" : "superficie pectínea",
#         "cresta pectínea" : "cresta pectínea",
#         "cresta del pubis" : "cresta del pubis"
#     },
#     "borde posterior" : {
#         "espina ilíaca posterosuperior" : "espina ilíaca posterosuperior",
#         "espina ilíaca posteroinferior" : "espina ilíaca posteroinferior",
#         "espina ciática" : "espina ciática",
#         "escotadura innominada" : "escotadura innominada",
#         "escotadura ciática mayor" : "escotadura ciática mayor",
#         "escotadura ciática menor" : "escotadura ciática menor",
#         "tuberosidad isquiática" : "tuberosidad isquiática"
#     },
#     "borde superior" : {
#         "labio interno" : "labio interno",
#         "labio externo" : "labio externo",
#         "línea intermedia" : "línea intermedia",
#     },
#     "borde inferior" : {
#         "carilla articular del sínfisis pubiana" : "carilla articular del sínfisis pubiana",
#         "rama isquiopubiana" : "rama isquiopubiana"
#     },
#     "angulo anterosuperior" : "angulo anterosuperior", # espina iliaca anterosuperior
#     "angulo posteriorsuperior": "angulo posteriorsuperior", # espina iliaca posterosuperior
#     "angulo medial" : "angulo medial", # angulo del pubis
#     "angulo posteroinferior" : "angulo posteroinferior", # tuberosidad isquiática
#     "pubis" : {
#         "rama ascendente" : "rama ascendente",
#         "rama descendente" : "rama descendente",
#     },
#     "isquion" : {
#         "rama ascendente" : "rama ascendente",
#         "rama descendente" : "rama descendente"
#     }
# )