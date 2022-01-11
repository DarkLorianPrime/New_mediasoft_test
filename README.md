# New_mediasoft_test
# Kasimov Aleksander (alias Dmitry Glukhovsky) 🦊
____
/* Переписанное с flask на django тестовое задание Mediasoft про пару магазинов на паре улиц в паре городов */
____
Описание проекта:
Сервис, который принимает и отвечает на HTTP запросы. В случае успеха возвращает 200, в случае ошибки 400
Имеет предустановленную (в течение 2 недель :) ) реляционную базу данных.
____
Немного о роутах:
**city/** - Создание и получение городов
**city/CITY_ID/street/** - Создание и получение улиц в городе с ID - CITY_ID
**city/CITY_ID/street/STREET_ID/shop/** - Создание и получение магазинов. Имеет GET параметр OPEN, который в зависимости от своего значения(1\0) Выдает Открытые\Закрытые магазины.
____
Подготовительные действия:
1. Поставить python (желательно 3.9)
2. Прописать pip install -r requirements.txt в корне проекта
3. Python manage.py runserver - запускает тестовый сервер для тестирования всей этой фигни.
А как устанавливать на прод я вам не скажу :З
____
Логины и пароли:
mysql base (FREE) 
host: remotemysql.com
db: u6FqJ4w7Z2
user: u6FqJ4w7Z2
password: CMtzRCPvZD
Можете заменить двоеточие на = и вставлять в .env, хе-хе.
____
Как запускать проект:
Для теста просто Python manage.py runserver, для продакшена
https://yandex.ru/search/?text=как+установить+джанго+на+продакшене
