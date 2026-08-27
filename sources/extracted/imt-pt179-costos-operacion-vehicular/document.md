<!-- source-id: imt-pt179-costos-operacion-vehicular -->
<!-- extractor: pymupdf -->
<!-- raw sha256: 27e7a5e65adc855e73313e095b1a5f2d91b5d280cb8c4594547731b3730a04d2 -->



<!-- page 1 -->

ISSN  0188-7297 
    
 
 
 
 
ANALISIS DE COSTOS DE OPERACION 
VEHICULAR DEL AUTOTRANSPORTE 
DE CARGA POR LA RED CARRETERA 
FEDERAL 
 
Publicación Técnica No.179 
Sanfandila, Qro. 2001 
Daniel Pérez Bello 
Alberto Mendoza Díaz 
Antonio García Chávez 
Noelia Villegas Villegas 


<!-- page 2 -->

 
 
 
 
INSTITUTO MEXICANO DEL TRANSPORTE 
SECRETARIA DE COMUNICACIONES Y TRANSPORTES 
 
 
 
 
 
 
 
 
 
 
 
 
Publicación Técnica No.179 
Sanfandila, Qro. 2001 
 
 
Análisis de Costos de 
Operación Vehicular del 
Autotransporte de Carga por 
la Red Carretera Federal 


<!-- page 3 -->

III
Este documento fue elaborado en la Coordinación de Seguridad y Operación del
Transporte, por Daniel Pérez Bello1, Alberto Mendoza Díaz, Antonio García
Chávez y Noelia Villegas Villegas . Se contó con la colaboración de Emilio Mayoral
Grajeda en la edición de este documento.
                                           
1  Pasante de la Maestría en Vías Terrestres de la Universidad Autónoma de Chihuahua.


<!-- page 4 -->



<!-- page 5 -->

V
Indice
Resumen
VII
Abstract
IX
Resumen Ejecutivo
XI
1   Introducción
1
1.1
Descripción del Problema
1
1.2
Información Preliminar
2
1.3
Justificación
4
1.4
Fundamentación Teórica
4
1.5
Objetivos
5
1.6
Hipótesis
6
1.7
Metodología
6
1.8
Utilidad del Proyecto
7
2   Antecedentes
9
2.1
Sistemas de Información Geográfica y de Posicionamiento
Global
9
2.2
Sistemas de Información Geoestadística para el Transporte
11
2.3
El Sistema “ArcView”
13
2.4
Bases de Datos
13
2.4.1 Aforos con Clasificación Vehicular
13
2.4.2 Capacidad y Niveles de Servicio
14
2.4.3 Tipo de Terreno
14
2.4.4 Estado del Pavimento
15
2.4.5 Curvatura
15
2.4.6 Cuotas
15


<!-- page 6 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera
Federal
VI
2.5
Metodología para el Cálculo de Costos de Operación Vehicular
(COV’s)
19
3   Desarrollo del Sistema
21
3.1
Enfoque
21
3.2
Información Cartográfica
21
3.3
Integración de Bases de Datos
27
3.3.1 Aforos con Clasificación Vehicular
27
3.3.2 Capacidad y Niveles de Servicio
28
3.3.3 Tipo de Terreno
28
3.3.4 Estado del Pavimento
28
3.3.5 Curvatura
28
3.3.6 Cuotas
29
3.3.7 Límite de Velocidad
29
3.4
Incorporación de Costos de Operación Vehicular
29
4   Generación de Algunos Resultados
40
4.1
Obtenidos Directamente de los Datos Integrados al Sistema
40
4.1.1 Aforos con Clasificación Vehicular
40
4.1.2 Vehículos-Kilómetro
42
4.1.3 Capacidad y Niveles de Servicio
44
4.2
Otros  Resultados a Partir de Procesos más Elaborados
49
4.2.1 COV Totales del Flujo de Vehículos de Carga y por Toneladas-
Kilómetro
49
4.2.2 Identificación de Corredores Prioritarios para Modernización
52
5   Conclusiones
61
5.1
Conclusiones
61
5.2
Recomendaciones
62
Referencias
63


<!-- page 7 -->

VII
Resumen
El presente trabajo tiene por objetivo integrar datos en formatos electrónicos
y no electrónicos, actualmente dispersos, en un ambiente que permita, de
manera ágil, la visualización y combinación de los datos para el cálculo y
análisis de los Costos de Operación Vehicular del autotransporte de carga
de la Red Carretera Federal y con éstos, la selección de rutas óptimas en el
traslado de las mercancías. 
Actualmente, gran parte de la información está desagregada por estado.
Con este trabajo, se podrá manejar toda la Red en un solo archivo o
proyecto. La información con que se alimenta a dicho proyecto puede
clasificarse en: (I) información cartográfica, (II) información de las
condiciones físicas de las carreteras y los volúmenes de tránsito que
circulan en ellas, y (III) Costos de Operación Vehicular.
El contar con tan diversas fuentes de información, hace necesario
establecer un sistema que permita el acceso de ésta en forma desagregada,
así como la utilización de herramientas computacionales adecuadas que
hagan posible configurar la red de forma integral, permitiendo al mismo
tiempo un grado de segmentación que facilite la alimentación de información
detallada al sistema.
En el desarrollo de este sistema, se integraron referencias cartográficas,
bases de datos existentes conteniendo aforos con clasificación vehicular,
capacidad y niveles de servicio, tipo de terreno, estado del pavimento,
curvatura y cuotas. Esta integración fue posible gracias al uso de la
herramienta computacional ArcView y su módulo de análisis de redes,
cuyos atributos y ventajas son descritos en el desarrollo del trabajo.
Una vez integrada la información anteriormente descrita, se procedió al
cálculo y análisis de los Costos de Operación Vehicular, con los que
también se alimentó al sistema para así estudiar las rutas más económicas
y seguras para el transporte de productos. 
Finalmente, en la generación de algunos resultados obtenidos a partir de los
datos integrados y con procesos más elaborados, se establecieron los
principios más convenientes para la identificación de los corredores de
transporte prioritarios para el autotransporte federal de carga a ser
modernizados en el futuro cercano.


<!-- page 8 -->



<!-- page 9 -->

IX
Abstract
This work is aimed at integrating electronic and non-electronic data,
currently dispersed in many different places, into a Geographic Information
System (GIS) thus making possible the efficient management of such
information as well as the computation of vehicle operation costs (VOC) of
freight road motor transport through the Mexican Federal Road Network and
the selection of the optimal routes for the road transport of commodities.
In the past, most of the former information has been handled separately by
state. This work will make it possible to integrally manage the information for
all the states in just one project. The project is fed with the following types of
data: (I) cartographic information, (II) physical and operational characteristics
of the roads, and (III) vehicle operating costs. The project or system is
developed in the GIS named ArcView.
Finally, with basis on the developed system and the ArcView Network
Analyst, a series of criteria for identification of the primary road corridors for
the transport of merchandise within the country are studied. From this study,
recommendations are generated for identifying the most convenient
corridors to be modernized in the near future.


<!-- page 10 -->



<!-- page 11 -->

XI
Resumen Ejecutivo
Hoy día, la apertura comercial internacional de México y otros factores
hacen importante mejorar la gestión de los sistemas de transporte del país,
particularmente el de la Red Carretera, por ser éste el modo que más
contribuye al movimiento nacional de pasajeros y carga. La complejidad de
las redes actuales de transporte hace necesario que la información sobre
sus aspectos operativos, tenga que ser manejada a través de sistemas de
cómputo. En el caso de la Red Carretera Federal, los datos de magnitud de
los flujos de tránsito, las características y situación que guarda cada tramo,
los Costos de Operación Vehicular (COV’s) y otros datos, son
fundamentales para la planeación del desarrollo de la Red y los servicios de
transporte que por ella se efectúan. Los sistemas de manejo y
procesamiento de bases de datos así como los Sistemas de Información
Geográfica (SIG), ambos de desarrollo reciente acelerado, representan
herramientas para el logro de los fines anteriores.
El objetivo de este trabajo es integrar datos en formatos electrónicos y no
electrónicos, actualmente dispersos, en un ambiente que permita de manera
ágil, la visualización y combinación de los datos para el cálculo y análisis de
los Costos de Operación Vehicular del autotransporte de carga de la Red
Carretera Federal y con éstos, la selección de rutas óptimas en el traslado
de las mercancías. 
Actualmente, gran parte de la información está desagregada por estado.
Con este trabajo, se podrá manejar toda la Red en un solo archivo o
proyecto. La información con que se alimentará a dicho proyecto puede
clasificarse en:
• Información cartográfica.
• Información de las condiciones físicas de las carreteras y los volúmenes
de tránsito que circulan en ellas.
• Costos de Operación Vehicular.
El contar con tan diversas fuentes de información, hace necesario
establecer un sistema que permita el acceso de ésta, en forma
desagregada. Así, el primer paso es la utilización de herramientas
computacionales adecuadas, que hacen posible configurar la red de forma


<!-- page 12 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera
Federal
XII
integral permitiendo al mismo tiempo un grado de segmentación que facilite
la alimentación de información detallada al sistema.
En el desarrollo de este sistema, se integraron referencias cartográficas,
bases de datos existentes conteniendo aforos con clasificación vehicular,
capacidad y niveles de servicio, tipo de terreno, estado del pavimento,
curvatura y cuotas. Esta integración fue posible gracias al uso de la
herramienta computacional ArcView y su módulo de análisis de redes,
cuyos atributos y ventajas son descritos en el desarrollo del trabajo.
Una vez integrada la información anteriormente descrita, se procedió al
cálculo y análisis de los Costos de Operación Vehicular, con los que
también se alimentó al sistema, para así estudiar las rutas más económicas
y seguras para el transporte de productos. 
Finalmente, se generaron algunos resultados obtenidos a partir de los datos
integrados y con procesos más elaborados. En el primer caso, estos
resultados son presentados en vistas o representaciones geográficas en
ArcView, obtenidos directamente con los datos integrados al sistema
(Transito Promedio Diario Anual, Vehiculos-Kilómetro, Capacidad y Niveles
de Servicio, Tipo de Terreno, Estado Superficial del Pavimento y Curvatura).
En el caso de los procesos más elaborados, se utilizaron los COV´s totales
del flujo de vehículos de carga y por tonelada-kilómetro transportadas y se
analizaron varios criterios de identificación de los corredores de transporte
prioritarios para el autotransporte federal de carga a ser modernizados en el
futuro cercano.


<!-- page 13 -->

1
1  Introducción
1.1
Descripción del Problema
A través de los años, se han venido generando diferentes tipos de
información utilizados en la gestión de la Red Carretera Federal, tales como:
(I) los aforos con clasificación vehicular recabados desde hace más de 30
años en numerosos sitios de la Red, (II) diversos indicadores para calificar
el estado de los diferentes elementos de la sección transversal de los arcos
(p. ej. nivel de servicio del pavimento, estado del señalamiento, etc.), el nivel
de saturación de los arcos, etc. También, como resultado de levantamientos
topográficos, se han obtenido planos con los alineamientos de los caminos.
El proceso anterior ha traído como consecuencia que actualmente se tenga
una diversidad de archivos, generalmente dispersos (en diferentes sitios u
organizaciones) y en papel (es decir, no en archivos electrónicos), lo cual
hace prácticamente imposible su utilización integral y automatizada. 
Con el fin de contribuir a resolver este problema, se realiza este trabajo, el
cual vacía varios de los archivos anteriores (sobre alineamientos, aforos,
etc.) en un Sistema de Información Geográfica (SIG). Como resultado de
esta acción, se genera un sistema que hace más expedita la explotación de
los distintos tipos de información para diversos fines. Se vacían en el
sistema siguientes datos para cada tramo de la Red considerada: aforo,
composición vehicular, capacidad, pendiente, curvatura, calidad de
rodamiento del pavimento y costos de operación vehicular (COV’s)
(Referencia 1). Estos últimos corresponden al autotransporte de carga,
particularmente a la configuración T3-S2 (a plena carga) la cual juega un
papel primordial en el autotransporte doméstico e internacional de
mercancías de México (Referencia 1). Los COV’s integrados en el sistema,
son calculados utilizando el programa VOC del Banco Mundial (Referencia
2). La información que se maneja en este trabajo corresponde básicamente
al año 2000.
La Red a considerar en este trabajo es la Red Federal libre (pavimentada)
más las autopistas de cuota, ya sean las de jurisdicción de Caminos y
Puentes Federales (CAPUFE), o del Banco Nacional de Obras y Servicios
(BANOBRAS), u otras concesionadas. Esta Red total tiene una longitud
aproximada de 48,470 kilómetros (42,478 km de Red Federal libre, 1,507


<!-- page 14 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
2
km de autopistas de CAPUFE, 2,813.4 km de autopistas de BANOBRAS y
1,671.6 km de otras autopistas concesionadas). 
1.2
Información Preliminar
La información preliminar más relevantes para el desarrollo de este trabajo
es la referente a: (I) el SIG en el que se realizan la mayoría de los
desarrollos de este trabajo, y (II) los archivos o inventarios a partir de los
cuales se toma la información de la Red Carretera Federal. A continuación
se describen algunos aspectos importantes en relación con estos dos tipos
de información: 
• 
Con la reciente tecnología, se cuenta actualmente con herramientas
que facilitan las tareas de manejo, análisis y administración de datos,
tales como los sistemas geográficos de información (GIS). Estos
permiten: 
a) 
Relacionar datos espaciales (vinculados con una ubicación de
acuerdo a un sistema de coordenadas) con no-espaciales.
b) 
Organizar y combinar la información proveniente de distintas
fuentes a través de capas.
c) 
Representar y analizar geográficamente los datos.
d) 
Automatizar el manejo de la información.
Para el desarrollo de este trabajo se seleccionó el SIG denominado ArcView
(Referencia 3), atendiendo a consideraciones de capacidad contra precio.
Así mismo se utiliza la extensión de ArcView para el análisis de problemas
de redes (Referencia 4). Como herramientas auxiliares de ArcView y su
módulo de redes, en este trabajo también se utilizan manejadores de bases
de datos y hojas de cálculo. 
• 
Dentro de los archivos o inventarios de información que se utilizan, se
considera que el más importante es el Sistema de Información
GeoEstadística para el Transporte (SIGET) (Referencia 5). Este es un
inventario georeferenciado de la infraestructura de transporte del país
(carreteras, puertos, etc.) en el que se detallan, entre otros aspectos,
las características de la Red Carretera Federal (alineamiento vertical y
horizontal, gasolineras y estaciones de servicio, etc.). Este inventario


<!-- page 15 -->

