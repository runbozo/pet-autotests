# Описание фреймворка
   Для установки зависимостей и создания виртуального окружения используется менеджер версий poetry.
   Также реализован выбор конфигурации окружения с помощью dynaconf.


Требования для запуска

* python>=3.7
* poetry

# Подготовка тестируемого приложения
   Для тестирования приложения contacts-api необходимо запустить его на localhost:8080 
   (подробно см. readme в приложении)

# Установка зависимостей
Poetry хранит информацию о необходимых пакетах в файле pyproject.toml
```sh
cd pet-autotests # Переходим в директорию pet-autotests, если вдруг еще не находимся в ней
poetry install
```

# Отчётность

1. Ставим java `openjdk-8-jre`

1. Качаем allure https://github.com/allure-framework/allure2/releases/
    ```sh
    wget https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/2.13.6/allure-commandline-2.13.6.zip
    ```

1. Распаковываем:
    ```sh
    unzip allure-commandline-2.13.6.zip
    ```

1. Смотрим отчёт:
    ```sh
    /path/to/allure-2.13.6/bin/allure serve allure_dir

    ```

# Конфигурация окружений
Управление конфигурациями сделано на основе библиотеки [dynaconf](https://www.dynaconf.com/).
Так как у нас тестовое приложение, рассчитанное на запуск только на _localhost_, доступен конфиг _dev_,
который и идет по умолчанию. Можно задать переменную окружения вручную.
Например, во время запуска тестового прогона
```shell
ENV_FOR_DYNACONF=dev pytest tests/
```
либо
```shell
export ENV_FOR_DYNACONF=dev
```
По умолчанию установленное окружение прописано в файле _/config.py_.
Конфиги находятся в файле _dev_settings.toml_ корня директории.

# Запуск

```sh
poetry run pytest tests --alluredir=results
```
или
```sh
poetry shell
pytest tests --alluredir=results
```

# Запуск ui тестов на локальном selenoid
1. Создаем в _env файл конфига для локального запуска, например local.yaml
2. Выполняем команды
```
poetry run invoke selenoid.up
poetry run pytest --env=<local.yaml> tests/web
```