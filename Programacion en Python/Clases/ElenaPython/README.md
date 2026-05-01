
Estado de ejecución de las pruebas (*unittest*) por GitLab CI/CD:

[![pipeline status](/../badges/master/pipeline.svg)](/commits/master)

# Banco Orientado a Objetivos (aka "POO")

Se pretende simular un banco.
Donde una persona puede abrir varias cuentas, recibir el salario, pagar los recibos. Además, el banco puede abonar unos intereses asociados una cuenta.

Datos de entrada:

* El programa `banco.py` podrá leer las ordenes por la entrada estándar (usando método `input`), desde un fichero. Tambien, implementará una clase `Banco` con un método  `ejecutar_orden(orden)` que recibirá como argumento `orden` a ejecutar.

    Lectura de ordenes desde entrada estándar.
    No se permite implementación de menus interactivos, la entrada estandar debe aceptar los mismos comandos que el resto de metodos de entrada de datos (p.e. fichero).
    La entrada de datos por la entrada estandar se indica mediante el argumento `-` en la primera posición de argumentos que recibe el programa.

    ```
    python3 ./banco.py -
    ```

    Lectura de ordenes desde un fichero. 
    El fichero puede contener lineas en blanco, tabuladors en vez de espacio, varios espacios entre argumentos de una orden.
    El nombre del fichero se indica en la primera posición de argumentos que recibe el programa.

    ```
    python3 ./banco.py ordenes.txt
    ```

    Uso de la funcion `main` desde otro modulo, ha de tener el mismo efecto que ejecución desde la linea de comandos.

    ``` 
    import banco

    argv = ['banco.py', './test_ordenes.txt']
    banco.main(argv)
    ```

    Uso del programa desde otro modulo:

    ```
    import banco

    mi_banco = banco.Banco()
    mi_banco.ejecutar_orden("crear Cliente1 100000U CC1000000001 700")
    ```

* Una `persona`, que se caracteriza por un DNI y un `listado de cuentas` bancarias, puede tener asociada hasta 3 cuentas bancarias.
Dichas operaciones no devuelven ningún resultado. Se podrá devolver mensajes de error, i.e., si la tupla de (DNI, cuenta) ya existe.

    Ejemplo de cargar datos:
    ```
    crear <nombre> <dni> <codigo_cuenta> <valor> <interes>
    crear Cliente1 123123X CC0987654321 700 3
    crear Cliente1 123123X CC0987654322 100 1
    crear Cliente1 123123X CC0987654323 0 3
    ```

* Una `cuenta` se caracteriza por tener asociado un *número de cuenta* representado por cadena de texto empezando por "CC", y *un saldo disponible* y *tipo de interés*.

* Se puede `consultar` el saldo disponible en cualquier momento. Se devolverá el saldo de la cuenta.

    ```
    consulta <codigo_cuenta>
    consulta CC0987654322
    100
    ```

* Se puede `ingresar` abonos, `pagar` recibos y realizar `transferencias` en cualquier momento. Dichas operaciones no devuelven ningún resultado. Se podrá devolver mensajes de error, i.e., si la cuenta no existe o el valor es menor que 0.

    ```
    ingreso <codigo_cuenta> <valor>
    ingreso CC0987654321 1100

    pago <codigo_cuenta> <valor>
    pago CC0987654322 750

    pago XX1111 1
    ERROR: Cuenta XX1111 no existe!

    transferencia <codigo_cuenta_emisora> <codigo_cuenta_receptora> <valor>
    transferencia CC0987654321 CC0987654322 750
    ```

* Se puede comprobar si `hay mora`, i.e., si tienen alguna cuenta con saldo negativo. Se devolverá `sihaymora` en caso si hay mora o `nohaymora` si no la hay.

    ````
    haymora <dni>
    haymora 123123X
    sihaymora
    ```

* Se pueden abonar los intereses a una cuenta, esta operación cambia el saldo de la cuenta. Dicha operación no devuelven ningún resultado. Se podrá devolver mensajes de error, i.e., si la cuenta no existe.

    ```
    intereses CC0987654322
    ```

* Complemente el fichero de pruebas unitarias `test_banco.py` para asegurar el buen funcionamiento del programa.

    ```
    python3 ./test_banco.py
    ```

A continuación, se describe un caso de uso.
Crear una persona con un DNI cualquiera, así como dos cuentas, una sin saldo inicial y otra con 700 euros.
La persona recibe la nómina mensual, por lo que ingresa 1100 euros en la primera cuenta, pero tiene que pagar el alquiler de 750 euros con la segunda.
Consulta si hay mora.
Posteriormente hacer una transferencia de una cuenta a otra y comprobar mostrándolo por pantalla que cambia el estado de la persona.
Banco abonara los intereses en la primera cuenta, consulte el saldo.