1  Introducción
3
ha venido siendo levantado por los Centros de la Secretaría de
Comunicaciones y Transportes (Centros SCT) en los Estados utilizando
Sistemas de Posicionamiento Global (GPS), bajo la dirección del IMT.
Este, además, ha realizado el análisis y desarrollo de la información
levantada. Aunque el SIGET se ha manejado tradicionalmente en el
GIS denominado ArcInfo, como ya se indicó, para esta aplicación se
seleccionó ArcView. Como ya también se mencionó, se utilizan
diferentes tipos de información sobre características físicas y operativas
de la Red (aforos con clasificación vehicular, nivel de servicio de los
pavimentos, etc.), los cuales se obtienen a partir de los organismos del
Gobierno Federal que los generan.
• 
Los COV’s integrados en sistema provienen del paquete de cómputo
denominado Costos de Operación Vehicular (VOC por sus siglas en
inglés) (Referencia 2). Este paquete fue elaborado por el Banco
Mundial, con el fin de proporcionar a los planeadores una herramienta
para la generación de información de dichos costos que pudiese
contribuir a una mejor evaluación técnico-económica de sus opciones
de inversión. Con base en estudios realizados en diversos países,
varios de ellos con sistema de transporte carretero con condiciones
similares al de México (por ejemplo Brasil), se construyeron una serie
de modelos matemáticos para diferentes tipos de vehículos (desde
automóviles hasta camiones de pasajeros y carga) con los que el
Banco Mundial estructuró posteriormente este programa de cómputo.
Algunos de los modelos generados, son: (I) de consumo de
combustibles, (II) de consumo de lubricantes, (III) de consumo de
llantas, (IV) de salario de tripulantes, (V) de mantenimiento vehicular
(incluyendo mano de obra y refacciones), (VI) de depreciación del
vehículo, (VII) de costos financieros, (VIII) de costo de oportunidad del
tiempo invertido en viajar por los pasajeros y la carga transportados,
etc. Varios de los modelos anteriores generan consumos, ingresados
por el usuario del programa. Para un vehículo deseado determinado
(especificado por el usuario), el programa genera, entre otras salidas,
los estimados de los consumos mencionados, así como el costo total
por kilómetro de operación y la distribución porcentual de los diferentes
conceptos que lo componen.


<!-- page 16 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
4
1.3
Justificación 
El desarrollo de este trabajo se justifica por las siguientes razones:
• 
Con la finalidad de generar un sistema de administración de distintos
tipos de información de la Red Carretera Federal en el ambiente de un
SIG (incluyendo costos operativos del autotransporte de carga), que
permita su ágil consulta y explotación. 
• 
Como una etapa que forma parte del desarrollo de proyectos de
investigación de mayores alcances, tales como la elaboración de
modelos de asignación del tráfico de carga por la por la Red Carretera
Federal.
1.4
Fundamentación Teórica
Los fundamentos teóricos para este trabajo, son:
• 
En el momento presente, la apertura comercial internacional de México
y otros factores hacen importante mejorar la gestión de los sistemas de
transporte del país, particularmente el de la Red Carretera, por ser éste
el modo que más contribuye al movimiento nacional de pasajeros y
carga. La complejidad de las redes actuales de transporte hace
necesario que la información sobre sus aspectos operativos, tenga que
ser manejada a través de sistemas de cómputo. En el caso de la Red
Carretera Federal, los datos de magnitud de los flujos de tránsito, las
características y situación que guarda cada tramo, COV’s y otros datos,
son fundamentales para la planeación del desarrollo de la Red y los
servicios de transporte que por ella se efectúan. Los sistemas de
manejo y procesamiento de bases de datos así como los SIG, ambos
de desarrollo reciente acelerado, representan herramientas para el
logro de los fines anteriores.
• 
La tecnología computacional ofrece actualmente una herramienta
diseñada específicamente para facilitar y apoyar las tareas de manejo,
análisis espacial y administración de información, conocida como
Sistemas de Información Geográfica (SIG). Las capacidades de los


<!-- page 17 -->

1  Introducción
5
SIG, ya mencionadas, hacen idónea su aplicación para la realización
de este trabajo.
• 
En el SIGET, la información de la Red Carretera Federal levantada con
GPS está organizada por Estados de la República, dado que se ha
adoptado la política de proporcionar a cada Estado su información para
sus propios fines (es decir, que su uso se realice de manera
descentralizada). Así mismo, es más ágil manejar la información total
en 32 archivos en vez de toda ella en uno solo. En este trabajo, se
aborda el problema de integrar y manejar la información de toda la Red
en un solo archivo (o proyecto), basándose en la segmentación de la
Red a nivel de los tramos considerados por el sistema de clasificación
de Carreteras Federales de la SCT (Referencia 6). Lo anterior se
efectúa utilizando SIG's, que son instrumentos técnicos con diversas
capacidades, diseñados para inventariar, administrar y manejar
información espacial y no espacial. 
• 
La información de COV’s del autotransporte de carga, evaluada
utilizando las características  físicas de la infraestructura en el SIGET y
manejada en el ambiente de un SIG, permite generar una gran
diversidad de análisis de alta precisión tales como la determinación del
COV total para determinadas rutas, la evaluación de la Red bajo
diferentes criterios, etc. 
1.5
Objetivos
El objetivo general de este trabajo es elaborar un SIG que permita evaluar
los COV’s del autotransporte de carga por los tramos de la Red Carretera
Federal a partir de sus características físicas y operativas, con el fin de
facilitar el desarrollo de medidas pertinentes de explotación, administración
o gestión de la Red. 
Así mismo, se contemplan los siguientes objetivos particulares:
• 
Dominar el uso de un SIG. 
• 
Diseñar un sistema de manejo de información de la Red Carretera
Federal, incluyendo COV’s del autotransporte de carga, tomando como


<!-- page 18 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
6
base el inventario de infraestructura con que ya se cuenta dentro del
SIGET. 
• 
Llevar a cabo el desarrollo del sistema anterior. 
• 
Realizar 
algunas 
aplicaciones 
del 
sistema 
antes 
mencionado
(generación de representaciones, determinación de rutas óptimas,
evaluación y rediseño de la Red, etc.). 
1.6
Hipótesis
Se propone la hipótesis de que es posible a través de ArcView, consultar y
analizar las condiciones que guardan los diferentes tramos de la Red
Carretera Federal, en términos de los datos operativos que se consideran
(aforo, composición vehicular, costos operativos, etc.). También se asume
que este enfoque facilita el desarrollo de medidas de gestión de la Red.
1.7
Metodología
La metodología y los alcances están contenidos en las siguientes partes
que constituyen este trabajo:
• 
Inicialmente se desarrolla una introducción que describe información
preliminar, objetivos y alcances del trabajo.
• 
En el Capítulo 2 se describen con detalle algunos antecedentes
relevantes, tales como: (I) el Sistema de Información GeoEstadística
para el Transporte (SIGET), que es la plataforma de referencia sobre la
que se realiza este trabajo y que contiene, en coberturas de ArcInfo, la
georeferenciación de la Red Carretera Nacional y cuya base
cartográfica, en lo referente a los limites estatales y cabeceras
municipales, proviene del INEGI; (II) el programa computacional
ArcView, que se utiliza para el desarrollo del sistema planteado y que
también se tiene disponible en el IMT; (III) los datos que se manejan de
la Red, incluyendo, para cada tramo: alineamientos, capacidad y
niveles de servicio, longitud, aforos con clasificación vehicular, estado
de la superficie de rodamiento, cuota (sólo en autopistas de cuota) y
tipo de terreno (plano, lomerío o montañoso); y (IV) el programa VOC
que se utiliza para el cálculo de COV’s del autotransporte de carga. 


<!-- page 19 -->

1  Introducción
7
• 
El Capítulo 3 describe detalladamente el desarrollo del sistema. Este
paso consiste en:
a) 
Preparar la Red para que pueda ser utilizada por ArcView y su
extensión para el análisis de redes.
b) 
Vaciar en la Red segmentada y preparada, los distintos datos
básicos a considerar.
c) 
Integrar en el sistema, para cada sentido de cada tramo, el COV
del autotransporte de carga.
• 
En el Capítulo 4 se generan algunas aplicaciones y resultados
obtenidos a partir del sistema desarrollado.
• 
Finalmente 
se 
presentan 
una 
serie 
de 
conclusiones 
y
recomendaciones.
Los alcances de este trabajo están limitados por las posibilidades que
brinda el SIG denominado ArcView y su módulo para el análisis de redes,
los rasgos geográficos de la Red contenidos dentro del SIGET, los otros
sistemas computacionales que se utilizan (p. ej. Visual Fox Pro, etc.), los
datos para toda la Red bajo estudio (clasificación y nomenclatura de las
carreteras, aforo, composición vehicular, nivel de servicio y los COV’s del
autotransporte de carga para cada tramo). Se reitera que este trabajo se
refiere a la Red Carretera Federal pavimentada, es decir, excluye
fundamentalmente carreteras no pavimentadas y estatales. 
1.8
Utilidad del Proyecto
Este trabajo resulta ser una herramienta útil con provecho estimado en
función de criterios como ahorro de tiempo, facilidad de manejo y efectividad
de los procesos, en relación con el análisis de información de la Red.
• 
Cuenta con información confiable, permitiendo obtener una perspectiva
de las características que guarda cada tramo de la Red Carretera
Federal. 
• 
Apoya las labores de planeación, investigación y toma de decisiones
por parte del Sector Transporte. 


<!-- page 20 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
8
• 
Genera información de utilidad para los administradores y operadores
de la infraestructura.
• 
Permite al autotransporte de carga, el conocimiento de sus costos
operativos como apoyo para la programación de sus actividades.


<!-- page 21 -->

9
2  Antecedentes
Como se indicó en la introducción, los antecedentes que se presentan a
continuación se refieren a los sistemas de información geográfica (SIG) y de
posicionamiento global (GPS), el Sistema GeoEstadístico para el Transporte
(SIGET), el programa computacional denominado ArcView, las bases de
datos que son insumo para el desarrollo del sistema que es objeto de este
trabajo y la metodología que se utiliza para el cálculo de costos de
operación vehicular.
2.1
Sistemas de Información Geográfica y de Posicionamiento
Global
Hoy en día, en diversos países, se tiene la necesidad de desarrollar un
sistema de base de datos georeferenciados y Sistemas Geográficos de
Información (SIG), para lograr lo anterior, los gobiernos de estos países y
las diversas organizaciones invierten grandes cantidades de dinero. Hace
unos cuantos años, los SIG eran herramientas muy especializadas sólo al
alcance de pocas organizaciones, hoy en día, estas herramientas son
utilizadas por un mayor número de usuarios. Lo anterior puede tener varias
explicaciones, de las cuales podemos mencionar:
• 
Los costos de los equipos informáticos son muy accesibles.
• 
La geografía y los datos que sirven para cuantificarla forman parte ya
de nuestro mundo cotidiano; la mayoría de las decisiones que
tomamos diariamente están relacionadas con o influenciadas por un
hecho geográfico. 
Los SIG han demostrado su utilidad práctica en diversas labores en torno al
transporte, ya sea mediante estudios experimentales o bien, a través de su
plena inserción como herramienta de apoyo en actividades particulares en
distintos departamentos y organismos de transporte,  principalmente de
Estados Unidos y Canadá.
Las diversas posibilidades que ofrecen los SIG en los sistemas de redes del
transporte están aún por revelarse, son resultado de las innovaciones
tecnológicas que amplían sus expectativas, así como la complejidad de la
actividad en la cual se definen condiciones e información múltiple y variada.


<!-- page 22 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
10
Como resultado de la necesidad de manejar información espacial para el
estudio y planeación del transporte, que exige alta confiabilidad y exactitud
en el manejo de los atributos, en los últimos años se han generado
sistemas automáticos más eficientes para la generación, análisis y
manipulación de la información geográficamente referenciada. Entre las
tecnologías que presentan un mayor desarrollo se encuentran las antes
señaladas, los Sistemas Geográficos de Información (SIG) y los Sistemas
de Posicionamiento Global (GPS) vía satélite.
El Sistema de Posicionamiento Global es una tecnología de navegación y
posicionamiento basado en satélites. El Desarrollo del Navigation Satellite
Timing and Ranging (NAVSTAR) Global Positioning System (GPS), nombre
completo del sistema, es un programa financiado por el gobierno de los
Estados Unidos, y administrado por el Departamento de la Defensa de ese
país. El GPS se ha constituido en la herramienta más completa para el
registro de la localización de rasgos o elementos sobre la superficie del
planeta. A partir de 1993, se completó la puesta en órbita de una
constelación de 24 satélites (21 operativos y 3 de reserva) con la misión de
transmitir 
señales 
con 
información 
de 
diversos 
parámetros 
de
posicionamiento, que registradas por receptores en tierra permiten calcular,
con un alto grado de exactitud, la localización geográfica de cualquier
objeto sobre la superficie terrestre (Referencia 7).
La tecnología del GPS, además de ser utilizada para determinar la
localización exacta de un lugar sobre la superficie terrestre, proporciona
también información sobre tiempo y velocidad que le permite actuar como
un sistema para calcular posiciones tridimensionales (latitud, longitud y
altitud) de la ubicación de los usuarios.
Los Sistemas Geográficos de Información (SIG) son sistemas diseñados
para la captura, almacenamiento  y manipulación de la información en
donde la ubicación espacial constituye el elemento fundamental. El análisis
conjunto derivado de la combinación de información gráfica en forma de
mapas (información espacial) y atributos asociados (información no
espacial), da a los SIG su particular potencial de aplicación al sistema de
transporte.
En 
otras 
palabras, 
los 
SIG 
son 
fundamentalmente 
instrumentos
computacionales de capacidades múltiples, diseñados y habilitados en
primera instancia para inventariar información geográfica y de los atributos


<!-- page 23 -->

