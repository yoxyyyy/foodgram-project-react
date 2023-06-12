# foodgram-project-react
![example workflow](https://github.com/yoxyyyy/foodgram-project-react/actions/workflows/yamdb_workflow.yml/badge.svg)

## Суть проекта
Приложение «Продуктовый помощник»: сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд. 

Стек:
- Django
- Docker Compose
- Nginx
- Postgres

1. Клонировать репозиторий:

```
git clone ...
```

2. Добавить в клонированный репозиторий секреты (Settings/Secrets):

```
Переменная: USER, значение: <имя пользователя для подключения к серверу>
```
```
Переменная: HOST, значение: <публичный ip-адрес сервера>
```
```
Переменная: SSH, значение: <закрытый ssh-ключ для подключения к серверу>
```
```
Переменная: PASSPHRASE, значение: <пароль, если ssh-ключ защищён паролем>
```
```
Переменная: DOCKER_USERNAME, значение: <имя пользователя для поключения к DockerHub>
```
```
Переменная: DOCKER_PASSWORD, значение: <пароль для поключения к DockerHub>
```
```
Переменная: DB_ENGINE, значение: django.db.backends.postgresql
```
```
Переменная: DB_HOST, значение: db
```
```
Переменная: DB_NAME, значение: postgres
```
```
Переменная: DB_PORT, значение: 5432
```
```
Переменная: POSTGRES_USER, значение: postgres
```
```
Переменная: POSTGRES_PASSWORD, значение: postgres
```
```
Переменная: TELEGRAM_TO, значение: <токен Вашего телеграм-аккаунта>
```
```
Переменная: TELEGRAM_TOKEN, значение: <токен Вашего телеграм-бота>
```

3. Настроить nginx и docker-compose, дальше отправить их на сервер в папку infra/ 

```
scp docker-compose.yaml <пользователь_сервера>@<ip-адрес сервера>:/home/<домашняя папка>
```
```
scp -r /nginx <пользователь_сервера>@<ip-адрес сервера>:/home/<домашняя папка>
```

4. Создайте образ и отправьте его на dockerhub
```
docker login
docker build -t username/название_образа:latest .
docker push username/название_образа:latest
```
5. На удаленном сервере выполните 
```
sudo docker-compose up -d --build
```
6. После запуска контейнеров нужно выполнить миграции, накатить статику и загрузить даныные
```
sudo docker ps -a 
sudo docker exec -it <имя> python manage.py migrate
sudo docker exec -it <имя> python manage.py collectstatic
sudo docker-compose exec <имя> python manage.py createsuperuser
sudo docker exec -it <имя> python manage.py load_ingredients_json
```
7. Ссылка на проект 
docs: ip/adi/docs
admin: ip/admin