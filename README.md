# Книжный магазин на Django с Docker

Этот проект представляет собой онлайн-книжный магазин, разработанный на Django и развернутый с помощью Docker. Он позволяет пользователям просматривать каталог книг, авторизовываться и регистрироваться 

## Особенности

- Просмотр каталога книг с обложками, описаниями и ценами
- Регистрация и вход пользователей
- Использование Docker для упрощенного разворачивания и развертывания проекта

## Требования

- Docker
- Docker Compose

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/KrisStinaK/Bookstore.git
cd Bookstore
```

2. Соберите и запустите контейнеры:
```
docker-compose up -d --build
```
3. Выполните миграции внутри контейнера:
```
docker-compose exec web python manage.py migrate
```
4. Создайте суперпользователя для доступа к административной панели:
```
docker-compose exec web python manage.py createsuperuser
```
5. Откройте браузер и перейдите по адресу:
* Основной сайт: http://localhost
* Админка: http://localhost/anything-but-admin
## Структура проекта
* docker-compose.yml — конфигурация Docker Compose
* Dockerfile — описание сборки контейнера Django
* django_project - конфигурация проекта
* accounts - приложение для входа и авторизации пользователей
* books - приложение для просмотра книг
* pages - приложение для главной страницы и about
* static - статические файлы 
* staticfiles
* templates - шаблоны для страниц
* requirements.txt — зависимости проекта
## Остановка проекта
```
docker-compose down
```
## Дополнительно
* Для обновления зависимостей измените requirements.txt, затем пересоберите контейнер:
```
docker-compose build
docker-compose up -d
```
* Для получения логов:
```
docker-compose logs -f
```