2  Antecedentes
11
que la caracterizan, la cual a su vez alimenta las funciones de análisis con
que están equipados, para convertirse en herramientas útiles a las labores
de planeación y administración. La clave exacta para emplear un SIG y
obtener de él efectividad y resultados satisfactorios, estriba en la
identificación acertada de su aplicación la cual deberá tener como
característica primordial la necesidad del análisis geográfico (Tabla 2.1)
(Referencia 8).
Lo que distingue a un SIG de una base de datos tradicional, es que los
atributos de éstos están asociados a un objeto topológico (punto, línea,
polígono) y registran una ubicación geográfica precisa. La utilización de
relaciones espaciales, propuesta explícitamente por los SIG, agrega un
nivel de “inteligencia” a bases de datos. 
El uso de GPS para el registro de información georeferenciada, así como el
de SIG para el manejo de esa información, proporcionan herramientas que
conjuntamente son muy poderosas para las diversas actividades que tienen
que ver con la planeación y operación del transporte.
2.2
Sistemas de Información Geoestadística para el Transporte
Una aplicación conjunta de las dos herramientas antes mencionadas (GPS
y SIG), es la que realiza el Instituto Mexicano del Transporte (IMT), el cual
desde 1991 inició una línea de investigación  tendiente a evaluar dichas
tecnologías, 
desarrollando 
el 
proyecto 
Sistema 
de 
Información
GeoEstadística para el Transporte (SIGET). Este proyecto se centró en la
creación, en formato digital, de bases de datos georeferenciados en
coberturas del Sistema Geográfico de Información (SIG) ArcInfo
(Referencia 9). El levantamiento fue realizado con GPS, e incluyó el trazo
de las redes carreteras pavimentadas, la ubicación de puertos y
aeropuertos, así como también la localización precisa de rasgos asociados
al camino (p. ej. bancos de materiales, señales, etc.). La importancia del
banco de información reside tanto en la precisión en la ubicación de los
elementos registrados, como en la gran versatilidad de manejo del formato
digital a través del SIG. 


<!-- page 24 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
12
Tabla 2.1  Ventajas que Brinda la Utilización de un SIG a la Planeación,
Administración e Investigación en el Sistema de Transporte.
INTEGRACION DE DATOS
Facilidad otorgada por el empleo de un
sistema común de referencia, tanto para
la información directamente relacionada
con las vías de comunicación, como de
aquellas otras que hacen posible análisis
más amplios (datos demográficos, etc.).
REPRESENTACION ESPACIAL
DE LOS DATOS
Muestra en forma gráfica (representación
cartográfica) 
la 
distribución 
y/o
comportamiento de los datos en el
territorio, lo cual permite una mayor
compresión del problema en cuestión.
ANALISIS INNOVADOR
Ofrece nuevas formas de observar viejos
problemas 
al 
combinar 
modelos 
y
proporcionar respuestas a preguntas
complejas y multidimensionales en forma
rápida.


<!-- page 25 -->

2  Antecedentes
13
2.3
El Sistema “ArcView”
Como ya se mencionó, en este trabajo se busca generar un sistema que
haga más expedita la explotación de los distintos tipos de información
(alineamientos, aforos, nivel de servicio del pavimento, estado del
señalamiento, etc.). Dado que ArcInfo, el SIG en el que se maneja el
SIGET, es un sistema muy poderoso pero también muy caro, para el
desarrollo de este trabajo se eligió el SIG denominado ArcView (Referencia
3). Este último tiene la ventaja de ser más fácil de utilizar y mucho más
barato, que es un factor muy importante a considerar ya que el sistema
generado será distribuido a los 32 Centros de la Secretaría de
Comunicaciones y Transportes (SCT) en los Estados de la República, y
además el Instituto Mexicano del Transporte cuenta con esta herramienta.
Adicionalmente el ArcView es un SIG compatible con ArcInfo, al ser ambos
elaborados por la misma empresa. 
ArcView permite sobreponer datos contenidos en distintas capas de
información, 
haciendo 
análisis 
combinados 
de 
los 
mismos,
representándolos a la escala deseada y permitiendo obtener resultados que
ayuden a tomar decisiones y resolver problemas de las redes del
transporte. El esfuerzo anterior se llevará a cabo apoyándose también en
otros tipos de programas de cómputo, como por ejemplo: Visual FoxPro
(Referencia 10), el cual proporciona todas las herramientas necesarias para
administrar datos, tanto si se va a organizar tablas de información y ejecutar
consultas, como si se va a crear un sistema de bases de datos integral o
programar una aplicación para la administración de usuarios finales. Otro
de los programas en que se apoya este trabajo es la Hoja de Cálculo Excel
(Referencia 11). 
2.4
Bases de Datos
2.4.1 Aforos con Clasificación Vehicular
Con el fin de conocer la magnitud de los flujos de tránsito y su composición
en términos de los diferentes tipos de vehículos que los integran así como
su variación histórica, la Dirección General de Servicios Técnicos (DGST)
de la SCT realiza anualmente conteos de tránsito en una serie de
estaciones distribuidas en toda la Red Carretera Federal pavimentada.
Como resultado de los conteos efectuados en un año determinado, la DGST
publica, al año siguiente, los aforos con clasificación vehicular en toda la


<!-- page 26 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
14
Red recabados en ese año. Esta información se publica a nivel de tramos,
según la clasificación de las Carreteras Federales de la misma DGST. Esta
es la información que será integrada al sistema desarrollado en esta tesis.
Como ya se dijo anteriormente, la información utilizada corresponde al año
2000 (Referencia 12). 
2.4.2 Capacidad y Niveles de Servicio
Para la Red bajo estudio, esta información es también generada por la
DGST de la SCT, y la publica con determinada periodicidad.  Esta
información se publica, a nivel de tramos, en el mismo formato que la
información de aforos con clasificación vehicular. Para cada tramo se
reporta su flujo vehicular horario existente, los flujos evaluados para los
niveles de servicio A a E y el nivel de servicio actual. El flujo estimado para
el nivel de servicio E es la capacidad en el tramo. En este trabajo, para los
diferentes niveles de servicio, se adoptan las definiciones del Manual de
Capacidad de Carreteras de los EUA (Referencia 13). La información de
capacidad y niveles de servicio que se integrará en el sistema es la que
corresponde a 1998 (Referencia 14), por ser la más recientemente
publicada por la DGST.
2.4.3 Tipo de Terreno
Este parámetro tiene una influencia determinante en los costos de
operación vehicular, por su relación con las pendientes de las carreteras.
Por esta razón, hubo de ser integrado al sistema el tipo de terreno sobre el
que se encuentra cada tramo de la Red considerada, ya sea plano, lomerío
o montañoso. En este trabajo se considera que terreno plano es aquél cuyo
promedio de inclinación, en una longitud mínima de 30 kilómetros, es menor
de 2%; es lomerío si dicho promedio se encuentra entre 2% y 4%; y
montañoso si es mayor que 4%. Para todos los tramos, la información del
tipo de terreno fue obtenida de la misma fuente de la DGST que los datos
de capacidad y niveles de servicio (Referencia 14). 


<!-- page 27 -->

2  Antecedentes
15
2.4.4 Estado del Pavimento
Esta información, para cada carretera, fue obtenida para el año de 2000 en
términos del Indice Internacional de Rugosidad (IRI por sus siglas en
inglés), a partir de la DGST (Referencia 15). El IRI es un índice
directamente relacionado con la suma de valores absolutos de las
deformaciones superficiales del pavimento por unidad de longitud, que
oscila típicamente entre valores de 2 y 15 metros por kilómetro. Los valores
de IRI que se utilizan en este trabajo fueron obtenidos empleando el equipo
denominado May’s Ride Meter (Referencia 16). 
2.4.5 Curvatura
El dato de curvatura horizontal que la metodología de cálculo de costos de
operación vehicular utilizada en este trabajo emplea, es la suma de los
valores absolutos de las deflexiones entre tangentes sucesivas a lo largo del
tramo, dividida entre la longitud del tramo. Para cada tramo, este dato fue
obtenido del registro en el SIGET del alineamiento horizontal de la Red,
según se indica en el capítulo siguiente.
2.4.6 Cuotas
La información de las cuotas cobradas en los puentes y autopistas de cuota
del país fue obtenida de las páginas de Internet de los diferentes
organismos que tienen a su cargo la administración de las mismas
(CAPUFE, BANOBRAS, etc.) (Referencias 17 y 18). La Tabla 2.2 reproduce
las cuotas cobradas para 75 carreteras o puentes de cuota para los que se
obtuvo esa información. En todos los casos se presenta el nombre de la
carretera o puente, su longitud y las cuotas cobradas a automóviles,
autobuses y camiones de carga según dos grupos, 4 y 5 ejes así como 6 ó
más ejes. 


<!-- page 28 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
16
Tabla 2.2  Cuotas en las Autopistas y Puentes del País
NOMBRE
LONGITUD
(KM)
TARIFA
AUTOMOVILES
TARIFA
AUTOBUSES
TARIFA
CAMIONES
DE 4 Y 5
EJES
TARIFA
CAMIONES
DE 6 O MAS
EJES
GUADALAJARA - TEPIC (CUOTA)
176.60
261
314
482
538
MEXICO - CUERNAVACA (CUOTA)
61.50
70
125
215
315
PUENTE DE IXTLA - IGUALA (CUOTA)
63.58
45
85
165
230
CUERNAVACA - ACAPULCO (CUOTA)
262.78
378
538
702
778
VILLAHERMOSA 
- 
CD. 
DEL 
CARMEN
(PUENTE)
5.07
53
106
170
229
KANTUNIL - CANCUN (CUOTA)
263.24
230
440
955
1270
SONOYTA – MEXICALI (PUENTE)
0.79
0
0
0
0
MONTERREY 
- 
REYNOSA 
(LIBRE)
(PUENTE)
2.70
18
35
35
35
VILLAHERMOSA 
- 
FCO. 
ESCARCEGA
(PUENTE)
2.76
16
30
59
85
IRAPUATO – GUADALAJARA (PUENTE)
3.13
9
14
21
34
ACATLAN DE JUAREZ - COLIMA (CUOTA)
154.01
142
208
348
458
CD. VALLES – TAMPICO (PUENTE)
4.38
0
0
0
0
SAN MARTIN TEXMELUCAN - OCOTOXCO
(CUOTA)
32.17
32
65
117
156
CD. ALEMAN – SAYULA (PUENTE)
1.70
16
29
59
85
MATEHUALA – SALTILLO (CUOTA)
34.50
46
64
85
107
MEXICO - QUERETARO (CUOTA)
115.14
98
196
384
564
QUERETARO - IRAPUATO (CUOTA)
116.19
89
171
327
480
MEXICO - TIZAYUCA (CUOTA)
46.66
25
50
101
151
MEXICO - LA MARQUESA (CUOTA)
21.00
70
210
350
630
MEXICO - PUEBLA (CUOTA)
110.91
96
180
360
520
LOS MOCHIS - CD. OBREGON
185.69
50
78
116
133
PUEBLA - CORDOBA (CUOTA)
162.69
137
282
525
748
COATZACOALCOS 
– 
VILLAHERMOSA
(PUENTE)
2.88
11
21
42
62
TUXPAN – TAMPICO (PUENTE)
2.30
26
50
96
133
TULANCINGO – TUXPAN (CUOTA)
7.06
20
45
90
133
BUENAVISTA - TUXTEPEC
119.36
16
29
59
85
TECATE - TIJUANA (CUOTA)
39.81
55
80
150
192
MEXICALI - TECATE (CUOTA)
20.41
40
82
133
200
TIJUANA - ENSENADA (CUOTA)
89.54
63
129
129
129
CD. DEL CARMEN – CAMPECHE (PUENTE)
3.17
0
0
0
0


<!-- page 29 -->

2  Antecedentes
17
TABLA 2.2  Cuotas en las Autopistas y Puentes del País
NOMBRE
LONGITUD
(KM)
TARIFA
AUTOMOVILES
TARIFA
AUTOBUSES
TARIFA
CAMIONES
DE 4 Y 5
EJES
TARIFA
CAMIONES
DE 6 O MAS
EJES
LIBRAMIENTO DE MATAMOROS
6.24
0
0
0
0
ARMERIA - MANZANILLO (CUOTA)
47.00
67
201
227
356
CHIHUAHUA - MADERA
108.40
0
0
0
0
JIMENEZ - CHIHUAHUA (CUOTA)
138.80
92
232
380
675
EL SUECO - CD. JUAREZ (CUOTA)
89.72
83
175
325
515
DURANGO - GOMEZ PALACIO (CUOTA)
242.04
263
448
849
1103
ZAPOTLANEJO – GUADALAJARA
25.08
32
37
71
94
LAGOS DE MORENO – ZAPOTLANEJO
(CUOTA)
126.39
144
192
280
340
AUT. PEÑON - TEXCOCO (CUOTA)
16.16
23
48
77
110
ENT. MORELOS - PIRAMIDES (CUOTA)
24.35
28
112
140
252
LA PERA - CUAUTLA (CUOTA)
34.16
38
70
106
160
CHAPALILLA - COMPOSTELA (CUOTA)
35.50
27
53
107
145
TEPIC - CRUCERO DE SAN BLAS (CUOTA)
25.00
25
40
70
100
PUEBLA - ATLIXCO (CUOTA)
28.50
0
0
0
0
LIBRAMIENTO DE SAN LUIS POTOSI
33.75
31
57
68
109
MAZATLAN - CULIACAN (CUOTA)
181.50
170
277
318
439
CULIACAN - LOS MOCHIS
221.36
16
30
59
85
LIBRAMIENTO DE NOGALES
6.27
30
60
105
120
LIBRAMIENTO DE EMPALME - GUAYMAS
29.27
22
42
64
75
CD. OBREGON - HERMOSILLO
119.23
50
78
116
133
HERMOSILLO - NOGALES
195.87
50
78
116
133
LIBRAMIENTO PTE. DE TAMPICO (CUOTA)
13.99
20
32
52
62
TEMPOAL -  CANOAS
89.11
14
27
50
75
POZA RICA - VERACRUZ
33.48
16
29
59
85
PASO DEL TORO - ACAYUCAN
232.62
16
29
59
85
T. C. (COATZACOALCOS - SALINA CRUZ) -
NUEVO TEAPA
29.29
11
21
42
62
LIBRAMIENTO DE CORDOBA - PEÑUELAS
5.29
0
0
0
0
TECATE - LA RUMOROSA (CUOTA)
55.50
40
82
133
200
PATZCUARO – URUAPAN
56.50
39
80
117
160
MARAVATIO – ZAPOTLANEJO
226.47
282
442
526
582


<!-- page 30 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
18
Continua Tabla 2.2
LEON 
- 
LAGOS 
DE 
MORENO 
–
AGUASCALIENTES (CUOTA)
116.00
128
181
236
264
LIBRAMIENTO 
CALERA 
DE 
VICTOR
ROSALES
6.49
9
15
43
59
CHIHUAHUA - SACRAMENTO (CUOTA)
21.80
26
66
110
195
CARBONERA - PUERTO MEXICO - LOS
CHORROS
20.94
46
64
85
107
ZACAPALCO - RANCHO VIEJO (CUOTA)
17.30
22
46
80
112
RANCHO VIEJO - TAXCO (CUOTA)
8.34
8
16
27
37
LIBRAMIENTO 
NORORIENTE 
DE
QUERETARO
37.00
30
45
45
60
TEHUACAN – OAXACA
243.00
140
283
341
538
CADEREYTA - REYNOSA (CUOTA)
132.01
160
202
296
329
CHAMPOTON - CAMPECHE (CUOTA)
39.00
43
64
110
143


