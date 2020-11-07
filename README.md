## Gerald Manager

## Основная информация

Принимает информацию в слеующем виде:
```
[
    {
        "id": int,
        "name": str,
        "category": str,
        "uri": str,
        "relation_id": int,
        "sex": str,
        "born": str,
        "died": str
    },
]
```
Подобное хранение позволяет составить геральдическое/иерархическое дерево

## Формат объектов

Формирует в объекты item
{ "id": int, "name": str, "uri": str, "sex": str, "born": str, "died": str }
и в объекты relation
{ "id": int, "base_id": int, "second_id": int, "is_parent": bool, "is_wifehusband": bool}

Объект item представляет собой информацию о персонаже/человеке (имя, пол, годы рождения и смерти)

Объект relation отражает (родственные) связи между объектами item

## Необходимая корректировка

*Перед добавлением нового объекта item, происходит проверка на существование его в базе
*На данный момент проверка по полю uri, в идеале для более точной, корректной проверки, ее необходимо проводить основываясь на существующих связях, поскольку имя и годы рождения могут отличаться (быть не корректными, либо не быть вообще)
