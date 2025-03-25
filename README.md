# Python-IA-Excel-Analisis
https://automatetheboringstuff.com/#toc
Test
 script.py
📂 Introduce la ruta del archivo Excel: H:\Sistema Account\Uso contable\Exportaciones\Exportaciones Ventas Detalladas.xlsx

📊 RESUMEN DE LOS DATOS 📊

🔹 Columnas: ['T.Fact.', 'Pto.Vta', 'Nº Factura', 'Fecha', 'Día', 'Mes', 'Año', 'Especie', '  kilos', 'Destino', 'Moneda', 'Precio x K.', 'Cotización', 'Tot. Fact. U$$', 'Tot. Fact. $', 'P.EMBARQUE', 'Transporte', 'Booking', 
'CLIENTE', 'T. U$S', 'T. Pesos']

🔹 Tipos de datos:
 T.Fact.                   object
Pto.Vta                  float64
Nº Factura               float64
Fecha             datetime64[ns]
Día                      float64
Mes                       object
Año                       object
Especie                   object
  kilos                  float64
Destino                   object
Moneda                    object
Precio x K.              float64
Cotización               float64
Tot. Fact. U$$           float64
Tot. Fact. $             float64
P.EMBARQUE                object
Transporte                object
Booking                   object
CLIENTE                   object
T. U$S                   float64
T. Pesos                  object
dtype: object

🔹 Valores nulos por columna:
 T.Fact.              0
Pto.Vta              2
Nº Factura          20
Fecha               20
Día                 20
Mes                 20
Año                 20
Especie             20
  kilos             20
Destino             20
Moneda              20
Precio x K.         20
Cotización          33
Tot. Fact. U$$       0
Tot. Fact. $         0
P.EMBARQUE         527
Transporte         978
Booking           3861
CLIENTE             20
T. U$S            7725
T. Pesos          7678
dtype: int64

📈 ESTADÍSTICAS CLAVE 📈

🔤 Columna categórica: T.Fact.
T.Fact.
FCE    8737
NCE     519
NC       24
NDE      15
Name: count, dtype: int64

🔢 Columna numérica: Pto.Vta
   • Media: 7.01
   • Mediana: 7.00
   • Moda: 7.00
   • Desviación estándar: 0.19

🔢 Columna numérica: Nº Factura
   • Media: 1803.28
   • Mediana: 1810.00
   • Moda: 931.00
   • Desviación estándar: 1013.85

🔤 Columna categórica: Fecha
Fecha
2015-02-27    81
2015-01-12    79
2017-06-02    74
2014-11-14    63
2015-11-28    52
2015-08-14    46
2015-02-28    44
2014-05-24    42
2014-08-26    41
2017-11-14    40
Name: count, dtype: int64


🔢 Columna numérica: Día
   • Media: 15.61
   • Mediana: 16.00
   • Moda: 18.00
   • Desviación estándar: 8.66

🔤 Columna categórica: Mes
Mes
febrero       939
noviembre     872
marzo         860
enero         826
agosto        789
septiembre    776
diciembre     750
junio         737
abril         719
julio         701
Name: count, dtype: int64

🔤 Columna categórica: Año
Año
2015    1058
2017     823
2018     805
2016     802
2019     771
2020     770
2021     769
2022     699
2014     693
2023     530
Name: count, dtype: int64

🔤 Columna categórica: Especie
Especie
Sábalo Entero             2351
Pejerrey Entero            731
Flete                      337
Langostino Pelado          302
Carpa Entera               279
Anillas de Calamar         266
Tentáculos de Calamar      199
Filet de Merluza           171
Filet de Salmón Rosado     163
FLETE                      153
Name: count, dtype: int64

🔢 Columna numérica:   kilos
   • Media: 7639.48
   • Mediana: 300.00
   • Moda: 28000.00
   • Desviación estándar: 11772.07

🔤 Columna categórica: Destino
Destino
Bolivia         5307
Colombia        1624
T. del Fuego     855
Brasil           360
Rusia            219
Paraguay         157
Camerun          123
Uruguay          122
Rumania           98
Israel            97
Name: count, dtype: int64

