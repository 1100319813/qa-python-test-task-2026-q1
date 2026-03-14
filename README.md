# Swagger Petstore API тесты

![Python](https://img.shields.io/badge/python-3.11-blue)
![pytest](https://img.shields.io/badge/tests-pytest-green)
![async](https://img.shields.io/badge/async-await-blueviolet)
![allure](https://img.shields.io/badge/report-allure-orange)
![docker](https://img.shields.io/badge/service-docker-blue)

Асинхронный набор автотестов для REST API сервиса **Swagger Petstore**.
Тесты реализованы на Python с использованием `pytest` и проверяют основные эндпоинты API.

---

# Стэк

* Python 3.11+
* pytest
* pytest-asyncio
* pytest-xdist (параллельный запуск)
* httpx (асинхронный HTTP клиент)
* allure-pytest (отчёты)

---

# Основные функции

* Асинхронные API тесты (`async/await`)
* Параллельный запуск тестов (`pytest-xdist`)
* API client abstraction layer
* Генерация тестовых данных через `data_factory`
* Независимые тесты с автоматической очисткой данных
* E2E тестовые сценарии
* Allure отчёты

---

# Покрытые API эндпоинты

## Pet

* POST `/pet` — создание питомца
* PUT `/pet` — обновление питомца
* GET `/pet/{petId}` — получение питомца
* DELETE `/pet/{petId}` — удаление питомца
* GET `/pet/findByStatus` — поиск по статусу
* GET `/pet/findByTags` — поиск по тегам

Тесты включают:

* позитивные сценарии
* негативные сценарии
* E2E сценарии
* async parallel demo

---

## Store

* GET `/store/inventory`
* POST `/store/order`
* GET `/store/order/{orderId}`
* DELETE `/store/order/{orderId}`

Тесты включают:

* позитивные сценарии
* негативные сценарии
* жизненный цикл заказа

---

## User

* POST `/user`
* POST `/user/createWithList`
* GET `/user/login`
* GET `/user/logout`
* GET `/user/{username}`
* PUT `/user/{username}`
* DELETE `/user/{username}`

Тесты включают:

* позитивные сценарии
* негативные сценарии
* полный пользовательский E2E сценарий

---

# Тестовые сценарии

## Жизненный цикл питомца

1. Создать питомца  
2. Получить питомца по ID  
3. Обновить данные питомца  
4. Проверить обновлённые данные  
5. Удалить питомца  
6. Убедиться, что питомец удалён  

---

## Поиск питомцев

1. Создать несколько питомцев с одинаковым статусом  
2. Найти питомцев по статусу  
3. Убедиться, что все созданные питомцы присутствуют в результатах  

---

## Жизненный цикл заказа

1. Создать питомца  
2. Создать заказ для питомца  
3. Получить заказ по ID  
4. Удалить заказ  

---

## Полный пользовательский сценарий

1. Создать пользователя  
2. Выполнить вход пользователя (login)  
3. Создать питомца  
4. Создать заказ  
5. Получить заказ  
6. Удалить заказ  
7. Удалить пользователя  

---

# Структура проекта

```
app/
    client.py
    config.py
    api/
        pet_api.py
        store_api.py
        user_api.py
    utils/
        data_factory.py

tests/
    conftest.py
    test_smoke_api.py
    test_async_parallel_demo.py
    pet/
    store/
    user/

requirements.txt
pytest.ini
README.md
docker-compose.yml
```

---

# Требования

* Python 3.11+
* Docker
* Docker Compose
* Java (для Allure)

Проверка Java:

```
java -version
```

---

# Запуск Swagger Petstore

Из корня проекта:

```
docker compose up -d
```

После запуска доступны:

Swagger UI
http://localhost:8080

API base URL
http://localhost:8080/api/v3

Проверка API:

```
curl http://localhost:8080/api/v3/pet/findByStatus?status=available
```

Остановка сервиса:

```
docker compose down
```

---

# Установка зависимостей

Создать виртуальное окружение:

Windows PowerShell:

```
python -m venv venv
venv\Scripts\activate
```

Установить зависимости:

```
pip install -r requirements.txt
```

---

# Запуск тестов

Все тесты:

```
pytest -v
```

Только Pet:

```
pytest tests/pet -v
```

Только Store:

```
pytest tests/store -v
```

Только User:

```
pytest tests/user -v
```

---

# Параллельный запуск тестов

```
pytest -n 4 -v
```

---

# Отчеты Allure 

pytest сохраняет результаты тестов в папку:

```
allure-results
```

---

# Сгенерировать Static Report

```
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

# Пример полного локального запуска

```
docker compose up -d
pip install -r requirements.txt
pytest -n 4
allure serve allure-results
docker compose down
```

---

