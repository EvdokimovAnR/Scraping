# Scraping
Этот скрипт на Python извлекает цитаты, информацию об авторах (имя, дата рождения, место рождения) с сайта quotes.toscrape.com и сохраняет данные в базу данных PostgreSQL.

Функции:

Авторизация: Скрипт выполняет вход на сайт с помощью логина и пароля (заполните их в коде).
Веб-скрапинг: Скрипт использует requests и BeautifulSoup для получения и анализа HTML-контента с нескольких страниц сайта.
Извлечение данных: Извлекает текст цитаты, имя автора, дату рождения и место рождения автора с каждой страницы.
Интеграция с базой данных: Создает таблицу Цитаты в PostgreSQL, вставляет извлеченные данные и управляет соединениями с базой данных с помощью psycopg2.
Переменные среды: Загружает конфиденциальную информацию (данные для входа в базу данных) из файла .env с помощью dotenv.
Пагинация: Проходит по нескольким страницам сайта, чтобы извлечь данные со всех доступных цитат.

Как использовать:

1. Установите зависимости:
    
    pip install requests beautifulsoup4 psycopg2-binary python-dotenv
    

2. Создайте файл .env:
    
    DBNAME=имя_вашей_базы_данных
    USER=имя_пользователя_базы_данных
    PASSWORD=пароль_базы_данных
    

3. Заполните логин и пароль в коде:
    
    data = {
        "csrf_token": token,
        "username": "username",
        "password": "password"
    }
    
    Замените "username" и "password" на ваши учетные данные для входа на сайт quotes.toscrape.com.

4. Запустите скрипт:
    
    python имя_вашего_скрипта.py 
    
