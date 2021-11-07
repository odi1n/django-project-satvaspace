## [Тестовое задание - Satvaspace](/readme/task.md)

### Run project

1. Склонировать проект: `git clone git@gitlab.com:odi1n/django_project_satvaspace.git`
2. Перейти в дерикторию: `cd django_project_satvaspace`
3. Изменить файл `.env.example` на `.env`
4. `docker‐compose build`
5. Запуск автотестов: `docker‐compose up autotests`
6. Запуск Django runserver: `docker-compose up runserver`

#### Внимание
1. После запуска доступен будет по http://0.0.0.0:8000
2. Админ-панель, данные для входа беруться с .env.example: http://0.0.0.0:8000/admin

### Пример вызова API
|Действие|Тип запроса|Ссылка|данные|
|:---|:---:|:---:|:---:|
|[Получить все страницы](#получить-все-страницы)|GET|/api/pages/|-|
|[Получить информацию о странице](#получить-информацию-о-странице)|GET|/api/pages/2/|Номер страницы|

#### Получить все страницы
На одной странице выводиться - 25 записей
```json
{
    "count": 50,
    "next": "http://localhost:8000/api/pages/?page=2",
    "previous": null,
    "results": [
        {
            "id": 50,
            "title": "Приятель ставить нож монета.",
            "absolute_url": "http://localhost:8000/api/pages/50/"
        },
    ]
}
```

#### Получить информацию о странице
```json
{
    "id": 50,
    "title": "Приятель ставить нож монета.",
    "contents": [
        {
            "id": 243,
            "content_audio": null,
            "content_text": null,
            "content_video": {
                "id": 81,
                "created": "2021-11-07 19:21:47",
                "modified": "2021-11-07 19:21:47",
                "title": "Табак сопровождаться тута труп.",
                "counter": 23,
                "link": "https://www.npo.com/",
                "link_subtitles": "http://abi.biz/"
            }
        },
        {
            "id": 244,
            "content_audio": {
                "id": 88,
                "created": "2021-11-07 19:21:47",
                "modified": "2021-11-07 19:21:47",
                "title": "Поезд упор полевой полоска оборот.",
                "counter": 23,
                "link": "http://www.oao.info/",
                "bitrate": 75161,
                "bit_in_second": 413407
            },
            "content_text": null,
            "content_video": null
        },
        {
            "id": 245,
            "content_audio": null,
            "content_text": null,
            "content_video": {
                "id": 82,
                "created": "2021-11-07 19:21:47",
                "modified": "2021-11-07 19:21:47",
                "title": "Торопливый выдержать сбросить запретить дальний некоторый страсть.",
                "counter": 23,
                "link": "http://egorova.info/",
                "link_subtitles": "http://gruppa.biz/"
            }
        }
    ]
}
```