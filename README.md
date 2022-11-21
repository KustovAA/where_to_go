# Сайт c интересными местами на карте города
[Открыть сайт](https://where-to-go-app.herokuapp.com/)
## Запуск

- Скачайте код
- python -m pip install pipenv (если не установлен pipenv)
- `pipenv shell`
- Установите зависимости командой `pipenv install`
- Создайте файл базы данных и сразу примените все миграции командой `python manage.py migrate`
- Запустите сервер командой `python manage.py runserver`


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта (обязательная переменная)
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `AWS_ACCESS_KEY_ID` - aws id пользователя
- `AWS_SECRET_ACCESS_KEY` - aws серетный ключ пользователя
- `AWS_STORAGE_BUCKET_NAME` - имя s3 бакета
- `AWS_URL` - ссылка на s3 бакет


## Добавление нового места
```
python manage.py load_place <url с данными места>
```
Пример данных:
```
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_long": "...Длинное описание...",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```