<!-- page 31 -->

2  Antecedentes
19
2.5
Metodología para el Cálculo de Costos de Operación Vehicular
(COV’s)
Para el cálculo de COV’s de los vehículos de autotransporte de carga, en
este trabajo se utilizó el paquete de cómputo denominado “Vehicle
Operating Cost (VOC)” (Referencia 2). Dicho paquete fue elaborado por el
Banco Mundial, con el propósito de proporcionar a los planeadores una
herramienta que genere información de COV’s que contribuya a una
confiable evaluación técnica y económica de sus opciones de inversión.
Este paquete, estructurado por el Banco Mundial, se basó en diversos
estudios realizados en diferentes países, de los cuales algunos cuentan con
sistemas de transporte carretero con condiciones similares al de México,
como es el caso de Brasil. Dichos estudios se refieren a una serie de
modelos matemáticos para diferentes configuraciones vehiculares, que van
desde automóviles hasta camiones de pasajeros y de carga. Algunos de los
modelos generados son: (I) de consumo de combustibles, (II) de consumo
de lubricantes, (III) de consumo de llantas, (IV) de salario de tripulantes, (V)
de mantenimiento vehicular (incluye mano de obra y refacciones), (VI) de
depreciación del vehículo, etc. En casi todos los casos, el VOC utiliza
valores y modelos matemáticos generados en Brasil.
La función del modelo VOC es simular los efectos de las características
físicas y condiciones del camino en las velocidades de operación de varios
tipos de vehículos, en sus consumos de combustibles y lubricantes, en sus
requerimientos de mantenimiento, etc., y determinar sus costos totales de
operación, para lo cual requiere que sean introducidos previamente algunos
costos unitarios (p. ej., de combustibles, lubricantes, llantas, etc.). Para esto,
el modelo calcula las cantidades consumidas de recursos, tales como litros
de combustible, número de llantas, horas-hombre (h-h) de trabajo, etc., así
como la velocidad del vehículo como función de las características de cada
tipo de vehículo y la geometría, tipo de superficie y condición actual del
camino.
Los pasos seguidos por el modelo en el cálculo de la velocidad, uso de
recursos y costos de operación para un tipo de vehículo dado y una sección
de camino determinada, son:
1 Calcular la velocidad de operación promedio para el vehículo
seleccionado.


<!-- page 32 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
20
2
Calcular las cantidades de recursos utilizadas por cada 1,000 vehículos-
kilómetro (v-km) para los siguientes componentes:
• Consumo de combustibles.
• Consumo de lubricantes.
• Consumo de llantas.
• Tiempo de los tripulantes.
• Tiempo de los pasajeros.
• Tiempo o retención de la carga.
• Mano de obra o de mantenimiento.
• Refacciones.
• Depreciación.
• Interés.
• Indirectos.
3
Aplicar costos unitarios a las cantidades consumidas de recursos para
obtener el costo de operación por cada 1,000 v-km para cada
componente. 
4
Sumar los costos de operación para cada componente con el fin de calcular el
costo de operación vehicular total por cada 1,000 v-km. 


<!-- page 33 -->

21
3  Desarrollo del Sistema
3.1
Enfoque
Como ya se indicó, en este trabajo se utiliza el SIG denominado ArcView
(Referencia 3). Por esta razón, el enfoque que se sigue en el desarrollo del
sistema consiste en ir integrando en un proyecto de ArcView, una serie de
elementos de información que incluyen: (I) datos para la representación
cartográfica de la Red Carretera Federal, (II) datos geométricos y operativos
de la misma, y (III) un conjunto de ecuaciones para estimar los costos de
operación vehicular (COV’s) a partir de los dos tipos de datos anteriores. 
El desarrollo del sistema incluye la modelación de la conectividad entre los
diferentes elementos de la Red, de manera que la modelación resulte
completamente apegada a la realidad en ese sentido. La modelación de la
conectividad hace posible realizar, con el sistema desarrollado, algunas
aplicaciones del Analista o Módulo de Redes de ArcView (Referencia 4).
Las redes urbanas son modeladas con menor detalle.
En ArcView, un proyecto es un archivo que contiene todas las vistas,
tablas, gráficas, etc., utilizadas en una aplicación específica. Una vista es
un mapa en el que se presentan un conjunto de datos espaciales y no-
espaciales. Un dato espacial o rasgo geográfico es aquél vinculado a una
ubicación geográfica determinada (p. ej., un segmento de calle, carretera,
etc.). Cada conjunto de datos ingresados en una vista constituye un tema.
Para cada tema existe una Tabla de Atributos, la cual es una base de datos
que almacena en diferentes campos las características específicas de cada
rasgo geográfico. 
Para el desarrollo de este trabajo se generó un proyecto de ArcView
denominado “red.apr”.
3.2
Información Cartográfica
Los siguientes temas que contienen información cartográfica, fueron
importados de coberturas de ArcInfo del SIGET, a una vista del proyecto
“red.apr” denominada “Modelo Red IMT”:


<!-- page 34 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
22
• 
“Nodos.shp”. En este tema, cada registro corresponde a un punto que
es inicio o terminación de cualquiera de los 9,150 tramos contenidos
en el tema “Highways.shp”. A su vez, dichos puntos corresponden a
entronques de caminos o poblaciones. Este tema contiene 7,000
puntos, de los cuales 3,302 son poblaciones. En este tema se
incluyen, en campos, los siguientes datos para cada nodo: (I) nombre
de la población representada por el nodo (campo “Nombre”); (II)
identificador (“Id01”), constituido por un número consecutivo de dos
dígitos dado al Estado en que se encuentra el nodo (por orden
alfabético del nombre de los Estados), más un número consecutivo de
tres dígitos dado a cada nodo (por orden alfabético del nombre de las
poblaciones); (III) longitud geográfica del nodo (“Longitude”); (IV)
latitud geográfica del nodo (“Latitude”); (V) clave del Estado
(“Clave_edo”), constituida por tres letras correspondientes a la
abreviatura del nombre del Estado; y (VI) variable binaria que es igual
a 1 si el nodo o población es capital de Estado y 0 si no lo es
(“Capital”). 
• 
“Highways.shp”. En este tema o archivo, cada registro corresponde a
una poligonal abierta que representa un tramo de la Red Carretera del
país. Este tema incluye 9,150 tramos (algunos de los cuales son
puentes) correspondientes a las siguientes jurisdicciones: (I) Red
Carretera Federal, (II) Red de Caminos Estatales pavimentados, (III)
autopistas de cuota de Caminos y Puentes Federales (CAPUFE), (IV)
autopistas del Banco Nacional de Obras y Servicios (BANOBRAS),
(V) autopistas concesionadas, y (VI) otros caminos del país. En total
este tema incluye cerca de 100 mil kilómetros de caminos nacionales.
En este tema, los tramos se encuentran clasificados en las 6
jurisdicciones anteriores. Este estudio sólo se refiere a las carreteras
de las jurisdicciones en los puntos (I), (III), (IV) y (V), es decir, no
considera carreteras de “jurisdicción estatal” ni “otros caminos del
país”. La Tabla 3.1 muestra el número de registros en este tema,
correspondiente a las 6 jurisdicciones anteriores, así como la longitud
total de carreteras registrada en este tema para cada jurisdicción. En
esta tabla es evidente que las carreteras a las que se refiere este
trabajo tienen una longitud total de 45,435 kilómetros (48.6% de la
longitud de la red total, repartido en 4,126 tramos). 


<!-- page 35 -->

3  Desarrollo del Sistema
23
Tabla 3.1 Número de Registros y Longitud por Jurisdicción, 
en el Tema “Highway.shp”
JURISDICCION
REGISTROS
%
LONGITUD
(KM)
%
Federal
3,840
42.1
39,797.3
42.6
Estatal
4,914
53.7
46,907.9
50.2
CAPUFE
96
1.0
1,424.3
1.5
BANOBRAS
96
1.0
2,647.9
2.8
Concesionadas
94
1.0
1,565.5
1.7
Otras
110
1.2
1,100.0
1.2
TOTAL
9,150
100.0
93,442.9
100.0
 


<!-- page 36 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
24
La red que se forma con todos los tramos contenidos en este tema,
es una red que tiene continuidad en todas las uniones o
intersecciones entre tramos, lo cual es un requisito para poder usar
en ella el Módulo de Redes de ArcView. Para esto último, hace falta
aún, por supuesto, integrar al sistema, las bases de datos que
permiten estimar el costo (o tiempo, o distancia, etc.) de circular por
cada tramo. Este será el objetivo de la siguiente sección del presente
capítulo. En este tema se incluyen, en campos, los siguientes datos
para cada tramo: (I) nombre del tramo según nomenclatura de la
Dirección General de Servicios Técnicos (DGST) (“Nombre”); (II)
identificador (“Id1”), constituido por un número consecutivo de dos
dígitos dado al Estado en que se encuentra el tramo, más un número
de cinco dígitos correspondiente a la clave dada por la DGST a la
carretera a la que pertenece el tramo, más un número consecutivo de
dos dígitos (p. ej. 01, 02, 03, etc.) dado a los tramos de la carretera
(por orden alfabético de su nombre); (III) longitud según hitos
kilométricos (proporcionada por la DGST) entre cada par de nodos
que definen al tramo (“Length”); (IV) longitud del tramo obtenida con
ArcView 
(“Length_av”); 
(V) 
clasificación 
funcional 
del 
tramo
(“Clas_funcd”), ya sea A2 si es autopista de dos carriles, A4 autopista
de cuatro carriles, C2 carretera libre de dos carriles, C4 carretera libre
de cuatro carriles, C6 carretera libre de seis carriles, P2 puente de
dos carriles, P4 puente de cuatro carriles, VU2 vía urbana de dos
carriles y VU4 vía urbana de cuatro carriles; (VI) número de carriles
del tramo (“Carriles”), ya sean 2, 4 o 6; (VII) variable alfanumérica
binaria que es “SI” si el tramo es de cuota o ”NO“ si no lo es (“Cuota”);
(VIII) variable binaria que define el medio en el que se encuentra el
tramo, “1” si es urbano o “2” si es rural (“Medio”); (IX) variable que
define la jurisdicción a la que pertenece el tramo, según las 6
categorías ya mencionadas (“jurisdic”); y (X) variable formada por 3 ó
4 letras para definir el tipo de superficie del camino, “BREC” para las
Brechas, “PAV” para caminos pavimentados y “REV” para caminos
Revestidos (“Supeficie”). La mayoría de estos datos para carreteras
federales fueron obtenidos de la DGST (Referencias 6, 12, 14 y 15). 
• 
“Manchas.dxf”. En este tema, cada registro corresponde a una
poligonal cerrada que representa algunas ciudades importantes del
país. Este tema contiene 121 ciudades en total, incluyendo algunas


<!-- page 37 -->

3  Desarrollo del Sistema
25
delegaciones que se encuentran en el Distrito Federal y en el Estado
de México. 
• 
“Zonas.shp”. En este archivo, cada registro corresponde a una
poligonal cerrada que representa las 200 diferentes zonas de
desarrollo que considera el Consejo Nacional de Población
(CONAPO) dentro del “Sistema de Ciudades y Distribución de la
Población en México, 2000” (Referencia 19). En este tema se
incluyen, en campos, los siguientes datos para cada tramo: (I) nombre
de la zona de desarrollo según la CONAPO (“Centroide”); (II)
identificador (“Id”), constituido por un número consecutivo de dos
dígitos dado a la zona (por orden alfabético con respecto al nombre
de la zona); (III) el área en Km² de cada zona (“Area_km2”) y (IV)
clave del Estado (“Edo”), constituida por tres letras correspondientes
a la abreviatura del nombre del Estado a la que pertenece la zona. 
• 
“Estados.dxf”. En este archivo cada registro corresponde a un
polígono. El conjunto de todos los polígonos define la división política
(o por Estados) de la República Mexicana. 
Como es evidente, la mayoría de los archivos anteriores contienen en su
nombre la extensión “shp”, que es un distintivo que ArcView utiliza para
identificar los archivos que siguen el formato de datos espaciales de
ArcView (“shapefiles”). Otros complementan su nombre con la extensión
dxf”, que es un distintivo de archivos realizados en diseño asistido por
computadora (CAD).
Una vez importados los temas anteriores a la vista “Modelo Red IMT”, se
obtuvo el mapa que se muestra en la Figura 3.1.  La Tabla de Contenidos, a
la izquierda del mapa, indica los temas incluidos en la vista.  Así mismo, con
una marca a la izquierda de sus letreros descriptivos o leyendas, se señalan
los temas activados o dibujados en la vista. Como es evidente en la figura,
todos los temas han sido activados (“highways.shp” bajo la leyenda “Red
Carretera”, “nodos.shp” bajo la leyenda “Nodos”, “manchas.dxf” bajo la
leyenda “Manchas Urbanas”, “zonas.shp” bajo la leyenda “Zonas” y
“estados.dxf” bajo la leyenda “División Política Estatal”).  En ArcView, los
temas activados son dibujados de abajo hacia arriba según se listan en la
Tabla de Contenidos. 


<!-- page 38 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red
Carretera Federal
26
Figura 3.1   Red Carretera del País Importada de ArcInfo


<!-- page 39 -->

3  Desarrollo del Sistema
27
La Figura 3.1 incluye el nombre de todas las poblaciones dentro del tema
”nodos.shp”. Aunque en la escala de la figura dichos nombres casi no se
perciben, al hacer un acercamiento de una región en el mapa (mediante un
“zoom”), los nombres en ella aumentarán de tamaño de acuerdo con la
nueva escala.
3.3
Integración de Bases de Datos
Se integran a los temas de la vista ”Modelo Red IMT” (principalmente al
tema “Highways.shp”) un conjunto de datos adicionales, necesarios para la
estimación de los COV’s del autotransporte de carga. Estos son, para cada
tramo de la Red, aforo con clasificación vehicular, nivel de servicio, tipo de
terreno, curvatura y cuota de las autopistas. Otro dato requerido para la
estimación de COV’s es el estado del pavimento (rugosidad), el cual ya fue
incorporado dentro de los temas importados. 
3.3.1 Aforos con Clasificación Vehicular
El siguiente paso en la construcción del sistema consistió en vincular al
tema “Highways.shp” de la vista ”Modelo Red IMT”, la información de aforos
y composición vehicular generada por la DGST para la Red Carretera
Federal pavimentada para el año 2000 (Referencia 12).  En realidad lo que
se añadió a cada tramo carretero en la vista (cada registro de la tabla de
atributos correspondiente), fue un promedio de una serie de aforos y
porcentajes de composición vehicular recabados por la DGST en un
conjunto de estaciones ubicadas en la carretera (según la clasificación de
carreteras de la DGST) de la que forma parte el tramo. 
El proceso de vinculación anterior consistió en, primero, generar la base de
datos (o tabla) de valores promedio por carretera, en donde cada registro
corresponde a una carretera identificada mediante la clave dada por la
DGST a la carretera (número de cinco dígitos). Posteriormente, esta base
de datos y el tema “Highways.shp” de la vista ”Modelo Red IMT” fueron
vinculados con base en los identificadores de carretera, mediante la
herramienta “Join” de ArcView. Cabe recordar que en el tema
“Highways.shp”, el identificador de carretera (clave dada por la DGST a la
carretera) está contenido dentro del identificador del tramo.


