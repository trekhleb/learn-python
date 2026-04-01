# Пісочниця та шпаргалка для вивчення Python

> 🇺🇦 УКРАЇНА [ЗАЗНАЄ ЗБРОЙНОЇ АГРЕСІЇ](https://war.ukraine.ua/) З БОКУ РОСІЙСЬКОЇ АРМІЇ. ГИНУТЬ МИРНІ ЖИТЕЛІ. ЖИТЛОВІ КВАРТАЛИ ЗАЗНАЮТЬ БОМБАРДУВАНЬ.
> - Допоможіть Україні:
>   - [Благодійний фонд Сергія Притули](https://prytulafoundation.org/en/)
>   - [Благодійний фонд «Повернись живим»](https://savelife.in.ua/donate/)
>   - [Національний банк України](https://bank.gov.ua/ua/news/all/natsionalniy-bank-vidkriv-spetsrahunok-dlya-zboru-koshtiv-na-potrebi-armiyi)
> - Більше інформації на [war.ukraine.ua](https://war.ukraine.ua/) та [МЗС України](https://twitter.com/MFA_Ukraine)

<hr/>

[![Build Status](https://travis-ci.org/trekhleb/learn-python.svg?branch=master)](https://travis-ci.org/trekhleb/learn-python)

> Це колекція скриптів мовою Python, розподілених за [темами](#зміст), що містять приклади коду з поясненнями, різними варіантами використання та посиланнями на додаткові матеріали.

> _Читати іншими мовами:_ [_English_](README.md), [_Português_](README.pt-BR.md), [_Español_](README.es-ES.md), [_繁體中文_](README.zh-TW.md).

Це **пісочниця**, тому що ви можете змінювати або доповнювати код, щоб побачити, як він працює, і [тестувати його](#тестування-коду) за допомогою тверджень. Також ви можете [перевіряти код](#перевірка-коду), який ви написали, і з'ясувати, чи відповідає він настановам зі стилю Python. Усе це може зробити процес навчання інтерактивнішим і допоможе підтримувати високу якість коду від самого початку.

Це **шпаргалка**, тому що ви можете повертатися до цих прикладів коду щоразу, коли захочете повторити синтаксис [стандартних інструкцій і конструкцій Python](#зміст). А оскільки код містить багато тверджень, ви зможете бачити очікуваний результат функцій та виразів одразу, без їх запуску.

> _Вас також може зацікавити 🤖 [Interactive Machine Learning Experiments](https://github.com/trekhleb/machine-learning-experiments)_

## Як користуватися цим репозиторієм

Кожен скрипт Python у цьому репозиторії має таку структуру:

```python
"""Lists  <--- Назва теми

# @see: https://www.learnpython.org/en/Lists  <-- Посилання на додаткові матеріали

Тут може бути детальніше пояснення поточної теми (наприклад, загальна інформація про списки).
"""


def test_list_type():
    """Пояснення підтеми.

    Кожен файл містить тестові функції, які ілюструють підтеми (наприклад, тип списку, методи списків).
    """

    # Ось приклад побудови списку.  <-- Коментарі пояснюють дію
    squares = [1, 4, 9, 16, 25]

    # Списки можна індексувати та зрізати (sliced).
    # Індексування повертає елемент.
    assert squares[0] == 1  # <-- Твердження ілюструють результат.
    # Зрізання повертає новий список.
    assert squares[-3:] == [9, 16, 25]  # <-- Твердження ілюструють результат.
```

Зазвичай ви можете зробити наступне:

- [Знайти тему](#зміст), яку хочете вивчити або повторити.
- Прочитати коментарі та/або документацію, на яку є посилання в docstring кожного скрипта (як у прикладі вище).
- Переглянути приклади коду та твердження, щоб побачити варіанти використання й очікуваний результат.
- Змінити код або додати нові твердження, щоб побачити, як усе працює.
- [Запустити тести](#тестування-коду) та [перевірити код](#перевірка-коду), щоб переконатися, що він працює і написаний правильно.

## Зміст

1. **Початок роботи**
    - [Що таке Python](src/getting_started/what_is_python.md)
    - [Синтаксис Python](src/getting_started/python_syntax.md)
    - [Змінні](src/getting_started/test_variables.py)
2. **Оператори**
    - [Арифметичні оператори](src/operators/test_arithmetic.py) (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
    - [Побітові оператори](src/operators/test_bitwise.py) (`&`, `|`, `^`, `>>`, `<<`, `~`)
    - [Оператори присвоєння](src/operators/test_assigment.py) (`=`, `+=`, `-=`, `/=`, `//=` тощо)
    - [Оператори порівняння](src/operators/test_comparison.py) (`==`, `!=`, `>`, `<`, `>=`, `<=`)
    - [Логічні оператори](src/operators/test_logical.py) (`and`, `or`, `not`)
    - [Оператори ідентичності](src/operators/test_identity.py) (`is`, `is not`)
    - [Оператори належності](src/operators/test_membership.py) (`in`, `not in`)
3. **Типи даних**
    - [Числа](src/data_types/test_numbers.py) (включно з булевими значеннями)
    - [Рядки](src/data_types/test_strings.py) та їхні методи
    - [Списки](src/data_types/test_lists.py) та їхні методи (включно з генераторами списків)
    - [Кортежі](src/data_types/test_tuples.py)
    - [Множини](src/data_types/test_sets.py) та їхні методи
    - [Словники](src/data_types/test_dictionaries.py)
    - [Перетворення типів](src/data_types/test_type_casting.py)
4. **Керування потоком виконання**
    - [Інструкція `if`](src/control_flow/test_if.py)
    - [Інструкція `for`](src/control_flow/test_for.py) (і функція `range()`)
    - [Інструкція `while`](src/control_flow/test_while.py)
    - [Інструкція `try`](src/control_flow/test_try.py)
    - [Інструкція `break`](src/control_flow/test_break.py)
    - [Інструкція `continue`](src/control_flow/test_continue.py)
5. **Функції**
    - [Визначення функції](src/functions/test_function_definition.py) (інструкції `def` і `return`)
    - [Області видимості змінних у функціях](src/functions/test_function_scopes.py) (інструкції `global` і `nonlocal`)
    - [Стандартні значення аргументів](src/functions/test_function_default_arguments.py)
    - [Іменовані аргументи](src/functions/test_function_keyword_arguments.py)
    - [Довільні списки аргументів](src/functions/test_function_arbitrary_arguments.py)
    - [Розпакування списків аргументів](src/functions/test_function_unpacking_arguments.py) (інструкції `*` і `**`)
    - [Лямбда-вирази](src/functions/test_lambda_expressions.py) (інструкція `lambda`)
    - [Рядки документації](src/functions/test_function_documentation_string.py)
    - [Анотації функцій](src/functions/test_function_annotations.py)
    - [Декоратори функцій](src/functions/test_function_decorators.py)
6. **Класи**
    - [Визначення класу](src/classes/test_class_definition.py) (інструкція `class`)
    - [Об'єкти класу](src/classes/test_class_objects.py)
    - [Об'єкти екземплярів](src/classes/test_instance_objects.py)
    - [Об'єкти методів](src/classes/test_method_objects.py)
    - [Змінні класу та екземпляра](src/classes/test_class_and_instance_variables.py)
    - [Успадкування](src/classes/test_inheritance.py)
    - [Множинне успадкування](src/classes/test_multiple_inheritance.py)
7. **Модулі**
    - [Модулі](src/modules/test_modules.py) (інструкція `import`)
    - [Пакети](src/modules/test_packages.py)
8. **Помилки та винятки**
    - [Обробка винятків](src/exceptions/test_handle_exceptions.py) (інструкція `try`)
    - [Генерування винятків](src/exceptions/test_raise_exceptions.py) (інструкція `raise`)
9. **Файли**
    - [Читання та записування](src/files/test_file_reading.py) (інструкція `with`)
    - [Методи файлових об'єктів](src/files/test_file_methods.py)
10. **Додатково**
    - [Інструкція `pass`](src/additions/test_pass.py)
    - [Генератори](src/additions/test_generators.py) (інструкція `yield`)
11. **Короткий огляд стандартних бібліотек**
    - [Серіалізація](src/standard_libraries/test_json.py) (бібліотека `json`)
    - [Шаблони пошуку файлів](src/standard_libraries/test_glob.py) (бібліотека `glob`)
    - [Пошук за шаблоном у рядках](src/standard_libraries/test_re.py) (бібліотека `re`)
    - [Математика](src/standard_libraries/test_math.py) (бібліотеки `math`, `random`, `statistics`)
    - [Дата і час](src/standard_libraries/test_datetime.py) (бібліотека `datetime`)
    - [Стиснення даних](src/standard_libraries/test_zlib.py) (бібліотека `zlib`)
12. **Введення користувача**
    - [Введення з терміналу](src/user_input/test_input.py) (інструкція `input`)

## Передумови

**Встановлення Python**

Переконайтеся, що на вашому комп'ютері [встановлено Python 3](https://realpython.com/installing-python/).

Ви можете використовувати стандартну бібліотеку Python [venv](https://docs.python.org/3/library/venv.html) для створення віртуальних середовищ, щоб Python, pip та всі залежні пакети встановлювалися й працювали з локальної теки проєкту, а не впливали на системні пакети та їхні версії.

Залежно від вашої інсталяції, доступ до інтерпретатора Python 3 можна отримати, виконавши команду `python` або `python3`. Те саме стосується менеджера пакетів pip — він може бути доступний через `pip` або `pip3`.

Перевірити версію Python можна, виконавши:

```bash
python --version
```

Зверніть увагу, що в цьому репозиторії, коли ви бачите `python`, мається на увазі Python **3**.

**Встановлення залежностей**

Встановіть усі необхідні залежності проєкту, виконавши:

```bash
pip install -r requirements.txt
```

## Тестування коду

Тести написані з використанням фреймворку [pytest](https://docs.pytest.org/en/latest/).

Ви можете додавати власні тести, створюючи файли та функції з префіксом `test_` (наприклад, `test_topic.py` з функцією `def test_sub_topic()` всередині).

Щоб запустити всі тести, виконайте з кореневої теки проєкту:

```bash
pytest
```

Щоб запустити окремі тести, виконайте:

```bash
pytest ./path/to/the/test_file.py
```

## Перевірка коду

Перевірка коду виконується за допомогою бібліотек [pylint](http://pylint.pycqa.org/) та [flake8](http://flake8.pycqa.org/en/latest/).

### PyLint

Щоб перевірити, чи написаний код відповідно до настанов зі стилю [PEP 8](https://www.python.org/dev/peps/pep-0008/), виконайте:

```bash
pylint ./src/
```

Якщо лінтер виявить помилку (наприклад, `missing-docstring`), ви можете дізнатися про неї більше, виконавши:

```bash
pylint --help-msg=missing-docstring
```

[Детальніше про PyLint](http://pylint.pycqa.org/)

### Flake8

Щоб перевірити, чи написаний код відповідно до настанов зі стилю [PEP 8](https://www.python.org/dev/peps/pep-0008/), виконайте:

```bash
flake8 ./src
```

Або, якщо ви хочете отримати детальніший вивід:

```bash
flake8 ./src --statistics --show-source --count
```

[Детальніше про Flake8](http://flake8.pycqa.org/en/latest/)

## Автор

- [@trekhleb](https://trekhleb.dev)
