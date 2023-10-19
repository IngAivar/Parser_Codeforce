# Parser for Codeforces

## Программа для решения задач на сайте Codeforces

## Технологический стек

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![PostgreSQL](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)
[![PostgreSQL](https://img.shields.io/badge/json-323330?style=for-the-badge&logo=json-web-tokens&logoColor=blue)](https://www.json.org/)
[![PostgreSQL](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://www.telegram.org/)

* Python 3.10
* Django
* Django REST framework
* PostgreSQL
* Docker and Docker Compose
* Celery
* Redis
* Unittest
* angiogram
* psycopg2


## Краткое описание

Этот проект представляет собой синтаксический анализатор, предназначенный для извлечения информации о программах из codeforces.com и их сохранения в
базе данных. Проект разработан с использованием Python 3.10 и Django REST framework. Проект включает в себя генерацию документации
с помощью Redoc и использует Celery для асинхронного выполнения задач. Redis используется в качестве посредника сообщений серверы PostgreSQL
- в качестве базы данных. Примечательно, что проект интегрируется с Telegram с целью отбора проблем на основе их
уровней сложности и тематики, а также для создания конкурсов, состоящих из 10 задач.


   ## Руководство по установке

1. Создайте файл .env, следуя примеру в файле .env.example.

2. Установите зависимости проекта перечисленные в requirements.txt файл.

3. Запуск контейнеров с помощью команды:

   ```bash
   docker-compose up -d
   ```

4. Создавать миграции:

   ```bash
    python manage.py makemigrations
   ```

5. Применять миграции:

   ```bash
    python manage.py migrate
   ```

6. Запустите Celery Worker для обработки асинхронных задач:

    ```bash
    celery -A parser_config worker -P eventlet -l INFO 
   ```
   
7. Запуск Celery Beat инициализирует Celery-beat который отвечает за планирование периодических задач:

   ```bash
    celery -A parser_config beat -l info -S django 
   ```
   
8. Запустите сервер:

   ```bash
   python manage.py runserver
   ```
   
9. Чтобы запустить Telegram-бота, выполните следующую команду:

   ```bash
    python manage.py telegram_bot
   ```
