# Homicidios por siniestros viales en la Ciudad Autónoma de Buenos Aires, Argentina

## Introducción

En este proyecto se simula el rol de un Data Analyst que forma parte del equipo de analistas de datos de una empresa consultora a la cual el **Observatorio de Movilidad y Seguridad Vial (OMSV)** les solicitó la elaboración de un proyecto de análisis de datos. 

Tiene como finalidad poder presentar un analisis en un dashboard que sea util para poder implementar acciones para la disminucion general de accidentes, y poder verificar su efectividad en funcion a los KPIs realizados.
Tambien, se solicita ciertas recomendaciones en funcion al analisis realizado.

## Contexto

Los siniestros viales, también conocidos como accidentes de tráfico o accidentes de tránsito, son eventos que involucran vehículos en las vías públicas y que pueden tener diversas causas, como colisiones entre automóviles, motocicletas, bicicletas o peatones, atropellos, choques con objetos fijos o caídas de vehículos. Estos incidentes pueden tener consecuencias que van desde daños materiales hasta lesiones graves o fatales para los involucrados.

En el contexto de una ciudad como Buenos Aires, los siniestros viales pueden ser una preocupación importante debido al alto volumen de tráfico y la densidad poblacional. Estos incidentes pueden tener un impacto significativo en la seguridad de los residentes y visitantes de la ciudad, así como en la infraestructura vial y los servicios de emergencia.

Las tasas de mortalidad relacionadas con siniestros viales suelen ser un indicador crítico de la seguridad vial en una región. Estas tasas se calculan, generalmente, como el número de muertes por cada cierto número de habitantes o por cada cierta cantidad de vehículos registrados. Reducir estas tasas es un objetivo clave para mejorar la seguridad vial y proteger la vida de las personas en la ciudad.

Es importante destacar que la prevención de siniestros viales involucra medidas como la educación vial, el cumplimiento de las normas de tráfico, la infraestructura segura de carreteras y calles, así como la promoción de vehículos más seguros. El seguimiento de las estadísticas y la implementación de políticas efectivas son esenciales para abordar este problema de manera adecuada.

## Datos

Para este proyecto se trabajó con la **Bases de Víctimas Fatales en Siniestros Viales** que se encuentra en formato de Excel y contiene dos pestañas de datos:

* **HECHOS**: que contiene una fila de hecho con id único y las variables temporales, espaciales y participantes asociadas al mismo.
* **VICTIMAS**: contiene una fila por cada víctima de los hechos y las variables edad, sexo y modo de desplazamiento asociadas a cada víctima. Se vincula a los HECHOS mediante el id del hecho.

En este [documento](Material_Complementario/NOTAS_HOMICIDIOS_SINIESTRO_VIAL.pdf) se detallan todas las definiciones manejadas en los datos y en el desarrollo de este proyecto. Por otra parte, en este [link](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales) se encuentran los datos utilizados en el análisis.

## ETL y EDA

En primer lugar, se realizó un proceso de extracción, transformación y carga de los datos (ETL), tanto de "HECHOS" como "VÍCTIMAS", donde se estandarizaron nombres de las variables, se analizaron nulos y duplicados de los registros, se eliminaron columnas redundantes o con muchos valores faltantes, entre otras tareas. Una vez finalizado este proceso para los dos conjuntos de datos de "Homicidios" se procedió a unir los dos conjuntos en uno solo denominado `df`.

En segundo lugar, se procedió a realizar un análisis exploratorio exahustivo (EDA), con la finalidad de encontrar patrones que permitan generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales. Todos los detalles de este análisis se encuentran [aquí](01_EDA.ipynb).

## Análisis de los Datos

### Analisis Temporal

Dentro del análisis temporal, se abordo el estudio de la distribucion de los años, meses, dias y franjas horarias de los accidentes.

Dando como resultados mas significativos que el mes de Diciembre es el mas afectado por accidentes, asi como los fines de semana no tienen una variacion significativa, pero si lo tienen las franjas horarias, siendo la mañana la franja horaria con mayor cantidad de accidentes.

### Analisis de accidente y partes involucradas

En este apartado se logro investigar con exito que los accidentes tienen como victimas principalmente a los conductores de motos y a los peatones, y como principales acusados a los autos y pasajeros de transporte publico. Tambien se puede ver que los hombres tieen mayores probabilidades de tener accidentes, asi como las personas de rango etario de entre 16 y 35 años.

### Analisis Geografico

Siguiendo con el analisis, podemos verificar que existe una correlacion significativa entre los lugares de los accidentes, siendo mayormente localizados en cruces de avenidas.

## KPI

En función de lo analizado en el punto anterior, se plantearon tres objetivos en relación a la disminución de la cantidad de víctimas fatales de los siniestros viales, desde los cuales se proponen tres indicadores de rendimiento clave o KPI.

