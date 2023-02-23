# 學習 Python 的練習場（Playground）和速查表（Cheatsheet）

[![Build Status](https://travis-ci.org/trekhleb/learn-python.svg?branch=master)](https://travis-ci.org/trekhleb/learn-python)

> 此專案依據 [目錄](#目錄) 分類收集了 Python 腳本，包含了程式碼範例及解釋、不同的使用情境以及衍伸閱讀連結。

> _閱讀英文原始版本:_ [_English_](README.md), [_Português_](README.pt-BR.md), [_Español_](README.es-ES.md).

此專案名稱之所以叫做 **練習場（Playground）**，是因為您可以修改或是新增程式碼至範例中去觀察程式執行流程並使用斷言關鍵字（assert）來 [測試程式](#測試程式)。同時，此專案也使用了業界常用的工具來 [檢查程式碼](#檢查程式碼)，確保您所撰寫的程式碼符合官方建議的 Python 程式碼風格規範。

總而言之，此專案會使您的學習過程更具互動性，並幫助您從一開始學習的時候就使用高品質的程式碼。

此專案名稱之所以也包含了 **速查表（Cheatsheet）** 是因為您可以隨時透過此專案中的 [標準 Python 陳述式以及結構](#目錄) 回顧程式碼語法，也因為在此專案中的每個程式碼範例都使用了斷言來說明及教學，故您可以不用執行程式就看到函式/陳述式的預期輸出結果。

> 若對機器學習（Machine Learning）有興趣，可以參考專案原作者的另一個學習專案：🤖 [Interactive Machine Learning Experiments](https://github.com/trekhleb/machine-learning-experiments)

## 如何使用此專案儲存庫

在此專案儲存庫中的每一個 Python 腳本皆為以下結構：

```python
"""串列（Lists） <--- 此為主題名稱

# @詳見: https://www.learnpython.org/en/Lists <-- 此為延伸閱讀連結

此處可能會有針對此主題更多的詳細說明（例如：關於串列的基本使用方法）
"""

def test_list_type():
    """此處為子主題解釋

    每個檔案皆包含說明該子主題的測試函式（例如：串列型態、串列方法）
    """

    # 建立串列之範例 <-- 此行是解釋下一行程式碼動作之註解
    squares = [1, 4, 9, 16, 25]

    # 串列可以被索引（indexed）及切片（sliced）
    # 索引會回傳該索引位置之內容值
    assert squares[0] == 1 # <-- 利用斷言來呈現結果
    # 切片會回傳一個新的串列
    assert squares[-3:] == [9, 16, 25] # <-- 利用斷言來呈現結果
```

故您可以做以下動作：

- 找一個您想要學習或是回顧的 [主題](#目錄)。
- 閱讀註解及/或包含於腳本文件字串（docstring）中的延伸閱讀資料（如上述之程式碼範例）。
- 查看程式碼範例並利用斷言來展示使用範例及預期輸出。
- 修改程式碼或新增新的斷言來了解程式運作流程。
- [執行測試](#測試程式) 及 [檢查程式碼](#檢查程式碼) 來確認程式是否被正確撰寫及是否可以被正確執行。

## 目錄

1. **入門**
    - [Python 是什麼](src/getting_started/what_is_python.md)
    - [Python 語法](src/getting_started/python_syntax.md)
    - [變數](src/getting_started/test_variables.py)
2. **運算子**
    - [數學運算子](src/operators/test_arithmetic.py) (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
    - [位元運算子](src/operators/test_bitwise.py) (`&`, `|`, `^`, `>>`, `<<`, `~`)
    - [指派運算子](src/operators/test_assigment.py) (`=`, `+=`, `-=`, `/=`, `//=` 等 ...)
    - [比較運算子](src/operators/test_comparison.py) (`==`, `!=`, `>`, `<`, `>=`, `<=`)
    - [邏輯運算子](src/operators/test_logical.py) (`and`, `or`, `not`)
    - [恆等運算子](src/operators/test_identity.py) (`is`, `is not`)
    - [成員存取運算子](src/operators/test_membership.py) (`in`, `not in`)
3. **資料類型**
    - [數字](src/data_types/test_numbers.py)（包含布林值）
    - [字串](src/data_types/test_strings.py) 及相關方法
    - [串列](src/data_types/test_lists.py) 及相關方法（包含列表構建）
    - [元組](src/data_types/test_tuples.py)
    - [集合](src/data_types/test_sets.py) 及相關方法
    - [字典](src/data_types/test_dictionaries.py)
    - [類型轉換](src/data_types/test_type_casting.py)
4. **流程控制**
    - [`if` 陳述式](src/control_flow/test_if.py)
    - [`for` 陳述式](src/control_flow/test_for.py) (以及 `range()` 函式)
    - [`while` 陳述式](src/control_flow/test_while.py)
    - [`try` 陳述式](src/control_flow/test_try.py)
    - [`break` 陳述式](src/control_flow/test_break.py)
    - [`continue` 陳述式](src/control_flow/test_continue.py)
5. **函式**
    - [函式定義](src/functions/test_function_definition.py)（`def` 以及 `return` 陳述式）
    - [函式內變數作用範圍](src/functions/test_function_scopes.py)（`global` 以及 `nonlocal` 陳述式）
    - [預設引數](src/functions/test_function_default_arguments.py)
    - [關鍵字引數](src/functions/test_function_keyword_arguments.py)
    - [任意引數串列](src/functions/test_function_arbitrary_arguments.py)
    - [拆解引數串列](src/functions/test_function_unpacking_arguments.py)（`*` 以及 `**` 陳述式）
    - [Lambda 表達式](src/functions/test_lambda_expressions.py) (`lambda` 陳述式)
    - [文件字串](src/functions/test_function_documentation_string.py)
    - [函式註釋](src/functions/test_function_annotations.py)
    - [函式裝飾器](src/functions/test_function_decorators.py)
6. **類別**
    - [類別定義](src/classes/test_class_definition.py) (`class` 陳述式)
    - [類別物件](src/classes/test_class_objects.py)
    - [物件實體](src/classes/test_instance_objects.py)
    - [物件方法](src/classes/test_method_objects.py)
    - [類別及實體變數](src/classes/test_class_and_instance_variables.py)
    - [繼承](src/classes/test_inheritance.py)
    - [多重繼承](src/classes/test_multiple_inheritance.py)
7. **模組**
    - [模組](src/modules/test_modules.py) (`import` 陳述式)
    - [套件](src/modules/test_packages.py)
8. **錯誤和例外**
    - [例外處理](src/exceptions/test_handle_exceptions.py) (`try` 陳述式)
    - [例外引發](src/exceptions/test_raise_exceptions.py) (`raise` 陳述式)
9. **檔案**
    - [讀取和寫入](src/files/test_file_reading.py) (`with` 陳述式)
    - [檔案物件方法](src/files/test_file_methods.py)
10. **附加內容**
    - [`pass` 陳述式](src/additions/test_pass.py)
    - [生成器](src/additions/test_generators.py) (`yield` 陳述式)
11. **標準函式庫簡介**
    - [串列化](src/standard_libraries/test_json.py) (`json` 函式庫)
    - [檔案萬用字元](src/standard_libraries/test_glob.py) (`glob` 函式庫)
    - [字串規則比對](src/standard_libraries/test_re.py) (`re` 函式庫)
    - [數學運算](src/standard_libraries/test_math.py) (`math`, `random`, `statistics` 函式庫)
    - [日期和時間](src/standard_libraries/test_datetime.py) (`datetime` 函式庫)
    - [資料壓縮](src/standard_libraries/test_zlib.py) (`zlib` 函式庫)

## 使用此專案必備條件

**安裝 Python**

確認您已安裝 [Python3](https://realpython.com/installing-python/) 在您的電腦上。

您可能會想要使用標準 Python 函式庫所提供的 [虛擬環境](https://docs.python.org/3/library/venv.html) 功能在專案目錄中建立虛擬環境來佈署 Python 程式、pip 程式以及安裝所有需要的套件，藉此來避免作業系統中 Python 版本及相依性的混亂。

根據您的安裝方法，您可能可以通過以下方式執行 Python 3 直譯器：執行 `python` 或 `python3` 命令。pip 套件管理器執行方式也是如此：執行 `pip` 或 `pip3`。

您可以使用以下命令來確認 Python 版本：

```bash
python --version
```

此專案儲存庫中的所有程式碼皆是基於 Python **3**。

**安裝相依性套件**

透過以下命令安裝此專案需要的相依性套件：

```bash
pip install -r requirements.txt
```

## 測試程式

此專案使用 [pytest](https://docs.pytest.org/en/latest/) 測試框架來執行程式碼測試。

您可以新增以 `test_` 為開頭的檔案/函式來新增測試。（例如：`test_topic.py` 檔案內有 `def test_sub_topic()` 測試函式）

請從專案根目錄下使用以下命令來執行所有測試：

```bash
pytest
```

您也可以使用以下命令執行特定測試：

```bash
pytest ./path/to/the/test_file.py
```

## 檢查程式碼

此專案使用 [pylint](http://pylint.pycqa.org/) 以及 [flake8](http://flake8.pycqa.org/en/latest/) 函式庫來執行程式碼檢查。

### PyLint

檢查撰寫之程式碼是否符合 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 風格規範，請執行以下命令：

```bash
pylint ./src/
```

若此檢查工具偵測到錯誤（例如：`missing-docstring`），您可以使用以下命令查看特定錯誤之詳細說明：

```bash
pylint --help-msg=missing-docstring
```

[更多關於 PyLint](http://pylint.pycqa.org/)

### Flake8

檢查撰寫之程式碼是否符合 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 風格規範，請執行以下命令：

```bash
flake8 . /src
```

若您希望得到更多詳細的輸出，您可以加上以下參數再執行此工具：

```bash
flake8 . /src --statistics --show-source --count
```

[更多關於 Flake8](http://flake8.pycqa.org/en/latest/)

## 支持此專案

您可以透過 ❤️️ [GitHub](https://github.com/sponsors/trekhleb) 或 ❤️️ [Patreon](https://www.patreon.com/trekhleb) 支持原作者專案