🔤 Columna categórica: Moneda
Moneda
Dólar    8423
Pesos     850
Euro        2
Name: count, dtype: int64

🔢 Columna numérica: Precio x K.
   • Media: 237.05
   • Mediana: 1.40
   • Moda: 1.20
   • Desviación estándar: 1065.14

🔢 Columna numérica: Cotización
   • Media: 82.43
   • Mediana: 17.31
   • Moda: 1.00
   • Desviación estándar: 188.58

🔢 Columna numérica: Tot. Fact. U$$
   • Media: 9115.72
   • Mediana: 1680.00
   • Moda: 0.00
   • Desviación estándar: 14634.66

🔢 Columna numérica: Tot. Fact. $
   • Media: 875647.05
   • Mediana: 65000.00
   • Moda: 0.00
   • Desviación estándar: 3642904.42

🔤 Columna categórica: P.EMBARQUE
P.EMBARQUE
FLETE               471
T. del Fuego        441
TIERRA DEL FUEGO    415
15020EC01000125S    114
17020EC01000418C     72
14020EC01000856F     72
14020EC01000744B     60
15020EC01000789L     50
15020EC01000559G     43
14020EC01000353U     39
Name: count, dtype: int64

🔤 Columna categórica: Transporte
Transporte
CRT              5815
T. del Fuego      436
FLETE             109
CRT                21
HLBU 901031-8      15
MSWU 1016498       14
TRIU 875184-4      12
FSCU 567312-7       9
MMAU 102172-2       9
ZCSU5107558         9
Name: count, dtype: int64

🔤 Columna categórica: Booking
Booking
CRT             3502
T. del Fuego     436
FLETE            110
CRT               22
BUA0258467        18
69458840          15
914570945         15
60483366          12
203994928         10
BUA0323031         9
Name: count, dtype: int64




🔤 Columna categórica: CLIENTE
CLIENTE
EL PEJERREY         4375
IMPORMAR            1495
LABRIOLA VIVIANA     388
SERVICIO COMPASS     375
DUNTOWER             310
ERICK BASCOPE        253
ALAOR CREMONESE      242
FRIGOPACU            234
VALFEMAR             222
EL MUTURU            219
Name: count, dtype: int64

🔢 Columna numérica: T. U$S
   • Media: 23923.06
   • Mediana: 22400.00
   • Moda: 2040.00
   • Desviación estándar: 33458.06

🔤 Columna categórica: T. Pesos
T. Pesos
1962310      4
24519693     3
2548000      3
3859056      3
714000       3
1820320.0    3
49768600     3
2581280      3
3583107      3
21934800     3
Name: count, dtype: int64

🤖 ANÁLISIS DE OPENAI 🤖
Basándonos en los primeros valores de cada columna de datos de ventas proporcionados:

1. **Producto y Venta**: Se observa que se trata de ventas del producto "Sábalo Entero" con un precio unitario de 1 dólar por kilo.
2. **Destino y Moneda**: Todas las ventas se realizaron a Colombia y en dólares.
3. **Fecha y Tiempo**: Las ventas se distribuyen en agosto de 2010, con facturas emitidas en los días 2 y 5 del mes.
4. **Cantidad y Monto**: Se vendieron 24,500 kilos de Sábalo Entero en cada factura, generando un total de 24,500 dólares por factura.
5. **Tipo de Pago**: Se observa que algunos clientes realizaron pagos en dólares y otros en pesos argentinos.
6. **Transporte y Embarque**: El transporte fue realizado por la empresa CRT y el tipo de embarque fue "FLETE".
7. **Cliente y Booking**: Todas las ventas fueron realizadas al cliente IMPORMAR y se utilizó el Booking CRT.

En resumen, se puede concluir que las ventas de Sábalo Entero a Colombia en agosto de 2010 fueron consistentes en términos de cantidad, destino y precio, con variaciones en la forma de pago entre dólares y pesos argentinos