* *Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior*

    Las tasas de mortalidad relacionadas con siniestros viales suelen ser un indicador crítico de la seguridad vial en una región. Se define como **Tasa de homicidios en siniestros viales** al número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico, en este caso se toman 6 meses. Su fórmula es:

    $\text{Tasa de homicidios en siniestros viales} = \frac{\text{Número de homicidios en siniestros viales}}{\text{Población total}}·100,000$

    Como *Población Total* se calculó la población para el año 2021 a partir de los censos poblacionales del año 2010 y 2022.

    En este caso, para el año 2021, la *Tasa de homicidios en siniestros viales* fue de 1.77 lo que significa que, durante los primeros 6 meses del año 2021, hubo aproximadamente 1.77 homicidios en accidentes de tránsito por cada 100,000 habitantes. Ahora, el objetivo planteado es reducir esta tasa para el siguiente semestre de 2021 en un 10%, esto es **1.61**. Cuando se calcula el KPI para este período se obtiene que la *Tasa de homicidios en siniestros viales* fue de **1.36**, lo que significa que para el segundo semestre de 2021 se cumple con el objetivo propuesto.

* *Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior*

    Como se vio en el análisis exploratorio, el 42% de las víctimas mortales se transportaban en moto al momento del hecho. Por lo que se consideró importante proponer el monitoreo de la cantidad de accidentes mortales en este tipo de conductor. Para ello se define a la **Cantidad de accidentes mortales de motociclistas** como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado periodo temporal. La fórmula para medir la evolución de los accidentes mortales con víctimas en moto es:

    $\text{Cantidad de accidentes mortales de motociclistas} = -\frac{\text{Víctimas moto año anterior - Víctimas moto año actual}}{\text{Víctimas moto año anterior}}·100$

    Donde:
    - $\text{Víctimas moto año anterior}$: Número de accidentes mortales con víctimas en moto en el año anterior
    - $\text{Víctimas moto año actual}$: Número de accidentes mortales con víctimas en moto en el año actual 

    Para este caso, se toma como año actual al año 2021 y como año anterior al año 2020. En primer lugar, se calculó la *Cantidad de accidentes mortales de motociclistas* para el año 2020, el cual resultó de 27, de esta manera el objetivo a cumplir es de **25** (es decir, la reducción del 7% de la cantidad de accidentes para 2020). El calcular la *Cantidad de accidentes mortales de motociclistas* para el año 2021 resultó de **46** lo que significa que aumentó un 70% la cantidad de muertes de conductores de motociclistas respecto del 2021.

* *Reducir en un 5% la cantidad de victimas del rango etario 16 a 35 años en el último año, en CABA, respecto al año anterior*

    Como se vio en el análisis exploratorio, el 45% de las víctimas mortales son del rango etario entre 16 y 35 años. Se define a la **Cantidad de accidentes mortales de rango etario 16 a 35** al número de víctimas fatales en accidentes de tránsito con edades entre 16 y 35 años. Su fórmula es:

    $\text{Cantidad de accidentes mortales de rango etario 16 a 35} = \frac{\text{Víctimas 16 a 35 años año anterior - Víctimas 16 a 35 años año actual}}{\text{Victimas rango etario año anterior}}·100$

    En primer lugar se calculó la *Cantidad de victimas de 16 a 35 años* para el año 2020, la cual resultó en 27. De esta se pudo determinar el objetivo a cumplir al año siguiente, que resultó en **26** (es decir, la reducción del 5%). Finalmente, al calcular la *Cantidad de victimas de 16 a 35 años* para el año 2021, la misma resultó de 42, lo que significa que se superó el objetivo, aumentando con respecto al año anterior.


## Conclusiones y recomendaciones

Entre los años 2016 a 2021 se registraron 717 víctimas fatales en accidentes de tránsito. 

El 70% ocurrio en dias de semana, siendo una distribucion equitativa en todos los dias.

El 17% entre las 5 y 8 de la mañana, siendo esta franja horaria la mas frecuente en ocurrir accidentes.

Diciembre es el mes con mas víctimas.

El 45% de las victimas entre 16 y 35 años de edad.

El 42% son conductores de motos.

El 62% de las víctimas ocurren en avenidas y el 55% del total general en cruce de avenidas.

### Objetivos 

Se cumplió con el objetivo de bajar la tasa de homicidios en el segundo semestre 2021.

No se cumplió con el objetivo de bajar la cantidad de accidentes de motos en el 2021.

No se cumplió con el objetivo de bajar la cantidad de accidentes del rango etario 16 a 35 en el 2021.


En función de lo anterior, se hacen las siguientes recomendaciones:

* Continuar monitoreando los objetivos propuestos acompañados de campañas puntuales, en especial a conductores de motos y usuarios de las avenidas.
* Reforzar las campañas de seguridad vial entre los días viernes a lunes, intensificando particularmente en el mes de Diciembre.
* Puntualizar campañas de conducción segura en avenidas y cruces de calles.
* Realizar controles para asegurar los elementos de seguridad en las motos.
* Dirigir las campañas de seguridad hacia el sexo masculino, especialmente en cuanto a conducción en moto, para un rango etario entre los 16 a 35 años.
* Realizar actos de concientizacion orientados a publico de 16 a 35 años de edad.