# Playground y Cheatsheet para aprender Python

[![Build Status](https://travis-ci.org/trekhleb/learn-python.svg?branch=master)](https://travis-ci.org/trekhleb/learn-python)

> Esta es una colección de scripts de Python divididos en [categorías](#contenido) que contienen
ejemplos de código con sus explicaciones, diferentes usos y links a recursos adicionales.

> _Lee esto en:_ [_Inglés_](README.md), [_Portugués_](README.pt-BR.md), [_Traditional Chinese_](README.zh-TW.md), [_Українська_](README.uk-UA.md).

Es un **playground** ya que puedes cambiar o añadir cosas al código para ver
cómo funciona y [probarlo](#probando-el-código) usando aserciones. También puedes
[revisar el código](#revisando-el-código) que has escrito y averiguar si está acorde con
la guía de estilos de Python. Todo esto, en conjunto, puede hacer que tu proceso de aprendizaje
sea más interactivo y puede ayudarte a mantener la calidad del código muy alta desde el principio.

Es un **cheatsheet** porque puedes regresar y revisar los ejemplos de código para
fortalecer tus conocimientos sobre las [sentencias y contrucciones estándar de Python](#contenido).
Además, ya que el código tiene muchas aserciones, podrás ver el resultado de las funciones/sentencias en el mismo
código sin la necesidad de ejecutarlos.

> _También puede interesarte 🤖 [Interactive Machine Learning Experiments](https://github.com/trekhleb/machine-learning-experiments)_

## Cómo usar este repositorio

Cada script de Python en este repositorio sigue la estructura:

```python
"""Lists  <--- Nombre del tema

# @see: https://www.learnpython.org/en/Lists  <-- Link a recurso adicional

Aquí puede haber una explicación detallada del tema en concreto (ej: información general sobre listas).
"""


def test_list_type():
    """Explicación del sub-tema.
    
    Cada archivo contiene funciones de prueba que muestran sub-temas (ej: tipos de listas, métodos en listas).
    """
    
    # Este es un ejemplo de cómo construir una lista. <-- Estos comentarios explican el procedimiento
    squares = [1, 4, 9, 16, 25]
    
    # Las listas pueden ser indexadas y cortadas. 
    # Al indexar devuelve el item.
    assert squares[0] == 1  # <-- Estas aserciones muestran el resultado.
    # Al cortar devuelve una nueva lista.
    assert squares[-3:] == [9, 16, 25]  # <-- Estas aserciones muestran el resultado.
```

Normalmente, querrás hacer lo siguiente:

- [Encontrar el tema](#contenido) que quieres aprender o revisar.
- Leer los comentarios y/o la documentación que está escrita en cada docstring del script (toma como ejemplo el script de arriba).
- Ver los ejemplos de código y las aserciones para conocer diferentes maneras de usar el código y entender el resultado previsto.
- Cambiar el código o añadir nuevas aserciones para ver cómo funcionan las cosas.
- [Probar](#probando-el-código) y [revisar](#revisando-el-código) el código para ver si funciona y si está escrito
correctamente.

## Contenido

1. **Empezando**
    - [¿Qué es Python?](src/getting_started/what_is_python.md)
    - [Sintaxis de Python](src/getting_started/python_syntax.md)
    - [Variables](src/getting_started/test_variables.py)
2. **Operadores**
    - [Operadores aritméticos](src/operators/test_arithmetic.py) (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
    - [Operadores Bitwise](src/operators/test_bitwise.py) (`&`, `|`, `^`, `>>`, `<<`, `~`)
    - [Operadores de atribución](src/operators/test_assigment.py) (`=`, `+=`, `-=`, `/=`, `//=` etc.)
    - [Operadores de comparación](src/operators/test_comparison.py) (`==`, `!=`, `>`, `<`, `>=`, `<=`)
    - [Operadores lógicos](src/operators/test_logical.py) (`and`, `or`, `not`)
    - [Operadores de identidad](src/operators/test_identity.py) (`is`, `is not`)
    - [Operadores de asociación](src/operators/test_membership.py) (`in`, `not in`)
3. **Tipos de datos**
    - [Números](src/data_types/test_numbers.py) (incluyendo booleans)
    - [Strings](src/data_types/test_strings.py) y sus métodos
    - [Listas](src/data_types/test_lists.py) y sus métodos (incluyendo comprensión de listas)
    - [Tuples](src/data_types/test_tuples.py)
    - [Sets](src/data_types/test_sets.py) y sus métodos
    - [Diccionarios](src/data_types/test_dictionaries.py)
    - [Tipo de casting](src/data_types/test_type_casting.py)
4. **Control de flujo**
    - [La sentencia `if`](src/control_flow/test_if.py)
    - [La sentencia `for`](src/control_flow/test_for.py) (y la función `range()`)
    - [La sentencia `while`](src/control_flow/test_while.py)
    - [La sentencia `try`](src/control_flow/test_try.py)
    - [La sentencia `break`](src/control_flow/test_break.py)
    - [La sentencia `continue`](src/control_flow/test_continue.py)
5. **Funciones**
    - [Definición de función](src/functions/test_function_definition.py) (sentencias `def` y `return`)
    - [Ámbito de variables dentro de funciones](src/functions/test_function_scopes.py) (sentencias `global` y `nonlocal`)
    - [Valores de argumento predeterminados](src/functions/test_function_default_arguments.py)
    - [Argumentos de palabras clave](src/functions/test_function_keyword_arguments.py)
    - [Listas de argumento arbitrario](src/functions/test_function_arbitrary_arguments.py)
    - [Listas de argumentos en funciones](src/functions/test_function_unpacking_arguments.py) (sentencias `*` y `**`)
    - [Expresiones Lambda](src/functions/test_lambda_expressions.py) (sentencia `lambda`)
    - [Strings de documentación](src/functions/test_function_documentation_string.py)
    - [Anotaciones en funciones](src/functions/test_function_annotations.py)
    - [Decoradores de funciones](src/functions/test_function_decorators.py)
6. **Clases**
    - [Definición de clase](src/classes/test_class_definition.py) (sentencia `class`)
    - [Objetos de clase](src/classes/test_class_objects.py)
    - [Objetos de instancia](src/classes/test_instance_objects.py)
    - [Métodos de objetos](src/classes/test_method_objects.py)
    - [Variables de clase y de instancia](src/classes/test_class_and_instance_variables.py)
    - [Herencia](src/classes/test_inheritance.py)
    - [Herencia múltiple](src/classes/test_multiple_inheritance.py)
7. **Módulos**
    - [Módulos](src/modules/test_modules.py) (sentencia `import`)
    - [Paquetes](src/modules/test_packages.py)
8. **Errores y excepciones**
    - [Controlando excepciones](src/exceptions/test_handle_exceptions.py) (sentencia `try`)
    - [Generando excepciones](src/exceptions/test_raise_exceptions.py) (sentencia `raise`) 
9. **Archivos**
    - [Leyendo y escribiendo](src/files/test_file_reading.py) (sentencia `with`)
    - [Métodos de objetos de archivo](src/files/test_file_methods.py)
10. **Adicionales**
    - [La sentencia `pass`](src/additions/test_pass.py)
    - [Generadores](src/additions/test_generators.py) (sentencia `yield`)
11. **Pequeño tour de las librerías estándar**
    - [Serialización](src/standard_libraries/test_json.py) (librería `json`)
    - [Parámetros en archivos](src/standard_libraries/test_glob.py) (librería `glob`)
    - [Expresiones regulares](src/standard_libraries/test_re.py) (librearía `re`)
    - [Matemática](src/standard_libraries/test_math.py) (librerías `math`, `random` y `statistics`)
    - [Fechas y horas](src/standard_libraries/test_datetime.py) (librería `datetime`)
    - [Compresión de datos](src/standard_libraries/test_zlib.py) (librearía `zlib`)

## Pre-requisitos

**Instalando Python**

Asegúrate de que tienes [Python3 instalado](https://realpython.com/installing-python/) en tu sistema.

Podrías utilizar la librería estándar [venv](https://docs.python.org/es/3/library/venv.html) para crear
entornos virtuales y tener Python, pip y todos los paquetes instalados en el directorio de tu
proyecto local para evitar cometer errores con paquetes del sistema y sus versiones.

Dependiendo de la instalación, tendrás acceso a Python3 ejecutando `python` o `python3`. Lo mismo
aplica para el administrador de paquetes pip - puedes tener acceso a él ejecutando `pip` o `pip3`.

Puedes ver tu versión actual de Python ejecutando:

```bash
python --version
```

Ten en cuenta que cuando leas `python` en este repositorio, se asume que es Python **3**.

**Instalando dependencias**

Instala todas las depencias requeridas para el proyecto ejecutando:

```bash
pip install -r requirements.txt
```

## Probando el código

Las pruebas son hechas usando el framework [pytest](https://docs.pytest.org/en/latest/).

Puedes añadir más pruebas por ti mismo añadiendo archivos y funciones con el prefijo `test_`
(ej: `test_topic.py` con la función `def test_sub_topic()` adentro).

Para ejecutar todas las pruebas, por favor escribe el siguiente comando desde el directorio
raíz del proyecto:

```bash
pytest
```

Para ejecutar diferentes pruebas escribe:

```bash
pytest ./path/to/the/test_file.py
```

## Revisando el código

La revisión del código está hecha usando las librerías [pylint](http://pylint.pycqa.org/) y [flake8](http://flake8.pycqa.org/en/latest/).

### PyLint

Para revisar si el código sigue la guía de estilos
[PEP 8](https://www.python.org/dev/peps/pep-0008/), por favor ejecuta:

```bash
pylint ./src/
```

En caso de que linter detecte un error (ej: `missing-docstring`), te recomiendo leer más sobre
el error concreto ejecutando:

```bash
pylint --help-msg=missing-docstring
```

[Más sobre PyLint](http://pylint.pycqa.org/)

### Flake8

Para revisar si el código sigue la guía de estilos
[PEP 8](https://www.python.org/dev/peps/pep-0008/), por favor ejecuta:

```bash
flake8 ./src
```

O, si quieres ver un output más detallado, ejecuta:

```bash
flake8 ./src --statistics --show-source --count
```

[Más sobre Flake8](http://flake8.pycqa.org/en/latest/)

## Apoya al proyecto

Puedes apoyar al proyecto a través de ❤️️ [GitHub](https://github.com/sponsors/trekhleb) o ❤️️ [Patreon](https://www.patreon.com/trekhleb).