<!-- page 40 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red 
Carretera Federal 
 
28 
3.3.2 Capacidad y Niveles de Servicio 
Para la Red bajo estudio (carreteras federales pavimentados, autopistas de 
cuota de CAPUFE, autopistas de BANOBRAS y autopistas concesionadas), 
la información de capacidad y niveles de servicio de la DGST (Referencia 
14) fue integrada al sistema siguiendo un procedimiento similar al empleado 
para los aforos con clasificación vehicular. También en este caso, a partir de 
los datos de la DGST (publicados a nivel tramos), en una base de datos se 
generaron para cada carretera valores ponderados (por la longitud de sus 
tramos) de flujo vehicular horario, flujos evaluados para los niveles de 
servicio A a F y el nivel de servicio actual. En esta tabla también se ingresó 
el tipo de terreno promedio para cada tramo, por encontrarse esta 
información también disponible en la publicación sobre capacidad y niveles 
de servicio de la DGST (Referencia 14). Posteriormente, esta base de datos 
y el tema “Highways.shp” de la vista ”Modelo Red IMT” fueron vinculados 
con base en los identificadores de carretera. 
 
3.3.3 Tipo de Terreno 
Por lo dicho en la sección anterior, esta información quedó vinculada al 
tema de la vista denominada “Modelo Red IMT” al vincularse al mismo la 
información de capacidad y niveles de servicio. 
 
3.3.4 Estado del Pavimento 
Esta información fue integrada al sistema siguiendo un procedimiento 
similar al empleado para los datos de Capacidad y Niveles de Servicio.  
 
3.3.5 Curvatura 
Para todos los tramos de la Red considerada, el cociente de la suma de los 
valores absolutos de las deflexiones a lo largo del tramo entre la longitud del 
mismo (C), fue estimado de acuerdo con el siguiente procedimiento:  
• 
Se tomó aleatoriamente una muestra de 100 tramos, calculándose para 
cada uno de ellos, a partir del dibujo de su vista horizontal, el valor de C 
y del cociente de su longitud registrada en ArcView (L) entre la longitud 
en línea recta de su punto de inicio a su punto de terminación (Lr).  


<!-- page 41 -->

3  Desarrollo del Sistema 
 29 
• 
La muestra de 100 pares de datos C versus L/Lr permitió generar la 
siguiente ecuación de regresión, con un coeficiente de determinación 
R2 de 0.8: 
15
.2
6
10
299
.1
1
−
×
−
=
Lr
L
C
                                                Ec. 3.1 
• 
Finalmente, la ecuación anterior fue utilizada, en ArcView, para estimar 
el valor de C para los 4,126 tramos de la Red considerada, a partir de 
sus correspondientes cocientes L/Lr. En éstos, los valores de L se 
obtuvieron directamente del tema “Highways.shp”, en tanto que, para 
contar con los valores de Lr, fue necesario correr una subrutina de 
ArcInfo sobre el tema anterior para generar, primero, las coordenadas 
de los puntos de inicio y terminación de cada tramo. A partir de estas 
coordenadas, posteriormente se obtuvieron los valores de Lr 
correspondientes. 
 
3.3.6 Cuotas 
En este caso, la cuota cobrada en un puente o autopista de cuota fue 
prorrateada entre sus tramos componentes, de acuerdo con la longitud de 
estos últimos en relación con la longitud total del puente o autopista. Las 
cuotas por tramo resultantes fueron posteriormente convertidas a dólares 
utilizando un tipo de cambio de 10 pesos por dólar y vinculadas a la Red 
modelada utilizando el mismo método que en los casos anteriores. 
 
3.3.7 Límite de Velocidad 
De acuerdo con el Reglamento de Tránsito de Carreteras Federales 
(Referencia 20) y prácticas de velocidad de operación de los conductores de 
camiones de carga (Referencia 21), se ingresaron al sistema como valores 
límite de velocidad, 100 km/hr para tramos de carreteras libres y 110 km/hr 
para tramos de autopista de cuota. 
3.4 
Incorporación de Costos de Operación Vehicular 
Otras fuentes (Referencias 22 y 23) reportan los porcentajes de 
participación en el transporte de toneladas-km de carga indicados en la 
Tabla 3.2, para las distintas configuraciones vehiculares autorizadas en 


<!-- page 42 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red 
Carretera Federal 
 
30 
Tabla 3.2 Participación de las Distintas Configuraciones en el 
Transporte Nacional de Toneladas-Km de Carga 
 
TIPO 
DE 
VEHICULO 
% DE LA 
CONFIG. 
DE 
CARGA 
% DE 
VEHICULOS 
CARGADOS 
PESO 
CARGA 
PROM. 
(TON) 
DISTANCIA 
MEDIA 
CON 
CARGA 
(KM) 
DISTRIBUCION 
RELATIVA DE 
TON-KM 
TRANSPOR-
TADAS 
% 
C-2 
32.2 
67.2 
5.8 
421.0 
528.4 
7.2 
C-3 
21.4 
71.2 
11.3 
566.0 
974.5 
13.3 
T3-S2 
22.7 
76.7 
18.5 
738.0 
2,377.1 
32.3 
T3-S3 
18.3 
75.7 
27.0 
718.0 
2,685.6 
36.5 
T3-S2-R4 
2.8 
78.4 
38.9 
726.0 
620.0 
8.4 
Otros 
2.6 
72.2 
14.9 
591.0 
165.3 
2.2 
 
100.0 
 
 
 
7,350.8 
100.0 
 
Fuente: Elaboración propia con base en las Referencias 22 y 23 
 


<!-- page 43 -->

3  Desarrollo del Sistema 
 31 
Carreteras Federales por el Reglamento de Pesos y Dimensiones Máximos 
vigente (Referencia 24). Esta tabla hace evidente que, de todas las 
configuraciones autorizadas por el Reglamento anterior, las 5 indicadas en 
esta tabla son las que mayor contribución realizan al movimiento de 
toneladas-km. 
Puede 
observarse 
en 
la 
tabla 
que 
las 
mayores 
participaciones corresponden a las configuraciones T3-S2 y T3-S3, con 
porcentajes relativamente similares.  
Se selecciona al T3-S2 para las condiciones de operación de plena carga 
(hasta donde permite el peso máximo autorizado por el Reglamento a esta 
configuración) y en vacío, como casos de referencia para la mayoría de los 
análisis que serán efectuados, considerando las participaciones relativas ya 
mencionadas de las configuraciones, así como otras ventajas de carácter 
económico-operativo del T3-S2 (p. ej. observa una mucho menor frecuencia 
de violaciones al Reglamento de Pesos Máximos que el T3-S3, es la 
configuración que más participa en el comercio internacional con Estados 
Unidos (Referencia 22), etc.).  
El enfoque seguido en este trabajo para la integración de COV’s en el 
sistema consiste en adoptar un conjunto de ecuaciones de regresión, 
generadas en la Referencia 1 a partir del programa “Vehicle Operating Cost 
(VOC)” del Banco Mundial, para determinar los costos de operación 
vehicular (COV’s) para los casos de referencia. A partir de éstos y de un 
conjunto de factores de equivalencia, también adoptados de la Referencia 1, 
se obtienen los COV’s para las condiciones de operación en vacío y de 
plena carga de los demás vehículos de carga más comunes. 
Para el T3-S2 a plena carga se asumió una “carga transportada” igual a 
28.8 ton, que junto con el “peso del vehículo vacío” de 15.2 ton, hacen un 
peso bruto vehicular total de 44 ton, el cual es el máximo permitido a esta 
configuración vehicular por el Reglamento de Pesos. Para la condición de 
operación en vacío se ingresó en el programa una “carga transportada” 
igual a 0 ton.  
Algunos estudios anteriores han demostrado que existe una correlación muy 
estrecha entre el COV y la velocidad de operación (VO) (Referencias 25 y 
26). Ha sido también demostrado que, además del peso de la “carga 
transportada” (variable que ya está tomada en cuenta en la condición de 
plena carga o en vacío), las características relevantes a este estudio que 
más influyen en la VO de un vehículo de carga en un segmento carretero, 


<!-- page 44 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red 
Carretera Federal 
 
32 
son: la pendiente del segmento (M); su curvatura (Q), medida por el 
cociente de la suma de los valores absolutos de las deflexiones de las 
curvas a lo largo del segmento entre la longitud del mismo; la calidad de la 
superficie de rodamiento, que puede medirse mediante el Indice 
Internacional de Rugosidad (IRI) (Referencia 27); el límite de velocidad (LV); 
y el nivel de servicio o saturación (S), que es un reflejo del cociente de la 
intensidad del flujo vehicular entre la capacidad efectiva del segmento 
(Referencia 13).  
A partir de los resultados anteriores, la Referencia 1 genera para ambos 
casos de referencia, una ecuación de regresión para la relación del COV 
contra la VO, y otra para la relación de la VO contra las variables M, Q, IRI y 
LV. Así mismo, para ambos casos, se incluye el efecto del nivel de servicio 
(S) mediante un factor de reducción de la VO para niveles inferiores al A. 
Este factor se calcula mediante otra ecuación de regresión, obtenida a partir 
de información contenida en el Manual de Capacidad de Carreteras de los 
Estados Unidos (Referencia 13).  
Para el caso del T3-S2 a plena carga, las ecuaciones de regresión 
generadas en la Referencia 1, son:  
Para la VO contra las variables M, Q, IRI y LV: 
VO = 10.3235 – 1.9331 M + 0.6137 LV – 0.03411 (IRI) (LV)  
+ 0.00219 (M) (Q) – 0.000361 (Q) (LV) + 0.0000295 (IRI) (Q) (LV)  
– 0.0000196 (M) (Q) (LV)                                                              Ec. 3.2 
donde:  
VO, es la velocidad de operación (en Km/h); 
M, es la pendiente (en %); 
Q, es la curvatura del segmento (en grados/km); 
IRI, es el índice internacional de rugosidad (en m/km); y 
LV, es el límite de velocidad (en kilómetros/h). 


<!-- page 45 -->

3  Desarrollo del Sistema 
 33 
La ecuación anterior se obtuvo con un coeficiente de determinación R2 
(indicativo de la calidad del ajuste) de 0.87.  
Para el COV contra la VO: 
         COV = 1,000 + e-53.695 x (300 – VO) 10.903   
 
 
   Ec. 3.3 
donde:  
COV, es el COV por cada 1000 v-k (en dólares/1000 v-k);  
e, es la base de los logaritmos naturales, es decir, 2.71828; y 
VO, es como ya se definió. 
La ecuación anterior se obtuvo con un R2 de 0.93. 
Para el caso del T3-S2 en vacío, las mejores ecuaciones de interpolación 
obtenidas son como se indica enseguida.  
Para la VO contra las variables M, Q, IRI y LV: 
VO = 10.663 + 0.775 LV – 0.044 (IRI) (LV) – 0.0346 (M) (LV) 
 – 0.000399 (Q) (LV) + 0.00302 (IRI) (M) (LV) 
 + 0.0000334 (IRI) (Q) (LV) + 0.0000343 (M) (Q) (LV) 
 – 0.00000312 (IRI) (M) (Q) (LV) 
                                      Ec. 3.4 
donde: 
todas las variables son como ya fueron definidas.  
La ecuación anterior se obtuvo con un R2 de 0.94. 
Para el COV contra la VO: 
         COV = 1,000 + e-45.165  x  (300 – VO) 9.396                                    Ec. 3.5 
 


<!-- page 46 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red 
Carretera Federal 
 
34 
donde: 
todas las variables ya fueron definidas.  
La ecuación anterior se obtuvo con un R2 de 0.90. 
                   FV = [2.67 x (S + 0.8)0.0663] – 2                                           Ec. 3.6 
La relación obtenida para tomar en cuenta el efecto en la VO de niveles de 
servicio menores que A, es: 
donde: 
FV, es el factor de reducción de la VO para niveles de servicio 
inferiores al A;. y 
S, es igual a 5 si el nivel de servicio es “A”, 4 si es “B”, 3 si es “C”, 2 
si es “D”, 1 si es “E” y 0.1 si es “F”. 
La ecuación anterior se obtuvo con un R2 de 1. 
Como ya se indicó, también se toman de la Referencia 1 un conjunto de 
factores que permiten obtener, a partir de los COV’s del vehículo de 
referencia (T3-S2), los COV’s de los otros vehículos más comunes. Dichos 
factores, que también fueron generados a partir de corridas del programa 
VOC, se presentan en la Tabla 3.3. Como puede observarse en la tabla, 
para cada configuración se reportan dos factores, uno para la condición de 
plena carga y otro para la condición en vacío. Esto obedece a que, de 
acuerdo con la Referencia 1, el comportamiento del COV para un mismo 
vehículo entre esas dos condiciones, sí es significativamente diferente.  
En la Tabla 3.3 es también evidente que los dos factores de cada vehículo, 
son muy similares; por lo que en la última columna se presenta el promedio 
de ambos, el cual, con base en este resultado, puede utilizarse de manera 
global para cualquier porcentaje de llenado, a condición de que éste sea el 
mismo entre la configuración de referencia (T3-S2) y aquélla para la cual se 
obtiene el COV a partir del COV del T3-S2.  


<!-- page 47 -->

3  Desarrollo del Sistema 
 35 
Tabla 3.3  Factores de Relación del COV de Diferentes Tipos de 
Vehículos en relación con el T3-S2 
 
Factor de Relación del COV de cada Configuración 
entre el del T3-S2 
CONFIGURACION 
CONDICION DE 
PLENA CARGA 
CONDICION EN 
VACIO 
PROMEDIO 
C2 
0.537 
0.521 
0.529 
C3 
0.599 
0.581 
0.590 
T3-S3 
1.063 
1.061 
1.062 
T3-S2-R4 
1.289 
1.241 
1.265 
 
 


<!-- page 48 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red 
Carretera Federal 
 
