# Movies API

Асинхронный REST API для управления коллекцией фильмов. Проект создан на FastAPI с использованием SQLAlchemy 2.0, SQLite и Alembic.

## Возможности

- Создание, просмотр, изменение и удаление фильмов (CRUD).
- Получение списка фильмов с фильтрацией.
- Сортировка по названию, году выпуска, рейтингу и ID.
- Проверка входных данных с помощью Pydantic.
- Асинхронная работа с базой данных SQLite.
- Управление структурой базы данных с помощью Alembic.

## Технологии

- Python
- FastAPI
- SQLAlchemy
- SQLite
- aiosqlite
- Alembic
- Pydantic
- pytest

## Структура проекта

```text
movie_project/
├── alembic/
│   └── versions/
├── src/
│   ├── models/
│   ├── repositories/
│   ├── routers/
│   ├── schemas/
│   ├── database.py
│   └── main.py
├── tests/
├── alembic.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Установка и запуск

1. Клонировать репозиторий:

```bash
git clone https://github.com/nedelskiynikita-dota2/movie_project.git
```

2. Перейти в папку проекта:

```bash
cd movie_project
```

3. Создать виртуальное окружение:

```bash
python -m venv .venv
```

4. Активировать виртуальное окружение.

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

5. Установить зависимости:

```bash
pip install -r requirements.txt
```

6. Применить миграции базы данных:

```bash
alembic upgrade head
```

7. Запустить приложение:

```bash
uvicorn src.main:app --reload
```

После запуска API будет доступно по адресу:

`http://127.0.0.1:8000`

Интерактивная документация Swagger:

`http://127.0.0.1:8000/docs`

## API Endpoints

| Метод | URL | Описание |
|---|---|---|
| GET | `/` | Проверка работы API |
| GET | `/movies/` | Получение списка фильмов |
| GET | `/movies/{movie_id}` | Получение фильма по ID |
| POST | `/movies/` | Создание фильма |
| PUT | `/movies/{movie_id}` | Полное обновление фильма |
| PATCH | `/movies/{movie_id}` | Частичное обновление фильма |
| DELETE | `/movies/{movie_id}` | Удаление фильма |

## Поля фильма

| Поле | Тип | Ограничения |
|---|---|---|
| id | integer | Создаётся автоматически |
| title | string | От 2 до 200 символов |
| genre | string | От 2 до 100 символов |
| rating | float | От 0 до 10 |
| year | integer | От 1888 до текущего года |

## Фильтрация и сортировка

Для получения списка фильмов доступны параметры:

- `year_min` — минимальный год выпуска.
- `year_max` — максимальный год выпуска.
- `min_rating` — минимальный рейтинг.
- `order_by` — поле и направление сортировки.
- `limit` — количество фильмов (максимум 100).
- `offset` — смещение для постраничного вывода.

Доступные значения `order_by`:

- `title` и `-title`
- `year` и `-year`
- `rating` и `-rating`
- `id` и `-id`

Пример запроса:

```text
GET /movies/?year_min=2000&min_rating=7&order_by=-rating&limit=10
```

## Пример создания фильма

Запрос:

```http
POST /movies/
```

Тело запроса:

```json
{
  "title": "Interstellar",
  "genre": "Sci-Fi",
  "rating": 8.7,
  "year": 2014
}
```

## Обработка ошибок

- `404 Not Found` — фильм с указанным ID не найден.
- `422 Unprocessable Entity` — переданы некорректные данные.

## База данных

Для хранения фильмов используется SQLite. Асинхронное взаимодействие с базой данных выполняется с помощью SQLAlchemy и aiosqlite.

Миграции базы данных управляются инструментом Alembic.
