# <p align="center">SCRAPING</p>
# <p align="center">parcing_quotes.py</p>
Этот скрипт на Python извлекает цитаты, информацию об авторах (имя, дата рождения, место рождения) с сайта quotes.toscrape.com и сохраняет данные в базу данных PostgreSQL.

## Функции:

 * Авторизация: Скрипт выполняет вход на сайт с помощью логина и пароля .
 * Веб-скрапинг: Скрипт использует requests и BeautifulSoup для получения и анализа HTML-контента с нескольких страниц сайта.
 * Извлечение данных: Извлекает текст цитаты, имя автора, дату рождения и место рождения автора с каждой страницы.
 * Интеграция с базой данных: Создает таблицу Цитаты в PostgreSQL, вставляет извлеченные данные и управляет соединениями с базой данных с помощью psycopg2.
 * Переменные среды: Загружает конфиденциальную информацию (данные для входа в базу данных) из файла .env с помощью dotenv.
 * Пагинация: Проходит по нескольким страницам сайта, чтобы извлечь данные со всех доступных цитат.

## Установка:

1. Установите зависимости:
    ```
    pip install requests beautifulsoup4 psycopg2-binary python-dotenv
    ```

2. Создайте файл .env:
    ```
    DBNAME=имя_вашей_базы_данных
    USER=имя_пользователя_базы_данных
    PASSWORD=пароль_базы_данных
    ```

3. Заполните логин и пароль в коде:
     ```
    data = {
        "csrf_token": token,
        "username": "username",
        "password": "password"
    }
     ```
    Замените "username" и "password" на ваши учетные данные для входа на сайт quotes.toscrape.com.


5. Запустите скрипт:
     ```
    python parcing_quotes.py 
     ```
# <p align="center">parcing_goods.py</p>

Этот скрипт на Python извлекает информацию о товарах с сайта Scraping Club Exercise (https://scrapingclub.com/exercise/list_basic/) и сохраняет ее в базу данных PostgreSQL.

## Функции:

* Веб-скрапинг: Использует requests и BeautifulSoup для получения и анализа HTML-контента с нескольких страниц списков товаров.
* Извлечение данных: Определяет название, цену и описание товаров с отдельных страниц товаров.
* Интеграция с базой данных: Создает таблицу Товары  в PostgreSQL, вставляет извлеченные данные и управляет соединениями с базой данных с помощью psycopg2.
* Переменные среды: Загружает конфиденциальную информацию (данные для входа в базу данных) из файла .env с помощью dotenv.
* Пагинация: Проходит по нескольким страницам списка товаров, чтобы извлечь данные со всех доступных товаров.
* Ограничение скорости: Включает задержку в 3 секунды между запросами, чтобы избежать перегрузки целевого сервера.

## Установка:

1. Установите зависимости:
     ```
    pip install requests beautifulsoup4 psycopg2-binary python-dotenv
     ```

2. Создайте файл .env:
     ```
    DBNAME=имя_вашей_базы_данных
    USER=имя_пользователя_базы_данных
    PASSWORD=пароль_базы_данных
     ```

3. Запустите скрипт:
     ```
    python parcing_goods.py 
     ```
# <p align="center">parcing_quotes_tags.py</p>

Этот скрипт на Python извлекает цитаты, информацию об авторах (имя, дата рождения, место рождения) с сайта quotes.toscrape.com, группируя их по тегам, и сохраняет данные в базу данных PostgreSQL. 

## Функции:

* Извлечение тегов: Скрипт сначала получает список всех тегов, доступных на сайте.
* Сбор данных по тегам:  Скрипт перебирает каждый тег и собирает цитаты, авторов, даты рождения и места рождения авторов с соответствующих страниц сайта.
* Интеграция с базой данных: Создает таблицу Цитаты_по_тегам в PostgreSQL, вставляет извлеченные данные и управляет соединениями с базой данных с помощью psycopg2.
* Переменные среды: Загружает конфиденциальную информацию (данные для входа в базу данных) из файла .env с помощью dotenv.
* Ограничение скорости: Скрипт включает задержку в 3 секунды между запросами, чтобы избежать перегрузки целевого сервера.

## Установка:

1. Установите зависимости:
     ```
    pip install requests beautifulsoup4 psycopg2-binary python-dotenv
     ```

2. Создайте файл .env:
     ```
    DBNAME=имя_вашей_базы_данных
    USER=имя_пользователя_базы_данных
    PASSWORD=пароль_базы_данных
     ```

3. Запустите скрипт:
     ```
    python parcing_quotes_tags.py 
     ```