36 
El resultado anterior sugiere la posibilidad de evaluar los COV’s para 
cualquier porcentaje de llenado, realizando la interpolación correspondiente 
entre los COV’s en vacío y de plena carga estimados mediante las 
ecuaciones antes mostradas. Este será el enfoque que se aplicará en 
análisis presentados más adelante. Con el fin de facilitar estas 
interpolaciones, la Tabla 3.4 reproduce los tonelajes de carga transportada 
asumidos en este trabajo para la condición de plena carga (100% de 
llenado) de las 5 configuraciones consideradas. Se muestran también en la 
tabla las taras (pesos propios en vacío) y los pesos brutos vehiculares de 
plena carga (máximos reglamentados), considerados en este trabajo. 
El último paso en la construcción del sistema consistió en integrar las 
Ecuaciones 3.2 a 3.6, con el fin de generar la información de costos de 
operación vehicular requerida para cada segmento. El proceso efectuado 
con este propósito consistió en: (I) exportar a un archivo electrónico en el 
formato DBASE (base electrónica de datos), la tabla de atributos del tema 
“Highways.shp” (mediante  la  herramienta “Export” del menú “File” de tablas 
de atributos); y (II) con base en la información contenida en dicho archivo 
(pendiente, IRI, etc.), calcular las diferentes variables indicadas en la Tabla 
3.4, utilizando las herramientas del manejador de bases de datos Visual Fox 
Pro (Referencia 10). Esta última tabla muestra la estructura de la base de 
datos obtenida después de eliminarle los insumos de las Ecuaciones 3.2 a 
3.6, quedándose sólo con los valores calculados. En ella figuran, además 
del identificador de cada tramo (“Id1”). 
 


<!-- page 49 -->

3  Desarrollo del Sistema 
 37 
 
Tabla 3.4  Tara, Tonelaje Máximo de Carga y Peso Bruto Vehicular 
Máximo Considerados para las Configuraciones 
 
CONFIGURACION 
TARA 
(Ton) 
TONELAJE 
MAXIMO DE 
CARGA 
(Ton) 
PESO BRUTO 
VEHICULAR 
MAXIMO 
(Ton) 
C2 
4.1 
13.4 
17.5 
C3 
8.3 
17.7 
26.0 
T3-S2 
15.2 
28.8 
44.0 
T3-S3 
18.8 
29.7 
48.5 
T3-S2-R4 
23.9 
42.6 
66.5 
 
 


<!-- page 50 -->

 
38 
4  Generación de Algunos Resultados 
 
Se presentan dos tipos de resultados, unos que son reflejo directo de los datos 
integrados al sistema, y otros que se obtienen a partir de procesos más 
elaborados.  
4.1 
Obtenidos Directamente de los Datos Integrados al Sistema 
4.1.1. Aforos con Clasificación Vehicular 
Un primer tipo de resultados que pueden generarse a partir del sistema 
desarrollado consiste en la generación de vistas o representaciones 
geográficas en ArcView, obtenidos directamente de los datos integrados al 
sistema. En la Figura 4.1, se muestra el mapa con la representación del 
Transito Diario Promedio Anual (TDPA) asignado a cada carretera. En esta 
representación, los aforos (TDPA) circulantes por los diferentes tramos son 
representados mediante líneas de diferente grosor e intensidad de rojo, 
correspondientes a 5 rangos de valores del TDPA, los cuales se encuentran 
indicados en la Tabla de Contenidos a la izquierda del mapa. En la figura son 
evidentes los tramos, carreteras y corredores nacionales por los que circulan 
los flujos de mayor magnitud.  
Otra manera de ver la información contenida en la Figura 4.1 es a través de las 
distribuciones de frecuencias de tramos y longitudes dentro de los mismos 5 
niveles de TDPA en que se clasifican los tramos en la Figura 4.1. Estas 
distribuciones de frecuencias se presentan en la Tabla 4.1. Tanto en la Figura 
4.1 como en Tabla 4.1 es evidente que un porcentaje importante de la Red 
considerada (más del 50%) soporta flujos vehiculares bastante considerables 
(TDPA por encima de 3000).  


<!-- page 51 -->

4  Generación de Algunos Resultados 
 
39 
 
Figura 4.1 TDPA de las Diferentes Carreteras Federales del País 
(Promedio Ponderado) 
 
 
Tabla 4.1  Porciones de la Red dentro de Diferentes Rangos de TDPA 
 
Rangos de 
TDPA 
No. de tramos 
% 
Longitud de la 
Red (km) 
% 
1,000 – 2,100 
499 
12.1 
9,799.5 
21.6 
2,100 – 3,700 
1,454 
35.2 
14,944.0 
32.9 
3,700 – 5,500 
815 
19.8 
10,012.6 
22.0 
5,500 – 10,000 
962 
23.3 
8,370.8 
18.4 
10,000 – 40,000 
396 
9.6 
2,308.2 
5.1 
TOTAL 
4,126 
100.0 
45,435.0 
100.0 
 


<!-- page 52 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
40 
4.1.2  Vehículos-Kilómetro 
Otro tipo de resultado que puede obtenerse se refiere al cálculo, mediante 
operaciones aritméticas directas sobre los datos integrados, de ciertos valores 
de interés. Algunos de éstos son los vehículos-kilómetro recorridos en toda o 
diferentes tramos de la Red. Para toda la Red, la Tabla 4.1 presenta el 
parámetro anterior calculado a partir de la información de aforos con 
clasificación integrada en el tema “highways.shp” del sistema. En la tabla se 
presenta dicho parámetro para el año 2000, tanto para todo el flujo como 
dividido entre automóviles, autobuses y camiones.  
Los vehículos-kilómetro totales fueron obtenidos de multiplicar el TDPA por la 
longitud de ArcView de cada arco (“Length_av”) por 365 días, almacenando 
los valores resultantes en un nuevo campo de la Tabla de Atributos del tema 
“highways.shp”, siendo estos últimos posteriormente sumados para obtener el 
resultado deseado. Un procedimiento similar fue utilizado para obtener los 
vehículos-kilómetro recorridos por tipo de vehículo (automóviles, autobuses y 
camiones), aunque en este caso hubo de involucrarse en las operaciones 
aritméticas anteriores el porcentaje de composición vehicular correspondiente.  
 
La Tabla 4.2 indica que por la Red considerada se recorrieron alrededor de 80 
mil millones de vehículos-kilómetro en 2000. De éstos, más del 75% fueron 
recorridos por automóviles, más del 5% por autobuses y el 20% restante por 
camiones de carga. En la Tabla 4.2 también se muestran estimados obtenidos 
con base en la longitud de los tramos registrada por la Dirección General de 
Servicios Técnicos (DGST) (“Length”). Como es evidente en la tabla, se 
generan en este caso resultados similares a los obtenidos con base a las 
longitudes de ArcView.  
 
Tabla 4.2  Vehículos-Kilómetro Recorridos en la Red de Interés 
Tipo de 
Vehículo 
Veh-Km (1e6)  
según Long. ArcView 
% 
Veh-Km (1e6)  
según Long. DGST 
% 
Automóviles 
59,117.81 
76.7 
63,103.94 
76.7 
Autobuses 
4,134.12 
5.4 
4,418.71 
5.4 
Camiones 
13,792.68 
17.9 
14,729.14 
17.9 
Total 
77,044.62 
100.0 
82,251.79 
100.0 
 
 


<!-- page 53 -->

4  Generación de Algunos Resultados 
 
41 
La Figura 4.2 muestra una vista en la que los tramos han sido clasificados de 
acuerdo con los 5 rangos de valores de vehículos-kilómetro indicados en la 
Tabla de Contenidos a la izquierda del mapa. En la figura son evidentes los 
tramos, carreteras y corredores nacionales por los que se generan los 
mayores valores de vehículos-kilómetro. 
 
 
 
Figura 4.2  Vehículos - Kilómetro en las Diferentes Carreteras  
Federales del País 
(Promedio Ponderado) 


<!-- page 54 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
42 
4.1.3 Capacidad y Niveles de Servicio 
A partir de la información de capacidad y niveles de servicio integrada al 
sistema, se obtuvo la Tabla 4.3, la cual presenta las distribuciones de 
frecuencias de tramos y longitudes dentro de los 6 niveles de servicio 
considerados por el Manual de Capacidad de Carreteras de los EUA 
(Referencia 13). La Figura 4.3, por su parte, ilustra los tramos dentro de cada 
uno de los 6 niveles de servicio. A partir de la Tabla 4.3 y la Figura 4.3 es 
evidente que la mayoría de la Red considerada opera bajo condiciones de 
congestionamiento adecuadas (con niveles de servicio C o superior). Sólo en 
183 tramos se encontró una operación cercana a la capacidad (4.4% de los 
tramos que representan 3.5% de la longitud total) y en un tramo, 
correspondiente a un cruce marítimo en panga en el estado de Veracruz 
(carretera Gutiérrez Zamora - La Guadalupe), los retrasos reportados son 
elevados por lo que su nivel de servicio fue clasificado como “F”.  
 
Tabla 4.3  Porciones de la Red por Niveles de Servicio 
Nivel de 
Servicio 
No. de tramos 
% 
Longitud de la 
Red (km) 
% 
A 
507 
12.3 
7,755.0 
17.1 
B 
1,031 
25.0 
13,565.5 
29.9 
C 
1,848 
44.8 
17,751.0 
39.0 
D 
556 
13.5 
4,789.3 
10.5 
E 
183 
4.4 
1,573.5 
3.5 
F 
1 
0.0 
0.7 
0.0 
TOTAL 
4,126 
100.0 
45,435.0 
100.0 
 
 
 


<!-- page 55 -->

4  Generación de Algunos Resultados 
 
43 
 
Figura 4.3. Carreteras dentro de los Diferentes Niveles de Servicio 
(Promedio Ponderado) 
 
 


<!-- page 56 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
44 
 
4.1.4  
Tipo de Terreno 
 
A partir de la información de tipo de terreno para cada tramo de la Red 
considerada, se obtuvieron la Tabla 4.4 y la Figura 4.4,  las cuales clasifican a 
los tramos según se encuentren en terreno plano, lomerío o montañoso. En la 
Tabla 4.4 es evidente que un porcentaje muy considerable de la Red (cerca 
del 70% en términos del número de tramos y de la longitud) se encuentra en 
terreno de orografía complicada (en lomerío o en terreno montañoso). 
 
4.1.5 
Estado del Pavimento 
 
A partir de los datos de Indice Internacional de Rugosidad (IRI) integrados al 
sistema, se obtuvieron la  Tabla  4.5  y  la  Figura  4.5,  las  cuales  clasifican  
a los tramos en bueno, regular y malo, según presentaron valores de IRI 
menores que 4, entre 4 y 8, y mayores que 8, respectivamente. 
 
Tabla 4.4  Porciones de la Red por Tipo de Terreno 
Tipo de 
Terreno 
No. de tramos 
% 
Longitud de la 
Red (km) 
% 
Plano 
1,342 
32.5 
14,288.1 
31.4 
Lomerío 
2,475 
60.0 
26,343.5 
58.0 
Montañoso 
309 
7.5 
4,803.4 
10.6 
TOTAL 
4,126 
100.0 
45,435.0 
100.0 
 


<!-- page 57 -->

4  Generación de Algunos Resultados 
 
45 
 
Figura 4.4  Tipo de Terreno en las Diferentes Carreteras  
Federales del País 
(Promedio Ponderado) 


<!-- page 58 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
46 
En la Tabla 4.5 es evidente que un porcentaje muy considerable de la Red 
(cerca del 90% en términos del número de tramos y de la longitud) se 
encuentra en condiciones aceptables (estado bueno o regular).  
 
Tabla 4.5  Porciones de la Red por Estado del Pavimento 
Estado del 
Pavimento 
No. de tramos 
% 
Longitud de la 
Red (km) 
% 
Bueno (IRI 
menor que 4) 
1,091 
26.4 
13,764.5 
30.3 
Regular (IRI 
entre 4 y 8) 
2,687 
65.1 
26,271.6 
57.8 
Malo (IRI 
mayor que 8) 
348 
8.5 
5,398.9 
11.9 
TOTAL 
4,126 
100.0 
45,435.0 
100.0 
 
Figura 4.5  Estado del Pavimento en las Diferentes Carreteras  
Federales del País 
(Promedio Ponderado) 


<!-- page 59 -->

4  Generación de Algunos Resultados 
 
47 
4.1.6 
Curvatura 
 
Después de haber estimado para todos los tramos los cocientes de la suma de 
los valores absolutos de sus deflexiones entre su longitud (C), según el 
procedimiento indicado en el capítulo anterior, se procedió a obtener la Tabla 
4.6 y la Figura 4.6. Estas clasifican a los tramos de acuerdo con los siguientes 
tres niveles de curvatura: (I) C menor que 100°/Km, (II) C entre 100 y 500°/Km, 
y (III) C mayor que 500°/Km. En la Tabla 4.6 es evidente que un porcentaje 
muy significativo de la Red, tiene valores considerables de C (mayores a 
100°/Km). En la Figura 4.6 es evidente que las mayores curvaturas se 
presentan en sitios de orografía complicada (zonas serranas). 
 
 
Tabla 4.6. Porciones de la Red por Niveles de Curvatura Horizontal 
Niveles de 
Curvatura (C) 
(°/Km) 
No. de tramos 
% 
Longitud de la 
Red (km) 
% 
Menor de 100 
2,305 
55.9 
14,681.5 
32.3 
Entre 100 y 500 
1,811 
43.9 
30,446.1 
67.0 
Mayor de 500  
10 
0.2 
307.4 
0.7 
TOTAL 
4,126 
100.0 
45,435.0 
100.0 


<!-- page 60 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
48 
 
Figura 4.6  Niveles de Curvatura Horizontal en las Diferentes Carreteras 
Federales del País (Promedio Ponderado) 
 
 
 
4.1.7  
Otros Resultados de este Tipo 
 
Con el sistema generado es posible obtener, directamente de otros datos 
integrados al sistema, tablas y figuras similares a las mostradas anteriormente 
para algunos de esos datos. De esta manera, sería posible generar tablas y 
figuras en relación con las cuotas cobradas en puentes y autopistas de cuota, 
los límites de velocidad, los COV’s por kilómetro, por tramo, etc. 
 


<!-- page 61 -->

4  Generación de Algunos Resultados 
 
49 
4.2 
Otros Resultados a Partir de Procesos más Elaborados. 
 
4.2.1  COV Totales del Flujo de Vehículos de Carga (CTF) y por Tonelada-
Kilómetro (TK) 
 
