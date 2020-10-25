## Вступление
Test_vectors это JSON API, который дает возможность пользователю создавать персон, добавлять к объекту вектор, образованный от изображения, сравнивать векторы.

## Стек
Python, Djangp, Django REST framework, docker, PostgreSQL, gunicorn

## Authorization 
API предназначет только для использования авторизованным пользователям.
Для получения доступа к API вам нужно зарегистрировать пользователя в task_manager POST запросом на http://127.0.0.1:8000/api/v1/register/ с параметрами *user* и *password*, после чего по POST запрос на http://127.0.0.1:8000/api/v1/token/ с теми же параметрами и вы получите JWT токен. 
При отправке любого запроса передавайте токен в заголовке **Authorization: Bearer <токен>**

## Доступные методы
| endpoint | Тип запроса | Описание |
| :--- | :--- | :--- | 
| api/v1/register/ | POST | Регистрация пользователя|
| api/v1/token/ | POST | Получение JWT токена (access и refresh)|
| api/v1/persons/ | GET, POST  | Получение списка id всех персон или создание новой персоны|
| api/v1/persons/{person_id}/ | GET, PUT, DELETE  | Получение, удаление, пoлное редактирование персоны по ее id|
| api/v1/persons/compare/{person_id_1}&{person_id_2}/| GET | Сравнение векторов двух персон |

## Примеры запросов

Пример запроса POST на api/v1/persons/

    {
        "first_name":"Йеннифер",
        "last_name": "Из Венгерберга"
    }

Пример ответа: 

    {
        "id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
    }
    
    
Пример запроса GET на api/v1/persons/

{

    {
        "id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
    }
    
    {
        "id": "afdk1243-9c0b-4ef8-bb6d-6bb9bd380a11",
    }
    
    {
        "id": "aht66if8-9c0b-4ef8-bb6d-6bb9bd380a11",
    }
    
}
## Инструкция к запуску
На вашей локальной машине должен быть установлен Docker
1. Склонировать репозиторий к себе на локальную машину
2. В корневой директории проекта файл .env и прописать, в нем следующее:
    ```
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    ```
3. Далее в теоминале выполнить команду `docker-compose up`.
4. Когда контейнер запустится, выполнить команду `docker stats` и узнать id контейнера, название которого заканчивается на web
5. Подключиться к контейнеру командой docker exec -it <id контейнера> bash
6. в контейнере выполнить команду python manage.py migrate
