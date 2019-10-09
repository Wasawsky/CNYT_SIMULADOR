# Simulador MARBLES
# Sistema con marbles y doble rendija

El sistema consiste en determinar la probabilidad de que una particula este en una posicion
El simulador permite especificar como vamos a operar y lo hacemos sobre

- Los experimentos de la canicas con coeficiente booleanos.
- Los Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas con coeficientes fraccionales
- El Experimento de las múltiples rendijas cuántico con coeficientes complejos.

# Generalidades

Calculando podemos determinar las posibilidades de que una particula entre en una rendija. Es posible teniendo la configuracion del sistema y el estado inicial de el sistema.

## Como usar

Esta libreria esta programada en la version de Python 3.7.4 y funciona para las versiones 3.7.* 
Debe tener instalado un entorno de desarrollo o un editor de texto donde se pueda compilar el archivo.

Si no posee uno puede ingresar a https://www.python.org/ para descargar la ultima version.


Despues de tenerlo, puede crear un archivo .py en el mismo directorio del archivo Simulador.py

Importe la libreria en el nuevo archivo y use las operaciones de manera directa
Por ejemplo el siguiente codigo le indicara el sistema, el estado inicial y el numero de cliks que tiene que hacer el sistema

`import Simulador_Sistema_Cuantico`

`a=Simulador.simuladorBool([[0, 1, 0, 0, 0, 1],
                           [0, 0, 0, 1, 0, 0],
                           [0, 0, 1, 0, 0, 0],
                           [1, 0, 0, 0, 1, 0]],
                           1,
                           [6, 2, 1, 5, 3, 10])`

`print(a)`

Producira un resultado:

`[[12], [5], [1], [9]]`

En caso de que tenga problemas puede ejecutar el archivo Pruebas_Simulador.py para ejecutar las pruebas establecidas.
En el repositorio existe un archivo Entradas_Manuales en las que puede ver codigo que le puede ayudar a hacer lectura de datos para el simulador por teclado; tambien esta el archivo Casos_Prueba si desea usar el archivo de Entradas_Manuales para probar casos de prueba.

### Como usarlo por consola?

Si desea usarlo por consola, ubique la consola en la carpeta donde esta el archivo Simulador_Sistema_Cuantico.py y escriba en la consola

        $ py Simulador.py

Para ejecutar las pruebas escriba en la consola

        $ py Pruebas_Simulador.py
        
Puede ejecutar el idle de python si escribe

        $ py

Estando en el directorio puede ejecutar 

        import Simulador
        Simulador.simuladorBool([[0, 1, 0, 0, 0, 1],
                                 [0, 0, 0, 1, 0, 0],
                                 [0, 0, 1, 0, 0, 0],
                                 [1, 0, 0, 0, 1, 0]],
                                 1,
                                 [6, 2, 1, 5, 3, 10])
 
Y el resultado sera:

        [[12], [5], [1], [9]]

## FUNCIONALIDADES:

- Permite experimentar con las canicas con coeficiente booleanos
- Permite calcular Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
- Permite determinar las posiciones para usar segun el Experimento de las múltiples rendijas cuántico.


## BIBLIOGRAFIA:


        > Quantum Computing For Computer Scientists 
        Noson S. Yanofsky 
        Mirco A. Mannucci
    
Para mas proyectos, Sigueme y encuentra mis repositorios de computacion cuantica
# Buscar mas ...
CALCULADORA DE NUMEROS COMPLEJOS 
https://github.com/Wasawsky/CNYT_COMPLEJOS.git


*Por: Michael Ballesteros*