A partir de la información en la segmentación por tramos sobre (I) flujo diario 
de los diferentes tipos de vehículos de carga y sus pesos brutos vehiculares 
promedio con que circulan por las carreteras y sus correspondientes 
porcentajes de llenado en la Tabla 4.7 (Referencia 22), (II) COV del T3-S2 
vacío y a plena carga para ambos sentidos de circulación, (III) los peajes en las 
autopistas y puentes de cuota para las distintas configuraciones y (IV) los 
factores de relación del COV de las diferentes configuraciones en relación con 
el T3-S2 (Tabla 3.3 en el Capítulo 3), se aproximaron los COV totales del flujo 
de vehículos de carga (CTF) a través de cada tramo mediante la siguiente 
ecuación:  
 
 
4.1
 
Ec.
 
......
..........
  
  
CuoT3S2R4
CV)
(CL
   
100
%LT3S2R4
CV
100
%T3S2R4
TDPA  
  
1.265
  
CuoT3S3
CV)
(CL
   
100
%LT3S3
CV
100
%T3S3
TDPA  
  
1.062
  
CuoT3S2
CV)
(CL
   
100
%LT3S2
CV
100
%T3S2
TDPA  
  
1.000
 
CuoC3
CV)
(CL
   
100
%LC3
CV
100
%C3
TDPA  
  
0.569
 
CuoC2
CV)
(CL
   
100
%LC2
CV
100
%C2
TDPA  
  
0.529
CTF










+
−
+
×






×
×
+










+
−
+
×






×
×
+










+
−
+
×






×
×
+










+
−
+
×






×
×
+










+
−
+
×






×
×
=
 
en la que: 
 
CTF, es el COV total del flujo diario de vehículos de carga en el tramo (US$);  


<!-- page 62 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
50 
TDPA, es el Tránsito Diario Promedio Anual (vehículos);  
%C2, es el porcentaje de vehículos C2 en la composición vehicular;  
 
 
Tabla 4.7 
Porcentajes Promedio de Llenado de las  
Diferentes Configuraciones 
 
Tipo de 
Vehículo 
PBV 
Promedio 
(Ton) 
Tara 
(Ton) 
Carga 
Promedio 
(Ton) 
Tonelaje 
Máximo de 
Carga 
% de 
Llenado 
C2 
7.7 
4.1 
3.6 
13.4 
26.9 
C3 
16.4 
8.3 
8.1 
17.7 
45.8 
T3-S2 
28.4 
15.2 
13.2 
28.8 
45.8 
T3-S3 
39.7 
18.8 
20.9 
29.7 
70.4 
T3-S2-R4 
54.0 
23.9 
30.1 
42.6 
70.7 
 
 
 
%LC2, es el porcentaje de llenado promedio del vehículo C2;  
%LC3, es el porcentaje de llenado promedio del vehículo C3;  
%LT3S2, es el porcentaje de llenado promedio del vehículo T3S2;  
%LT3S3, es el porcentaje de llenado promedio del vehículo T3S3;  
%LT3S2R4, es el porcentaje de llenado promedio del vehículo T3S2R4;  
CuoC2, es el peaje para el vehículo C2 en el tramo (US$);  
CuoC3, es el peaje para el vehículo C3 en el tramo (US$);  
CuoT3S2, es el peaje para el vehículo T3S2 en el tramo (US$);  
CuoT3S3, es el peaje para el vehículo T3S3 en el tramo (US$); y 
CuoT3S2R4, es el peaje para el vehículo T3S2R4 en el tramo (US$).  
 
Así mismo a partir de la información en la misma segmentación sobre (I) flujo 
diario de los diferentes tipos de vehículos de carga y sus correspondientes 
tonelajes promedio de carga transportados en la Tabla 4.7 y (II) longitud de los 


<!-- page 63 -->

4  Generación de Algunos Resultados 
 
51 
tramos, se obtuvieron las toneladas-kilómetro de carga (TK) circulando 
diariamente por cada tramo mediante la siguiente expresión:  
 
(
)
(
)
(
)
(
)
(
)
Ec.4.2
 
......
  
1000
LAV
100
TDPA
  
PT3S2R4
   
%T3S2R4
 
 
PT3S3
  
%T3S3
 
  
PT3S2
  
%T3S2
 
 
PC3
  
%C3
 
 
PC2
  
%C2
 
TK
 x
x 
×




×
+
×
+
×
+
×
+
=
    
 
donde: 
 
TK, son las toneladas-kilómetro de carga circulando diariamente por el tramo; 
PC2, es el tonelaje promedio de carga transportado por el vehículo C2;  
PC3, es el tonelaje promedio de carga transportado por el vehículo C3;  
PT3S2, es el tonelaje promedio de carga transportado por el vehículo T3S2;  
PT3S3, es el tonelaje promedio de carga transportado por el vehículo T3S3;  
PT3S2R4, es el tonelaje promedio de carga transportado por el vehículo 
T3S2R4;  
LAV, es la longitud del tramo en metros; y 
las demás variables son como ya fueron definidas. 
 
Los dos valores anteriores (CTF y TK) para todos los tramos fueron calculados 
con Visual Fox Pro (Referencia 10), a partir de la información en un archivo en 
formato DBASE obtenido de la exportación de la tabla de atributos de la 
segmentación por tramos. Una vez obtenidos esos valores en dicho archivo, 
éste fue vinculado de vuelta a la tabla de atributos de la segmentación anterior. 
Como resultado de la agregación en ArcView de esos valores para todos los 
tramos, se obtuvo que por la Red modelada se genera un CTF de 41'598,991 
de dólares por día en la transportación diaria de 340'452,427 toneladas-
kilómetro de carga. Las cifras anteriores representan un CTF/TK promedio de 
0.122 dólares/tonelada-kilómetro, el cual resulta 30% por debajo de su 
correspondiente valor promedio reportado para Estados Unidos (Referencia 
28) y 20% por encima del de Canadá (Referencia 29).  
 


<!-- page 64 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
52 
4.2.2 Identificación de Corredores Prioritarios para Modernización 
 
Criterios 
 
El sistema generado también permite identificar los corredores prioritarios para 
el autotransporte nacional de carga, a ser modernizados en el futuro cercano. 
Lo anterior es posible si se utilizan combinadamente las potencialidades del 
sistema manejado con ArcView y su Módulo de Redes de ArcView, junto con 
información existente de origen a destino (O-D) de los viajes del autotransporte 
de carga como la que se muestra en la Tabla 4.8 (Referencia 30).  Esta última 
proviene de estaciones de encuesta O-D de vehículos de carga instaladas 
durante las 24 horas de todos los días de una semana determinada, en 
diferentes sitios de la Red Carretera Federal (Referencia 22).  La Tabla 4.8 
muestra los 40 pares O-D que, según la información recopilada en las 
estaciones instaladas en los años más recientes (1999 y 2000), observan 
mayores flujos de vehículos de carga por día. Como es evidente a partir de la 
última columna de la tabla, los 40 pares O-D en ella comprenden 23.15% del 
total de viajes del autotransporte de carga.  
La identificación de corredores más importantes a modernizar puede 
efectuarse con base en los siguientes tres criterios:  
1 La minimización del costo de modernización o construcción (CM). En este 
caso, la red de corredores queda definida por el árbol de expansión mínima 
(AEM) (Referencia 31) que conecte a todas las poblaciones que se deseen 
comunicar entre sí. Esta solución, en contraparte, hace caso omiso de lo 
que pudiese ser más conveniente desde el punto de vista de la 
minimización de los COV’s.  


<!-- page 65 -->

4  Generación de Algunos Resultados 
 
53 
Tabla 4.8  Pares O-D con Mayor Flujo Diario de Vehículos de Carga  
 
P A R E S 
ORIGEN 
DESTINO 
 
 
No. 
POBLACION 
CLAVE 
POBLACION 
CLAVE 
 
 
VEH./DIA 
% 
DEL 
TOTAL 
NACIONAL  
 
         % 
ACUMULADO 
1 
NUEVO LAREDO 
TMS03 
MEXICO 
DF01 
1,991 
1.71 
1.71 
2 
MEXICO 
DF01 
TOLUCA 
MEX01 
1,630 
1.40 
3.11 
3 
TOLUCA 
MEX01 
MEXICO 
DF01 
1,624 
1.40 
4.51 
4 
HERMOSILLO 
SON01 
HERMOSILLO 
SON01 
1,180 
1.02 
5.53 
5 
TIJUANA 
BCN04 
ENSENADA 
BCN03 
980 
0.84 
6.37 
6 
MEXICO 
DF01 
PUEBLA 
PUE01 
960 
0.83 
7.19 
7 
MEXICO 
DF01 
GUADALAJARA 
JAL01 
952 
0.82 
8.01 
8 
ENSENADA 
BCN03 
TIJUANA 
BCN04 
928 
0.80 
8.81 
9 
CD. JUAREZ 
CHI05 
CHIHUAHUA 
CHI01 
811 
0.70 
9.51 
10 
GUADALAJARA 
JAL01 
MEXICO 
DF01 
794 
0.68 
10.19 
11 
MONTERREY 
N L01 
NUEVO LAREDO 
TMS03 
784 
0.67 
10.87 
12 
CHIHUAHUA 
CHI01 
CD. JUAREZ 
CHI05 
782 
0.68 
11.54 
13 
MEXICO 
DF01 
NUEVO LAREDO 
TMS03 
770 
0.66 
12.2 
14 
MEXICO 
DF01 
VERACRUZ 
VER02 
763 
0.66 
12.86 
15 
PUEBLA 
PUE01 
MEXICO 
DF01 
763 
0.66 
13.52 
16 
MONTERREY 
N L01 
MEXICO 
DF01 
740 
0.64 
14.15 
17 
NUEVO LAREDO 
TMS03 
MONTERREY 
N L01 
719 
0.62 
14.77 
18 
MEXICO 
DF01 
MONTERREY 
N L01 
694 
0.60 
15.37 
19 
MEXICO 
DF01 
VILLAHERMOSA 
TAB01 
650 
0.56 
15.93 
20 
VERACRUZ 
VER02 
MEXICO 
DF01 
634 
0.55 
16.47 
21 
GUADALAJARA 
JAL01 
ZAPOTLANEJO 
JAL07 
487 
0.42 
16.89 
22 
MEXICO 
DF01 
QUERETARO 
QRO01 
472 
0.41 
17.30 
23 
ZAPOTLANEJO 
JAL07 
GUADALAJARA 
JAL01 
441 
0.38 
17.68 
24 
GUADALAJARA 
JAL01 
TEPATITLAN 
JAL04 
440 
0.38 
18.06 
25 
NOGALES 
SON06 
HERMOSILLO 
SON01 
437 
0.38 
18.43 
26 
MEXICO 
DF01 
SN LUIS POTOSI 
SLP01 
425 
0.37 
18.80 
27 
TEPATITLAN 
JAL04 
GUADALAJARA 
JAL01 
420 
0.36 
19.16 
28 
SN LUIS POTOSI 
SLP01 
MEXICO 
DF01 
407 
0.35 
19.51 
29 
QUERETARO 
QRO01 
MEXICO 
DF01 
376 
0.32 
19.84 
30 
SAHUAYO 
MIC04 
JIQUILPAN 
MIC06 
367 
0.32 
20.15 
31 
CUITZEO 
MIC11 
MORELIA 
MIC01 
363 
0.31 
20.46 
32 
JIQUILPAN 
MIC06 
SAHUAYO 
MIC04 
361 
0.31 
20.77 
33 
VILLAHERMOSA 
TAB01 
MEXICO 
DF01 
361 
0.31 
21.08 
34 
MORELIA 
MIC01 
CUITZEO 
MIC11 
355 
0.31 
21.39 
35 
MONTERREY 
N L01 
GUADALAJARA 
JAL01 
355 
0.31 
21.69 
36 
OAXACA 
OAX01 
TELIXTLAHUACA 
OAX10 
352 
0.30 
22.00 
37 
MEXICO 
DF01 
COATZACOALCOS VER24 
341 
0.29 
22.29 
38 
HERMOSILLO 
SON01 
NOGALES 
SON06 
334 
0.29 
22.58 
39 
GUADALAJARA 
JAL01 
EL SALTO 
JAL05 
332 
0.29 
22.86 
40 
COATZACOALCOS 
VER24 
MEXICO 
DF01 
329 
0.28 
23.15 
 
OTROS 
 
89,308 
76.15 
100.00 
              TOTAL 
 
116,212 
100.00 
 
 


<!-- page 66 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
54 
2  La minimización de COV’s. Bajo este enfoque se trata de conectar a todas 
las poblaciones de interés, privilegiando la implementación de líneas de 
comunicación directas entre los pares O-D de mayor flujo. Por lo tanto, la 
red de corredores a modernizar queda definida fundamentalmente por el 
juego de caminos más cortos (de menor COV) entre los pares O-D de 
mayor importancia. La determinación de caminos más cortos entre dos 
sitios determinados de una red dada, así como sus correspondientes 
distancia o COV mínimos, es uno de los problemas que pueden resolverse 
con el Módulo de Redes de ArcView, obviamente si se cuenta con el 
sistema de COV’s en todos los arcos de la red, como es el caso ahora en 
este trabajo. En contraparte, esta solución no garantiza la conectividad 
entre todas las poblaciones de interés.  
3 Otro adicional que fuese la combinación de los dos anteriores y que por lo 
mismo favoreciese la minimización de COV’s, garantizando al mismo tiempo 
la conectividad de todas las poblaciones de interés. En este caso el enfoque 
más razonable sería complementar la red obtenida según el criterio 2, con 
elementos de la obtenida según el criterio 1 para completar la comunicación 
de todas las poblaciones de interés (conectividad de la red).  
 
Ejemplo de Aplicación 
Como ejemplo de la aplicación de los tres criterios anteriores se presenta la 
Figura 4.7, la cual muestra el AEM para las 12 poblaciones involucradas en los 
14 primeros pares O-D de la Tabla 4.8.  Este AEM resulta con una longitud 
total de 4,428 kilómetros que si se multiplica por un costo promedio de 
modernización de 500 mil dólares por kilómetro, da un costo total de 
modernización (CM) de 2,214 millones de dólares. Por otra parte, obteniendo 
con el Módulo de Redes de ArcView los caminos más cortos sobre este AEM 
entre cada uno de los 14 primeros pares O-D de la Tabla 4.8 así como sus 
COV’s y agregando la multiplicación de éstos por sus flujos correspondientes 
en la Tabla 4.8 (antepenúltima columna de la tabla) y por 365 días por año, se 
obtiene un COV total anual de 4,279 millones de dólares. Por lo tanto, la 
implementación del criterio 1 representa un costo total durante el primer año 
(CT = CM + COV) de 6,493 millones de dólares. Las cifras antes obtenidas 
indican que para un horizonte de análisis de un año, el COV prevalece por 
encima del CM. Obviamente, para mayores horizontes de análisis, el 
predominio del COV sobre el CM tendería a hacerse mayor.  


<!-- page 67 -->

4  Generación de Algunos Resultados 
 
55 
 
 
 
Figura 4.7  Red Obtenida a partir de la Minimización de Costos de 
Modernización o Construcción (AEM)  
 
 
 
 
La Figura 4.8 ilustra la red que se obtiene, atendiendo al criterio 2, si se 
conectan entre sí a través de sus caminos más cortos los 14 pares O-D 
considerados. Como es evidente en la figura, esta red no tiene conectividad 
total.  
 


<!-- page 68 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
56 
 
 
Figura 4.8  Red Obtenida a partir de la Minimización de los COV’s  
(con la Red Obtenida del Criterio Anterior) 
 
La Figura 4.9 ilustra la red completamente conectada que se obtiene de aplicar 
el criterio 3. Esta solución tiene una longitud total de 4,948 kilómetros que si se 
multiplica por el costo promedio de modernización por kilómetro de 500 mil 
dólares, da un costo total de modernización (CM) de 2,474 millones de dólares. 
Por otra parte, para la circulación de los flujos de los 14 primeros pares O-D de 
la Tabla 4.8 se obtiene un COV total de 3,417 millones de dólares. Por lo tanto, 
la implementación de esta solución representa un costo total (CT) de 5,891 
millones de dólares. Como es evidente, en este caso el COV también 
prevalece por encima del CM. Esta solución tiene un CT menor que el obtenido 
del criterio 1, por ser más congruente con la minimización de COV’s, que es el 
componente predominante del CT.  


<!-- page 69 -->

4  Generación de Algunos Resultados 
 
57 
 
 
Figura 4.9  Red Obtenida a partir de la Combinación de los Dos Criterios 
Anteriores (Minimización de COV’s y del Costo de Modernización) 
 
 
La gráfica en la Figura 4.10 presenta la evolución de CM, COV y CT para las 
longitudes totales de red obtenidas para los criterios 1 y 3. La línea de CT en la 
gráfica reitera la conveniencia de favorecer los pares O-D de mayor 
importancia al definir la red a modernizar.  
 
 
 


<!-- page 70 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
58 
 
 
Figura 4.10  Gráfica Comparativa de Costos para los Criterios 1 y 3 
 
 
Red Total Nacional a Modernizar 
 
La Figura 4.11 ilustra la fracción primordial de la Red Carretera Federal, a ser 
modernizada; ésta fue obtenida de aplicar las recomendaciones antes 
generadas  (criterio 3), considerando a su vez los 132 pares O-D de mayor flujo 
de vehículos de carga reportados en la Referencia 30. Estos pares 
comprenden 40.0% del total nacional de viajes del autotransporte de carga.  
0
1,000
2,000
3,000
4,000
5,000
6,000
7,000
4,400
4,500
4,600
4,700
4,800
4,900
5,000
DISTANCIA (KM)
COSTOS (MILLONES DE DOLARES)
Costo de Operación Vehicular
Costo de Mantenimiento
Costo de Transporte


<!-- page 71 -->

4  Generación de Algunos Resultados 
 
59 
La red obtenida en la Figura 4.11 tiene una extensión de 30,153 kilómetros y 
puede considerarse como congruente con el Programa de Modernización de 
Ejes Carreteros de la SCT (Referencia 32).  
 
 
 
Figura 4.10  Ejemplo de Red Total Nacional a Modernizar 
 
 


<!-- page 72 -->

 
60 
5  Conclusiones 
5.1 
Conclusiones 
Las conclusiones más importantes derivadas de este trabajo son: 
 
• De manera similar que en un estudio previo realizado sólo para las 
Carreteras Federales del Estado de Veracruz (Referencia 1), se reconoce 
que la estimación de costos de operación vehicular (COV) en este trabajo 
no considera algunos factores (externalidades) que pueden ser importantes. 
El más importante de ellos es el costo por accidentes. Al respecto, se tienen 
evidencias de que la circulación por alternativas de cuota es más segura (en 
términos del índice de costo de accidentes por vehículo-kilómetro recorrido) 
que por alternativas libres (Referencia 33). 
 
• El sistema generado permite desplegar, a nivel de tramos de la Red 
Carretera Federal, diferentes tipos de información sobre el estado de los 
mismos (aforo, nivel de servicio, tipo de terreno, IRI, curvatura, cuotas y 
costos de operación vehicular). En este sentido, puede ser una herramienta 
útil para diferentes tipos de gestión de mejoramiento de la Red. 
 
• Se obtiene que por la Red Carretera Federal se genera un COV promedio 
de 0.122 dólares/tonelada-kilómetro transportada, el cual es 30% menor 
que su correspondiente valor para los Estados Unidos y 20% superior al de 
Canadá. Lo anterior evidencia que el COV del autotransporte de México es 
competitivo en relación con el de los otros dos países, aunque otros 
componentes del costo de transporte (aseguramiento de vehículos y carga) 
pueden restarle competitividad a los productos nacionales. 
 
• Con base al sistema generado, se analizan distintos criterios de 
identificación de corredores prioritarios. Se obtiene que el más conveniente 
de ellos es el que resulta en la subred que privilegia a los recorridos más 
directos entre los pares origen-destino (O-D) más importantes y, a su vez, 
logra la conectividad entre los sitios más importantes del país. 
 
• El sistema generado apoya las labores de planeación, investigación y toma 
de decisiones por parte del Sector Transporte. Genera información de 
utilidad para los administradores y operadores de la infraestructura. Permite 
a los autotransportistas conocer sus costos operativos, como apoyo a la 
programación de sus actividades. 
 


<!-- page 73 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red Carretera 
Federal 
61 
5.2 
Recomendaciones 
Las recomendaciones más importantes son: 
 
• Los procesos de organización, planeación y gestión del transporte deben 
realizarse utilizando las tecnologías más modernas y eficientes de manejo 
de información. Por tal razón, se recomienda seguir utilizando los Sistemas 
de Información Geográfica (SIG) y los sistemas de Posicionamiento Global 
(GPS), que son herramientas que pueden seguirse explorando y adecuando 
a las necesidades específicas del transporte por su versatilidad para la 
administración, evaluación y análisis de gran cantidad de datos 
referenciados geográficamente. 
 
• Se recomienda ampliar los análisis de identificación de corredores, 
considerando la información O-D más completa y reciente posible. 
 


<!-- page 74 -->

 
62 
Referencias 
 
1 
Aburto A. y Mendoza A. SIG para el Análisis de Costos de Operación 
de Vehículos de Carga en Carreteras Federales. Caso Estado de 
Veracruz, Publicación Técnica No. 153, Instituto Mexicano del 
Transporte, Sanfandila, Qro., 2000.  
2 
The Highway Design and Maintenance Standards Series, VOC Model, 
Version 3.0. The World Bank, Washington, D.C., U.S.A.,1989.  
3 
ArcView GIS, Version 3.2. The Geographic Information System for 
Everyone. Enviromental Systems Research Institute, U.S.A.,1997.  
4 
ArcView Network Analyst. Optimum Routing, Closest Facility and 
Service Area Analysis. Environmental Systems Research Institute, 
U.S.A., 1998. 
5 
Backhoff P., Miguel A., Tristán Ruiz Lang y Juan Carlos Vázquez 
Paulín. Sistema de Información GeoEstadística para el Transporte 
(SIGET), Instituto Mexicano del Transporte, Sanfandila, Qro., 1999. 
6 
Sistema de Clasificación de las Carreteras Federales. Dirección 
General 
de 
Servicios 
Técnicos 
(DGST), 
Subsecretaría 
de 
Infraestructura, Secretaría de Comunicaciones y Transportes (SCT), 
México, D.F., 2000.  
7 
Memorias del IV Congreso Latinoamericano de Usuarios del ArcInfo y 
Erdas. México D. F., noviembre de 1996.  
8 
García O., Gabriela y Miguel A. Backoff P. Los Sistemas de 
Información Geográfica y el Transporte. Publicación Técnica No. 32, 
Instituto Mexicano del Transporte, Sanfandila, Qro., 1992. 
9 
ArcInfo GIS, Environmental System Research Institute, Inc., U.S.A., 
1998.  
10 
Sistema de Programación de Bases de Datos Relacionales, Visual 
FoxPro, Versión 5.0, Microsoft Corporation, Inc., 1998. 
11 
Excel, Versión 5.0, Microsoft Corporation, Inc., 2000. 


<!-- page 75 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red 
Carretera Federal 
63 
12 
Datos Viales 2000, Dirección General de Servicios Técnicos, 
Secretaría de Comunicaciones y Transportes, México, D. F., 2001. 
13 
Highway Capacity Manual (Manual de Capacidad de Carreteras), 
Special Report 209, Transportation Research Board. National 
Research Council, Washington, D. C., U.S.A., 1985. 
14 
Capacidad y Niveles de Servicio en la Red Federal de Carreteras, 
Dirección 
General 
de 
Servicios 
Técnicos, 
Secretaría 
de 
Comunicaciones y Transportes, México, D. F., 1998.  
15 
Índice Internacional de Rugosidad para las Carreteras Federales, 
Dirección 
General 
de 
Servicios 
Técnicos, 
Secretaría 
de 
Comunicaciones y Transportes, México, D. F., 2000. 
16 
Haas R., y W. R. Hudson. Pavement Management Systems, Robert 
E. Krieger Publishing Company, Malabar, Florida, U.S.A., 1982. 
17 
Cuotas en Puentes y Autopistas de Cuota 2001. Caminos y Puentes 
Federales 
de 
Ingresos 
y 
Conexos 
(CAPUFE). 
http://www.capufe.gob.mx 
18 
Unidad de Autopistas de Cuota. http://www.sct.gob.mx 
19 
“Sistema de Ciudades y Distribución de la Población en México”, 
Consejo Nacional de Población (CONAPO), 2000.  
20 
Reglamento de Tránsito de Carreteras Federales. Presidencia de la 
República, 1976.  
21 
Chavarría V., J. M., A. Mendoza D. y E. Mayoral G. Algunas Medidas 
para Mejorar la Seguridad Vial en las Carreteras Nacionales. 
Publicación Técnica No. 89, Instituto Mexicano del Transporte, 
Secretaría de Comunicaciones y Transportes, Sanfandila, Qro., 1996.  
22 
Gutiérrez H., J. L., A. Mendoza D. y P. Dontchev K. Estudio 
Estadístico de Campo del Autotransporte Nacional. Análisis 
Estadístico de la Información Recopilada en las Estaciones 
Instaladas en 1995 y 1996. Documento Técnico No. 20, Instituto 
Mexicano 
del 
Transporte, 
Secretaría 
de 
Comunicaciones 
y 
Transportes, Sanfandila, Qro., 1999.  


<!-- page 76 -->

Referencias 
 
64 
23 
Mendoza D., A. y J. G. Reyes G. Estudio de Pesos y Dimensiones de 
los Vehículos que Circulan Sobre las Carreteras Nacionales. 
Impactos Económicos de la Reglamentación y el Control de Pesos. 
Publicación Técnica No. 51, Instituto Mexicano del Transporte, 
Secretaría de Comunicaciones y Transportes, Sanfandila, Qro., 1994. 
24 
Reglamento Sobre el Peso, Dimensiones y Capacidad de los 
Vehículos de Autotransporte que Transitan en los Caminos y Puentes 
de 
Jurisdicción 
Federal. 
Secretaría 
de 
Comunicaciones 
y 
Transportes, México, D.F., 1997.  
25 
Aguerrebere S., R. y F. Cepeda N. Elementos de Proyecto y Costos 
de Operación en Carreteras. Publicación Técnica No. 20, Instituto 
Mexicano 
del 
Transporte, 
Secretaría 
de 
Comunicaciones 
y 
Transportes, Sanfandila, Qro., 1991.  
26 
Aguerrebere S., R. y F. Cepeda N. Estado Superficial y Costos de 
Operación en Carreteras. Publicación Técnica No. 30, Instituto 
Mexicano 
del 
Transporte, 
Secretaría 
de 
Comunicaciones 
y 
Transportes, Sanfandila, Qro., 1991. 
27 
Arriaga P., M. C. Indice Internacional de Rugosidad, Aplicación en la 
Red Carretera de México. Publicación Técnica No. 108, Instituto 
Mexicano 
del 
Transporte, 
Secretaría 
de 
Comunicaciones 
y 
Transportes, Sanfandila, Qro., 1998.  
28 
National Transportation Statistics 1999. Bureau of Transportation 
Statistics, 
US 
Department 
of 
Transportation 
(http://206.4.84.245/btsproducts/category.cfm?Category=102).  
29 
Transportation 
Statistics 
Report 
1999. 
Transport 
Canada. 
(http://www.tc.gc.ca/en/menu.htm).  
30 
Rico R., Alfonso., A. Mendoza D. y M. Mayoral G. Una Aproximación 
a la Definición de los Principales Corredores de Transporte Terrestre 
en México. Documento Técnico No. 94, Instituto Mexicano del 
Transporte, Secretaría de Comunicaciones y Transportes, Sanfandila, 
Qro., 2000.  
 


<!-- page 77 -->

Análisis de Costos de Operación Vehicular del Autotransporte de Carga por la Red 
Carretera Federal 
65 
31 
Larson, Richard C. y Amedeo R. Odón. Investigación de Operaciones 
Urbana (en Inglés). Instituto Tecnológico de Massachussetts. 
Prentice Hall, Inc., 1981.  
32 
Modernización del Sistema Carretero Troncal. Secretaría de 
Comunicaciones y Transportes, México, D.F., 1998. 
33 
Uribe M., Aristóteles, Francisco L. Quintero P., Alberto Mendoza D., 
Claudia Z. Gil A., y Jesús M. Cavaría V. Sistema para la 
Administración de la Información de Accidentes en Carreteras 
Federales (SAIACF). Documento Técnico No. 138, Instituto Mexicano 
del Transporte, Secretaría de Comunicaciones y Transportes, 
Sanfandila, Qro., 2000.  
 


<!-- page 78 -->

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
CIUDAD DE MEXICO 
SANFANDILA 
 
 
Av. Patriotismo 683 
Km. 12+000, Carretera 
Col. Mixcoac 
Querétaro-Galindo 
03730, México, D. F. 
76700, Sanfandila, Qro. 
Tel  (55)  56 15 35 75 
Tel  (442)   2 16 97 77 
Tel. (55)  55 98 52 18 
Tel. (442)   2 16 96 46 
Fax (55)  55 98 64 57 
Fax (442)   2 16 96 71 
 
 
 
 
Internet:  http://www.imt.mx 
 
 
publicaciones@imt.mx 
 
 
