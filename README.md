# api_final
## Как запустить проект:
**Клонировать репозиторий и перейти в него в командной строке:**

> git clone https://github.com/vladsmailov/api_final_yatube.git

> cd api_final_yatube

**Cоздать и активировать виртуальное окружение:**

> python -m venv env

> venv/scripts/activate.ps1

**Установить зависимости из файла requirements.txt:**

> python -m pip install --upgrade pip

> pip install -r requirements.txt

**Выполнить миграции:**

> python3 manage.py migrate

**Запустить проект:**

> python3 manage.py runserver

## Примеры запросов:

**GET-запрос к адерсу:**

> http://127.0.0.1:8000/api/v1/posts/

вернет список постов из БД.

*Так же возможно получение данных с уточнением количества возвращаемых объектов и порядкового номера.*

**GET-запрос к адресу:**

> http://127.0.0.1:8000/api/v1/posts/?offset=3&?limit=2

вернет два поста с номерами 4 и 5, если такие номера имеются в БД

